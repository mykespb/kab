#! /usr/bin/env python3

# Mikhail (myke) Kolodin, 2021
# ver. 2021-01-28 1.0
# find all bards' names, structure them

import os, os.path

__version__ = '0.1'
# print(f"{__version__=}")

dirs    = '/home/myke/bards/bardsh/архив'
subdirs = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ'

allnames = []

for subd in subdirs:
    dodir = os.path.join(dirs, subd)
    # print(f"{dodir=}")

    names = os.listdir(dodir)
    # print(names)

    for name in names:

        # print(f"[{name=}]", end=" -- ")
        if os.path.isdir(name):
            namesplit = name.split()
            # print("is dir", namesplit)
            allnames += [namesplit]
        elif os.path.isfile(name):
            # print("is file")
            pass
        else:
            # print("notype")
            namesplit = name.split()
            # print("is dir", namesplit)
            allnames += [namesplit]

    # names = [ d for d in os.listdir(dodir) if os.path.isdir(d) ]
    # print(f"{names=}")

# print(f"{allnames=}")
for aname in allnames:
    print(','.join(aname))
