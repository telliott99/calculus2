import os
import util
from shutil import copyfile

ipath = '/Users/telliott/Github/calculus_book/'

p =   '/Users/telliott/Github/calculus2/files'
src = '/Users/telliott/Github/calculus_book/png/'
dst = '/Users/telliott/Github/figures/'

#----------------

L = os.listdir(p)
L.sort()


for fn in L:
    print(fn)
    data = util.load(p + '/' + fn)
    sL = util.get_fig_fn(data)
    for e in sL:
        print(e), 
        if os.path.isfile(dst + e):
            pass
        else:
            try:
                copyfile(src + e, dst + e)
            except IOError:
                pass
    print


