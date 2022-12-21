"""
| Name:      logger.py
| Purpose:   Creates logging files for modules
|
| Created:   2022-04-22
| Modified:  2022-04-23
"""

import logging
import os
from datetime import datetime, timedelta
from glob import glob

# ==============================================================================
# LOGGING Constants
# ==============================================================================
LOG_FOLDER_PATH = None                 # Overrides the default log folder location ('d:\\logs')
DEBUG_LEVEL_FILE = 'DEBUG'             # Options 'DEBUG' | 'INFO' | 'ERROR' | 'CRITICAL'
DEBUG_LEVEL_CONSOLE = 'DEBUG'          # Options 'DEBUG' | 'INFO' | 'ERROR' | 'CRITICAL'
LOG_RETENTION_DAYS = 30                # Number of days to retain log files


def get_log_folder():
    """ Returns the log folder path based on default location or
        to the LOG_FOLDER_PATH constant
    :returns:         Log folder path
    """
    if LOG_FOLDER_PATH is None:
        return os.path.join(os.path.dirname(__file__), '..\\', 'logs')
    else:
        return LOG_FOLDER_PATH


def get_logging_levels(log_level):
    """ Returns the logging level based on the DEBUG_LEVEL_FILE or
        DEBUG_LEVEL_CONSOLE constant
    :param log_level  DEBUG_LEVEL constant
    :returns:         Log folder path
    """
    if log_level == 'DEBUG':
        return logging.DEBUG
    elif log_level == 'INFO':
        return logging.INFO
    elif log_level == 'WARNING':
        return logging.WARNING
    elif log_level == 'ERROR':
        return logging.ERROR
    elif log_level == 'CRITICAL':
        return logging.CRITICAL
    else:
        return logging.NOTSET


def create_logger(logname):
    """ Creates a logger object
        https://docs.python.org/2.7/howto/logging.html
    :param logname    String Name of the module
    :returns:         Logger object
    """
    # Create the logger and sets the logging level
    logger = logging.getLogger(logname)
    logger.setLevel(get_logging_levels(DEBUG_LEVEL_FILE))

    # Check if log folder exists and creates the log file
    logs_path = get_log_folder()
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    log_file = os.path.join(
        logs_path,
        datetime.now().strftime('%Y%m%d%H%M') + '-' + logname + '.log'
    )

    # Create the file and console handlers
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(get_logging_levels(DEBUG_LEVEL_FILE))
    console_handler = logging.StreamHandler()
    console_handler.setLevel(get_logging_levels(DEBUG_LEVEL_CONSOLE))

    # Create and assign the log formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers and return the logger object
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger, log_file


def delete_old_logs():
    """ Deletes a log files older than LOG_RETENTION_DAYS set in settings.py
    :returns:           n/a
    """
    # Get a list of files in the log folder path ending with .log
    log_expiration_date = datetime.today() - timedelta(days=LOG_RETENTION_DAYS)
    for log in glob(os.path.join(get_log_folder(), '*.log')):
        # Extract the log file date from the log filename
        filename = os.path.basename(log)
        file_date = datetime.strptime(filename[:8], "%Y%m%d")
        # Check if log is older than the retention days and delete old files
        if file_date < log_expiration_date:
            os.remove(log)
