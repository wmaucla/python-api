from contextlib import asynccontextmanager
from typing import AsyncGenerator
import logging
from fastapi import FastAPI

logger = logging.getLogger(__name__)


async def some_async_function():
    print("Async startup logic")


async def some_async_cleanup_function():
    logger.info("Shutting down")
    print("Shutting down")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await some_async_function()  # Called on startup
    yield
    await some_async_cleanup_function()  # Called on shutdown
