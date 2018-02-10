#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcap
import json
import os

"""This is the helpers module
"""


def get_adapters_names():
    '''Finds all adapters on the system

    :return: A list of the network adapters available on the system
    '''
    return pcap.findalldevs()


def config_loader(config_name):
    '''Loads a .json configuration file

    The config name has to be relative to the helpers.py location

    :param config_name: The path name of the json configuration file
    :return: A dictionary of the configuration
    '''
    with open(config_name, 'r') as f:
        config_json = f.read()
    return json.loads(config_json)


def main():
    pass


if __name__ == '__main__':
    main()
