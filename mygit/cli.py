import argparse
import os

from . import data

def main():
    # use argparse to parse arguments
    args = parse_args()
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    return parser.parse_args()

# This command should initialize the directory by creating a new directory with current files
def init(args):
    data.init()
    print('Initialized empty mygit repo in %s' %os.path.join(os.getcwd(), MYGIT_DIR))
