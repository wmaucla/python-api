import os


class _Config:
    VERSION = "v0.0.0"
    NAME = "Test Python App"
    ENV = os.getenv("APP_ENV", "local")


Config = _Config()
