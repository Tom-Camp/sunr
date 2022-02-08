from sunr import __version__
import json


with open('configuration.json', 'r') as f:
    config = json.load(f)


def test_version():
    assert __version__ == '0.1.0'


def test_load_config():
    assert type(config) is dict


def test_config_color():
    assert len(config.get('color')) == 3


def test_config_delay():
    assert config.get('delay') > 0
    