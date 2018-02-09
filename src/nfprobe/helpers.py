#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcap

"""This is the helpers module
"""


def find_all_interface():
    """Finds all interfaces on the system

    :return: A list of the interfaces available on the system
    """
    return pcap.findalldevs()
