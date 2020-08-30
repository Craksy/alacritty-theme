#!/usr/bin/env python3

"""A small script to change the current alacritty color scheme from the shell"""

#Imports
from ruamel.yaml import YAML
import argparse
import os

yaml = YAML()
parser = argparse.ArgumentParser('alacritty-theme',
                                 description='Change alacritty color scheme from the shell')
parser.add_argument('theme',
                    help='the name of the theme to switch to.')
args = parser.parse_args()

alacritty_config_path = os.path.expanduser('~/.config/alacritty/alacritty.yml')
themes_folder = os.path.expanduser('~/.config/alacritty/themes')
theme_name = args.theme
theme_path = os.path.join(themes_folder, theme_name+'.yaml')

#read the current config and load the data into a python object
with open(alacritty_config_path, 'r') as config:
    config_data = yaml.load(config)

#read the theme provided and modify the config yaml
with open(theme_path, 'r') as theme:
    theme_data = yaml.load(theme)
    for k,v in theme_data.items():
        if k in config_data:
            config_data[k] = v

#write the changes back to the config
with open(alacritty_config_path, 'w') as config:
    yaml.dump(config_data, config)
