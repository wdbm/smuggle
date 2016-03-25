#!/usr/bin/env python

import smuggle
shijian_test = smuggle.smuggle(
    URL = "https://cdn.rawgit.com/wdbm/shijian/master/shijian.py"
)
sys_test = smuggle.smuggle(
    module_name = "sys"
)
# raises exception:
#zappo_test = smuggle.smuggle(
#    module_name = "zappo"
#)
# raises exception:
#gwappo_test = smuggle.smuggle(
#    URL = "httpsno://cdn.rawgit.com/wdbm/no/master/no.py"
#)

def main():
    alpha = shijian_test.Clock(name = "alpha")
    alpha.printout()
    sys_test.exit()

if __name__ == '__main__':
    main()
