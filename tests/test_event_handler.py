from unittest.mock import patch, call
from fastapi import FastAPI
from app.event_handlers import lifespan
import logging


logger = logging.getLogger(__name__)


async def test_lifespan():
    app = FastAPI(lifespan=lifespan)

    with patch("builtins.print") as mock_print:
        async with lifespan(app):
            # Add any additional test logic here if needed
            pass

    mock_print.assert_has_calls([call("Async startup logic"), call("Shutting down")])
