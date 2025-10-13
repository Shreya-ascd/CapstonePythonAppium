"""Centralized logger utility for the Appium framework."""

import logging
import os
from config.config import Config


class Logger:
    """Simple logger utility using Python’s logging module."""

    @staticmethod
    def get_logger(name):
        """Return a configured logger instance."""
        log_dir = Config.LOGS_DIR
        os.makedirs(log_dir, exist_ok=True)

        logger = logging.getLogger(name)
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler(os.path.join(log_dir, "test_execution.log"))
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] [%(name)s] - %(message)s",
                "%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Optional console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        return logger
