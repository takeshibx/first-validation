# First validation

Make sure you have followed the [installation
instructions](https://textbook.nipraxis.org/installation).  You will need
Git, Python and the various Python libraries installed.

```
cd $HOME/Documents
```

```{warning}
If you get `The system cannot find the path specified`, and you are on Windows,
make sure you are running a **Powershell** shell, not the much older Windows `cmd` shell.
```

Make a new directory to store your work, if you have not already done this in
the [installation instructions](https://textbook.nipraxis.org/installation).

```
mkdir nipraxis-work
```

Change your shell to that directory:

```
cd nipraxis-work
```

Nexc, clone the repository:

```
git clone https://github.com/nipraxis/first-validation
```

Then

```
cd first-validation
python get_data.py
```

You should see something like this:

```
Saving files to "data" directory
Fetched mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii to /Users/mb312/Library/Caches/nipraxis/0.4/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii
Copied /Users/mb312/Library/Caches/nipraxis/0.4/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii to data/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii
Fetched ds114_sub009_highres_brain_222.nii to /Users/mb312/Library/Caches/nipraxis/0.4/ds114_sub009_highres_brain_222.nii
Copied /Users/mb312/Library/Caches/nipraxis/0.4/ds114_sub009_highres_brain_222.nii to data/ds114_sub009_highres_brain_222.nii
Fetched 24719.f3_beh_CHYM.csv to /Users/mb312/Library/Caches/nipraxis/0.4/24719.f3_beh_CHYM.csv
Copied /Users/mb312/Library/Caches/nipraxis/0.4/24719.f3_beh_CHYM.csv to data/24719.f3_beh_CHYM.csv
Contents of "data" subdirectory:
   data/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii
   data/24719.f3_beh_CHYM.csv
   data/ds114_sub009_highres_brain_222.nii
```

You will see a different cache directory in the printout above.  My cache
directory was `/Users/mb312/Library/Caches/nipraxis/0.4/` but your directory
will be specific to you, and the current version of the `nipraxis` module.

If there are any errors, let us know.
