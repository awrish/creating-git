import argparse
import os
import sys

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

    # Hashing data to store it 
    hash_obj_parser = commands.add_parser('hash-object')
    hash_obj_parser.set_defaults(func=hash_object)
    hash_obj_parser.add_argument('file')

    # printing hashed file
    catFileParser = commands.add_parser('cat-file')
    catFileParser.set_defaults(func=cat_file)
    catFileParser.add_argument('object')

    return parser.parse_args()

# This command should initialize the directory by creating a new directory with current files
def init(args):
    data.init()
    print('Initialized empty mygit repo in %s' %os.path.join(os.getcwd(), data.MYGIT_DIR))


# func to hash data
# follows git's method of hashing file based on contents

def hash_object(args):
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))

def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object))



