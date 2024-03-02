from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Config
from app.event_handlers import lifespan
from app.router import router
from app.middleware import log_path


def get_app() -> FastAPI:
    fast_app = FastAPI(
        title=Config.NAME,
        version=Config.VERSION,
        lifespan=lifespan,
    )
    fast_app.include_router(router)
    return fast_app


app = get_app()

# Middleware function to add CORS headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace with specific origins as needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Add the custom middleware
app.middleware("http")(log_path)
