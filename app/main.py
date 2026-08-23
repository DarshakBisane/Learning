import log_config
import logging

logger = logging.getLogger(__name__)

logger.debug("This is a DEBUG message")
logger.info("Application started successfully")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

