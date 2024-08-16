package debug_util

import logging
from logging_config import set_log_level

def debug(bind_port_case):
    set_log_level('DEBUG')
    logging.debug(f'Debug message: Bind port case - {bind_port_case}')