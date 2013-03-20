#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    mk_chk_ini.py
#  @brief   make a ini file for check.py
#  @author  meegoo.tsui@gmail.com
#  @date    2013/03/20

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.arg            import arg
from   utils.path           import path
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
    printf.reset()
    mk_chk_ini_args = arg.mk_chk_ini_args()

    ## list repos
    for r in os.walk(mk_chk_ini_args['-p']).next()[1]:
        print r

    sys.exit(0)
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
