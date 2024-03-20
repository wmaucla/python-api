from main import app
from uvicorn import run


def start_server() -> None:
    run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start_server()
