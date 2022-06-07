#!/usr/bin/env python
from os import rename, listdir

badprefix = "co%20risks%20"
fnames = listdir('.')

for fname in fnames:
#    if fname.startswith(badprefix*2):
    rename(fname, fname.replace(badprefix, '', 1).replace("%20","-"))
