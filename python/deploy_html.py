#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    deploy_html.py
#  @brief   deploy html to apache
#  @author  meegoo.tsui@gmail.com
#  @date    2013/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
apache_path = "/var/www"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
    printf.reset()
    printf.status("deploy html ...")

    # walk
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.split(".")[-1].upper() == "MD":
                of = root + "/" + f
                nf = root + "/" + f[0:len(f) - 2] + "html"
                command = "pandoc -s -S " + of + " -o " + nf
                cmd.do(command)
    # copy
    if not os.path.isdir(apache_path):
        printf.error("Error path: " + apache_path)
    command = "cp -rf * " + apache_path
    cmd.do(command)

    #delete
    command = "find " + apache_path + " -name \"*.md\" | xargs rm -f"
    cmd.do(command)

    sys.exit(0)
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
