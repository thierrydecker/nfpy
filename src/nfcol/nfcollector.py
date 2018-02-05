#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the main module of the Netflow collector

"""
import signal
import sys
import time


def nfcol_stopper(signum, stack):
    """Stops the Netflow collector

    :param signum: the signal number received
    :param stack: the stack when signal was received
    """
    print('NFCollector stopped')
    sys.exit(0)


def main():
    """Starts the Netflow collector

    """
    signal.signal(signal.SIGINT, nfcol_stopper)
    print('NFProbe started')
    while True:
        print('NFCollector is running... Press CTRL+C to stop it.')
        time.sleep(1)


if __name__ == '__main__':
    main()