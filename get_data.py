""" Script to get images and copy to this directory.

For a reminder about "pathlib" see https://textbook.nipraxis.org/pathlib.

For putting variables into strings, see
https://textbook.nipraxis.org/string_formatting
"""

from pathlib import Path

import nipraxis

filenames = ['mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii',
             'ds114_sub009_highres_brain_222.nii',
             '24719.f3_beh_CHYM.csv']

current_wd = Path()

# Make directory to contain data.
out_dir = current_wd / 'data'
if not out_dir.is_dir():
    out_dir.mkdir()
print(f'Saving files to "{out_dir}" directory')

for fname in filenames:
    # Fetch the file to a local cache directory.
    fetched_fname = nipraxis.fetch_file(fname)
    print(f'Fetched {fname} to {fetched_fname}')
    # Copy the file to the data directory
    contents = Path(fetched_fname).read_bytes()
    out_fname = out_dir / fname
    out_fname.write_bytes(contents)
    print(f'Copied {fetched_fname} to {out_fname}')

print('Contents of "data" subdirectory:')
for pth in out_dir.glob('*'):
    print('  ', pth)
