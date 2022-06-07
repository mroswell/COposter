#!/usr/bin/env python
# Adapted from https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python


from os import rename, listdir

badprefix = "co-conditions-"
fnames = listdir('.')

for fname in fnames:
#    if fname.startswith(badprefix*2):
    rename(fname, fname.replace(badprefix, '', 1).replace("%20","-"))
