from fastapi import FastAPI
from app.routes import user_router

app = FastAPI(title="KubeCI User Service")

app.include_router(user_router, prefix="/users")
