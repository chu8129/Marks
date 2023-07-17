import logging
import sys
import os
import socket
from logging.handlers import RotatingFileHandler
from config import LOG_DIR


class Logger:
    _logger = None

    def __new__(cls, *args, **kwargs):
        if cls._logger is None:
            cls._logger = logging.getLogger("root")
            if not cls._logger.handlers:

                formatter = logging.Formatter("%(levelname)9s | %(asctime)s [%(filename)s:%(lineno)d] %(message)s")

                streamHandler = logging.StreamHandler()
                fileHandler = RotatingFileHandler(
                    os.path.join(LOG_DIR, "widget-host-%s.log" % socket.gethostname()),
                    mode="a",
                    maxBytes=5 * 1024 * 1024,
                    backupCount=2,
                    encoding=None,
                    delay=0,
                )

                cls._logger.setLevel(logging.DEBUG)

                fileHandler.setFormatter(formatter)
                streamHandler.setFormatter(formatter)

                cls._logger.addHandler(fileHandler)
                cls._logger.addHandler(streamHandler)

        return cls._logger



if __name__ == "__main__":
    log = Logger()
    log.info("info ...")
    log.debug("debug ...")
    log.warning("warning ...")
