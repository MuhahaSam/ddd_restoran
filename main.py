from fastapi import FastAPI
from src.client.controller import client_controller

app = FastAPI(title="DDD restoran", root_path="/api/v1")
app.include_router(client_controller.router)
