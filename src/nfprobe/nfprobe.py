#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the main module of the Netflow probe

"""
import signal
import sys
import time


def nfprobe_stopper(signum, stack):
    """Stops the Netflow probe

    :param signum: the signal number received
    :param stack: the stack when signal was received
    """
    print('NFProbe stopped')
    sys.exit(0)


def main():
    """Starts the Netflow probe

    """
    signal.signal(signal.SIGINT, nfprobe_stopper)
    print('NFProbe started')
    while True:
        print('NFProbe is running... Press CTRL+C to stop it.')
        time.sleep(1)


if __name__ == '__main__':
    main()
