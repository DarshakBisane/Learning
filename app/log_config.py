import logging 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class DebugErrorFilter(logging.Filter):

    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.ERROR)


lformat = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

hformat = logging.Formatter(
    "%(name)s | %(message)s | %(asctime)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(hformat)

file_Handler = logging.FileHandler("logs/app.log")
file_Handler.setLevel(logging.DEBUG)
file_Handler.setFormatter(lformat)

error_handler = logging.FileHandler("logs/error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(lformat)

custom_handler = logging.FileHandler("logs/debug_error.log")
custom_handler.setLevel(logging.DEBUG)
custom_handler.addFilter(DebugErrorFilter())
custom_handler.setFormatter(lformat)

logger.addHandler(console_handler)
logger.addHandler(file_Handler)
logger.addHandler(error_handler)
logger.addHandler(custom_handler)