"""helpers module
"""

import json

import pcap
import yaml


def get_adapters_names():
    """Finds all adapters on the system

    :return: A list of the network adapters available on the system
    """
    return pcap.findalldevs()


def config_loader_yaml(config_name):
    """Loads a .yml configuration file

    :param config_name: The path name of the yml configuration file
    :return: A dictionary of the configuration
    """
    with open(config_name, 'r') as f:
        config_yml = f.read()
    return yaml.load(config_yml)


def log_message(queue, level, module, function, message):
    """Sends a message to a log worker process

    :param queue: A queue to send the message to
    :param level: A string identifying the level of the message (Either DEBUG, INFO, WARNING, ERROR, CRITICAL
    :param module: A string identifying the source module of the message
    :param function: A string identifying the source function module of the message
    :param message: A string representing the message
    :return:
    """
    queue.put((level, module, function, message))
