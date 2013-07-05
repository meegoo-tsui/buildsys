#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    git_add_remote.py
#  @brief   add remote for git
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
    git_add_remote_args = arg.git_add_remote_args()

    ## list repos
    for r in os.walk(os.getcwd()).next()[1]:
        if not str(r).find(".git"):
            continue
        # print ini
        if not git_add_remote_args['-p'] == "":
            group = str(git_add_remote_args['-u']).split(":")[-1] + str(r).split(".git")[0]
            print "[group " +  group + "]"
            print "members = @local/gitosis-admin"
            print "writable = " + group
            repo =  str(git_add_remote_args['-u']).split(":")[-1] + r
            print "[repo " + repo + "]"
            print "gitweb      = yes"
            print "description = clone at @ AAAAA/" + r
            print ""
            print "#" + "+"*79
            continue
        
        # push to new remote
        path.push()
        path.change(r)
        command = "git-push-local.sh " + git_add_remote_args['-u'] + r
        cmd.do(command)
        path.pop()

    sys.exit(0)
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
