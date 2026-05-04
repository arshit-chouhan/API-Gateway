# API Gateway
A lightweight, production-inspired API Gateway built with FastAPI that centralizes authentication,
request routing, rate limiting, and monitoring for multiple backend microservices.

# Features
- JWT Authentication — Stateless token-based auth. Every request is verified before routing.
- Sliding Window Rate Limiting — Max 10 requests per user per 60 seconds. Prevents abuse and DDoS.
- Dynamic Request Routing — Incoming requests are matched against a service registry and forwarded to the correct microservice.
- Request Logging — Every routed request is logged with path and status code.
- Monitoring Dashboard — Live view of registered services and recent request logs via a Jinja2 web dashboard.

# Tech Stack
FastAPI, JWT(Python Jose), Redis, HTML&CSS
