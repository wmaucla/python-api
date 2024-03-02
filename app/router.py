from fastapi import APIRouter, Response, Body, Request, Depends, HTTPException
from datetime import timedelta
from app.jwt_handler import create_jwt_token, decode_jwt_token, LoginData

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
async def login_for_access_token(request: Request, login_data: LoginData = Body(...)):
    # For simplicity, check if username and password match a fixed value
    if login_data.username == "testuser" and login_data.password == "testpassword":
        # Create a simple token with user information
        token_data = {"sub": login_data.username}
        token = create_jwt_token(token_data, expires_delta=timedelta(minutes=15))
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# Protected endpoint that requires authentication
@router.get("/protected")
async def protected_route(
    request: Request, current_user: dict = Depends(decode_jwt_token)
):
    return {"message": "You are authenticated!", "user": current_user}
