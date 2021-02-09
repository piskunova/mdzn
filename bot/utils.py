# -*- coding: utf-8 -*-
from pyaml import yaml


class _objectview(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class ConfigParser(_objectview):
    def __init__(self, config_fp):
        super().__init__(self.load_yaml(config_fp))

    @staticmethod
    def load_yaml(filepath):
        with open(filepath, 'r') as f:
            file = yaml.safe_load(f)
        return file
