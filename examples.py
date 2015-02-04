#!/usr/bin/env python

import smuggle as smuggle
shijianTest = smuggle.smuggle(
    URL = "https://cdn.rawgit.com/wdbm/shijian/master/shijian.py"
)

def main():
    alpha = shijianTest.Clock(name = "alpha")
    alpha.printout()

if __name__ == '__main__':
    main()
