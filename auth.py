
from jose import jwt, JWTError
from fastapi import HTTPException, Header

SECRET = "secret123"
ALGO = "HS256"

def create_token(data):
    return jwt.encode(data, SECRET, algorithm=ALGO)

def verify_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.replace("Bearer ", "")
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
