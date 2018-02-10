#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcap

"""This is the helpers module
"""


def get_adapters_names():
    """Finds all adapters on the system

    :return: A list of the network adapters available on the system
    """
    return pcap.findalldevs()


def main():
    print(get_adapters_names())


if __name__ == '__main__':
    main()
