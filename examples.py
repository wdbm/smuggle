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
# raises exception:
#gwappoTest = smuggle.smuggle(
#    URL = "httpsno://cdn.rawgit.com/wdbm/no/master/no.py"
#)

def main():
    alpha = shijianTest.Clock(name = "alpha")
    alpha.printout()
    sysTest.exit()

if __name__ == '__main__':
    main()
