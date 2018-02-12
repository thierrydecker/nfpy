"""bootstrap module
"""

import argparse

from ..commons.helpers import config_loader_json
from ..commons.helpers import config_loader_yaml


def main():
    """This is the entry point of the application
    """
    flags = parser_create()
    if flags.json:
        config_data = config_loader_json(flags.json)
    else:
        config_data = config_loader_yaml(flags.yaml)


def parser_create():
    """Creates the arguments parser

    :return: command line arguments
    """
    #
    # Create parser
    #
    parser = argparse.ArgumentParser()

    #
    # Either -j/--json or -y/--yaml flag has to be set
    #
    config_group = parser.add_mutually_exclusive_group(required=True)
    config_group.add_argument("-y", "--yaml", type=str, help="yaml configuration file name")
    config_group.add_argument("-j", "--json", type=str, help="json configuration file name")

    #
    # Get flags
    #
    return parser.parse_args()
