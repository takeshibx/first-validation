""" First validation
"""

from pathlib import Path

from hashlib import sha1

pth = Path() / 'data' / '24719.f3_beh_CHYM.csv'

contents = pth.read_bytes()
hash_value = sha1(contents).hexdigest()

print(f'Hash value for {pth} is {hash_value}')


def hash_for_fname(fname):
    return
