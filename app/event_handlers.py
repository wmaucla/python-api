from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI


async def some_async_function():
    # Your asynchronous startup logic goes here
    print("Async startup logic")


async def some_async_cleanup_function():
    # Your asynchronous cleanup logic goes here
    print("Async cleanup logic")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await some_async_function()  # Called on startup
    yield
    await some_async_cleanup_function()  # Called on shutdown
