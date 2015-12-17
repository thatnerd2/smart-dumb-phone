import imp
import sys

if len(sys.argv) > 1:
    for i in sys.argv[1::]:
        try:
            imp.find_module(i)
            found = True
        except ImportError:
            found = False
        print "Module",i,"found:",found
