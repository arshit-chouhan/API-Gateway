A lightweight, production-inspired API Gateway built with FastAPI that centralizes authentication,
request routing, rate limiting, and monitoring for multiple backend microservices.

Architecture:

Client Request
      │
      ▼
┌─────────────────────┐
│    API Gateway       │  ← Port 8000
│                     │
│  1. Verify JWT      │
│  2. Check Rate Limit│
│  3. Route Request   │
│  4. Log Request     │
└─────────────────────┘
        │
   ┌────┴────┐
   ▼         ▼
User      Order
Service   Service
:8001     :8002

Tech Stack: FastAPI, JWT(Python Jose), Redis, HTML&CSS
