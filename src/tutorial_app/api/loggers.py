from logging.config import dictConfig
from typing import Any

AppContext = Any
LoggingConfig = Any


def init_logger(app_context: AppContext) -> None:

    config = {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": str(app_context.log_path),
                "formatter": "default",
                "level": app_context.logging_level,
            },
            "stream": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": app_context.logging_level,
            },
        },
    }

    dictConfig(config)
