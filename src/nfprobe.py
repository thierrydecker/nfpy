#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""This is the main module of the Netflow probe
"""

import argparse
import src.commons.helpers as helpers


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-j", "--json", type=str, help="json configuration file name")
    group.add_argument("-y", "--yaml", type=str, help="yaml configuration file name")
    flags = parser.parse_args()
    print(flags)


if __name__ == '__main__':
    main()
