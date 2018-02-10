#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcap

"""This is the helpers module
"""


def get_adapters_names():
    """Finds all interfaces on the system

    :return: A list of the interfaces available on the system
    """
    return pcap.findalldevs()


def main():
    print(get_adapters_names())


if __name__ == '__main__':
    main()
