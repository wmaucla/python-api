from fastapi import APIRouter, Response
from fastapi import Depends, HTTPException
from datetime import timedelta

from app.jwt_handler import create_jwt_token, decode_jwt_token

router = APIRouter()


@router.get("/healthcheck", response_class=Response)
async def get_healthcheck() -> None:
    return None


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


# POST endpoint
@router.post("/post-example")
async def create_item(item: dict):
    return {"received_data": item}


@router.post("/token")
async def login_for_access_token(username: str, password: str):
    # For simplicity, check if username and password match a fixed value
    if username == "testuser" and password == "testpassword":
        # Create a simple token with user information
        token_data = {"sub": username}
        token = create_jwt_token(token_data, expires_delta=timedelta(minutes=15))
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# Protected endpoint that requires authentication
@router.get("/protected")
async def protected_route(current_user: dict = Depends(decode_jwt_token)):
    return {"message": "You are authenticated!", "user": current_user}
