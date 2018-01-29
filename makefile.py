# -*- coding: utf-8 -*-

'makeTextFile.py -- create text file'

import os
ls = os.linesep

#get filename
while True:
    fname = raw_input('please input file name:\n')
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

#get file content(text) lines
all_list = []
print "\nEnter lines ('. ' by itself to quit). \n"

# loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all_list.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all_list])
fobj.close()
print 'DONE!'