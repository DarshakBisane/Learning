from log_config import logger
import logging

logger = logging.getLogger(__name__)

try:
    result = 10/0

except Exception:
    logger.exception("lawde tere Baap ne Kiya kabhi aisa")