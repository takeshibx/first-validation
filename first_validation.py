""" First validation
"""

from pathlib import Path

from hashlib import sha1

data_pth = Path() / 'data'
pth =  data_pth / '24719.f3_beh_CHYM.csv'

contents = pth.read_bytes()
hash_value = sha1(contents).hexdigest()

print(f'Hash value for {pth} is {hash_value}')

hashes_pth = data_pth / 'data_hashes.txt'

print(f'Contents of {hashes_pth}')
hashes_text = hashes_pth.read_text()
print(hashes_text)


def hash_for_fname(fname):
    return
