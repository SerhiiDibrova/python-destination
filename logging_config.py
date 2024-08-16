import logging

def set_log_level(level):
    if level == 'DEBUG':
        logging.basicConfig(level=logging.DEBUG)
    elif level == 'INFO':
        logging.basicConfig(level=logging.INFO)

def enable_tracing():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

def disable_tracing():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)