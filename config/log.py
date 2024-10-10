import logging

from config import log_settings


class ErrorFilter(logging.Filter):
    def filter(self, record) -> bool:
        if record.levelno >= logging.ERROR:
            return True
        return False


class InfoFilter(logging.Filter):
    def filter(self, record) -> bool:
        if record.levelno <= logging.WARNING:
            return True
        return False


LOGGERS = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": log_settings.log_level,
        "handlers": ["console", "error_file", "info_file"],
    },
    "handlers": {
        "console": {
            "level": log_settings.log_level,
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
        "error_file": {
            "level": logging.ERROR,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": log_settings.log_dir / "errors.log",
            "mode": "a+",
            "backupCount": 3,
            "maxBytes": 5_000_000,
            "encoding": "utf-8",
            "filters": ["error_filter"],
        },
        "info_file": {
            "level": log_settings.log_level,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": log_settings.log_dir / "info.log",
            "mode": "a+",
            "backupCount": 3,
            "maxBytes": 5_000_000,
            "encoding": "utf-8",
            "filters": ["info_filter"],
        },
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] | %(name)s: %(funcName)s | %(message)s",
        },
    },
    "filters": {
        "error_filter": {
            "()": "config.log.ErrorFilter",
        },
        "info_filter": {
            "()": "config.log.InfoFilter",
        },
    },
}
