import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


class ResponseFormatter(logging.Formatter):
    def format(self, record):
        record.status = getattr(record, "status", "-")
        record.method = getattr(record, "method", "-")
        record.client_url = getattr(record, "client_url", "-")
        record.elapsed_ms = getattr(record, "elapsed_ms", "-")
        return super().format(record)


def setup_logging():
    fmt = ("%(levelname)s | %(asctime)s | status=%(status)s | %(method)s %(client_url)s | "
           "elapsed=%(elapsed_ms)s ms | %(message)s")
    datefmt = "%Y-%m-%d %H:%M:%S"
    handler = logging.StreamHandler()
    handler.setFormatter(ResponseFormatter(fmt=fmt, datefmt=datefmt))

    root = logging.getLogger()
    root.setLevel(LOG_LEVEL)
    root.handlers.clear()
    root.addHandler(handler)

    logging.getLogger("urllib3").setLevel("WARNING")
    return root
