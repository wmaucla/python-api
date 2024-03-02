from fastapi import FastAPI

from app.config import Config
from app.event_handlers import lifespan
from app.router import router


def get_app() -> FastAPI:
    fast_app = FastAPI(
        title=Config.NAME,
        version=Config.VERSION,
        lifespan=lifespan,
    )
    fast_app.include_router(router)
    return fast_app


app = get_app()


"""
Middleware functions can intercept requests and responses, allowing you to perform additional operations before they reach the route handler or before the response is sent. Here's an example of a FastAPI application with a middleware function:
"""
