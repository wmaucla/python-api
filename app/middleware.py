"""
Middleware functions can intercept requests and responses, allowing you to perform
additional operations before they reach the route handler or before the response is sent.
"""

from fastapi import Request


# Custom middleware to log the request path
async def log_path(request: Request, call_next):
    print(f"Request path: {request.url.path}")
    response = await call_next(request)
    return response
