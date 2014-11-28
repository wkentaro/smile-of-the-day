#! /usr/bin/env python
# -*- coding: utf-8 -*-
# sample_read_yaml.py

import yaml


def load_yaml(sns):
    f = open('api_key.yaml', 'r')
    data = yaml.load(f)
    f.close()

    return data[sns]

if __name__ == '__main__':
    import pprint

    data = load_yaml(sns='twitter')
    pprint.pprint(data)