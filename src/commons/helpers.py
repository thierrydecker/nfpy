#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcap
import json
import yaml

"""This is the helpers module
"""


def get_adapters_names():
    """Finds all adapters on the system

    :return: A list of the network adapters available on the system
    """
    return pcap.findalldevs()


def config_loader_json(config_name):
    """Loads a .json configuration file

    The config name has to be relative to the helpers.py location.

    :param config_name: The path name of the json configuration file
    :return: A dictionary of the configuration
    """
    with open(config_name, 'r') as f:
        config_json = f.read()
    return json.loads(config_json)


def config_loader_yaml(config_name):
    """Loads a .yml configuration file

    The config name has to be relative to the helpers.py location

    :param config_name: The path name of the yml configuration file
    :return: A dictionary of the configuration
    """
    with open(config_name, 'r') as f:
        config_yml = f.read()
    return yaml.load(config_yml)


def main():
    config = config_loader_json('../nfprobe/config.json')
    print('json -->', config)
    for key, value in config.items():
        print('json -->', key, value)
    config = config_loader_yaml('../nfprobe/config.yml')
    print('yaml -->', config)
    for key, value in config.items():
        print('yaml -->', key, value)


if __name__ == '__main__':
    main()
