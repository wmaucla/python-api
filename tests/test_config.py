import os
from app.config import _Config


def test_config_version():
    assert _Config.VERSION == "v0.0.0"


def test_config_name():
    assert _Config.NAME == "Test Python App"


def test_config_env():
    assert _Config.ENV == os.getenv("APP_ENV", "local")
