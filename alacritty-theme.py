#!/usr/bin/env python3

import yaml
from yaml import CLoader as Loader, CDumper as Dumper
import argparse
import sys, os

parser = argparse.ArgumentParser('alacritty-theme',
                                 description='Change alacritty color scheme from the shell')
parser.add_argument('name',
                    help='the name of the theme to switch to.')

args = parser.parse_args()

print(args.name)


alacritty_config_path = os.path.expanduser('~/.config/alacritty/alacritty.yml')
themes_folder = os.path.expanduser('~/.config/alacritty/themes')
theme_name = args.name

theme_path = os.path.join(themes_folder, theme_name+'.yaml')


#read the current config and load the data into a python object
with open(alacritty_config_path, 'r') as config:
    config_data = yaml.load(config, Loader=Loader)

#read the theme provided and modify the config yaml
with open(theme_path, 'r') as theme:
    theme_data = yaml.load(theme, Loader=Loader)

    for k,v in theme_data.items():
        if k in config_data:
            config_data[k] = v

#write the changes back to the config
with open(alacritty_config_path, 'w') as config:
    yaml.dump(config_data, config)
