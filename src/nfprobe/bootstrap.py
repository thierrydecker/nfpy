#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def config_loader(config_name):
    with open(config_name, 'r') as f:
        config_json = f.read()
    return json.loads(config_json)


def main():
    print(config_loader('config.json'))


if __name__ == '__main__':
    main()
