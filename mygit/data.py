import os
import hashlib

MYGIT_DIR = '.mygit'

def init():
    os.makedirs(MYGIT_DIR)
    os.makedirs(f'{MYGIT_DIR}/objects')


# hashes file based on contents
def hash_object(data):

    oid = hashlib.sha1(data).hexdigest()

    file = f'{MYGIT_DIR}/objects/{oid}'

    with open(f'{MYGIT_DIR}/objects/{oid}', 'wb') as output:
        output.write(data)

    return oid

def get_object(oid):
    file = f'{MYGIT_DIR}/objects/{oid}'

    with open(file, 'rb') as f:
        return f.read()


