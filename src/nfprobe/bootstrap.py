"""bootstrap module
"""

import argparse
import inspect
import multiprocessing

from ..commons.helpers import config_loader_yaml
from ..commons.helpers import log_message
from .workers import LoggingWorker


def main():
    """This is the entry point of the application
    """
    flags = parser_create()
    config_data = config_loader_yaml(flags.config_file)
    loggers_config = get_loggers_config(config_data)
    logging_queue = multiprocessing.Queue()
    logging_worker = LoggingWorker(loggers_config, logging_queue)
    logging_worker.start()

    fn_name = inspect.stack()[0][3]
    for i in range(5):
        log_message(logging_queue, 'DEBUG', __name__, fn_name, 'Message ' + str(i))
        log_message(logging_queue, 'INFO', __name__, fn_name, 'Message ' + str(i))
        log_message(logging_queue, 'WARNING', __name__, fn_name, 'Message ' + str(i))
        log_message(logging_queue, 'ERROR', __name__, fn_name, 'Message ' + str(i))
        log_message(logging_queue, 'CRITICAL', __name__, fn_name, 'Message ' + str(i))
        log_message(logging_queue, 'Unknown', __name__, fn_name, 'Message ' + str(i))

    logging_queue.put(None)
    logging_worker.join()


def parser_create():
    """Creates the arguments parser

    :return: command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config-file", type=str, help="yaml configuration file name")
    return parser.parse_args()


def get_adapters_config(config_data):
    """Extracts adapters configuration from configuration data

    :param config_data: A configuration file data
    :return: A dictionary of the adapters configuration
    """
    adapters = {k: config_data[k] for k in ('adapters',)}
    adapters = adapters['adapters']
    return adapters


def get_loggers_config(config_data):
    """Extracts loggers configuration from configuration data

    :param config_data: A configuration file data
    :return: A dictionary of the loggers configuration
    """
    loggers = {k: config_data[k] for k in ('loggers',)}
    loggers = loggers['loggers']
    return loggers
