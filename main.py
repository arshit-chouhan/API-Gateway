
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from auth import create_token, verify_token
from rate_limiter import check_rate_limit
from logger import log_request, get_logs

app = FastAPI(title="Personal API Gateway")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SERVICES = {
    "/users": "http://localhost:8001",
    "/orders": "http://localhost:8002"
}

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login():
    token = create_token({"user": "admin"})
    return {"token": token}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    logs = get_logs()
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "logs": logs, "services": SERVICES}
    )

@app.api_route("/{path:path}", methods=["GET","POST"])
async def gateway(path: str, request: Request, token: str = Depends(verify_token)):
    await check_rate_limit(token)

    full_path = "/" + path

    for route in SERVICES:
        if full_path.startswith(route):
            log_request(full_path, 200)
            return {"message": f"Request routed to {SERVICES[route]}"}

    log_request(full_path, 404)
    raise HTTPException(status_code=404, detail="Service not found")
