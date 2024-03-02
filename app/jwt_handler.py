import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel

# Secret key for signing and verifying JWT
SECRET_KEY = "test_secret_key"
ALGORITHM = "HS256"


class LoginData(BaseModel):
    username: str
    password: str


# Function to create a JWT token
def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to decode and verify a JWT token
def decode_jwt_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
