#!/usr/bin/env python

import smuggle
shijianTest = smuggle.smuggle(
    URL = "https://cdn.rawgit.com/wdbm/shijian/master/shijian.py"
)
sysTest = smuggle.smuggle(
    moduleName = "sys"
)
# raises exception:
#zappoTest = smuggle.smuggle(
#    moduleName = "zappo"
#)

def main():
    alpha = shijianTest.Clock(name = "alpha")
    alpha.printout()
    sysTest.exit()

if __name__ == '__main__':
    main()
