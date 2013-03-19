#!/bin/bash

cd $WORKSPACE
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lncmd="ln -sf github/checkopen.git/github.ini github.ini"
print_color.sh -g "$lncmd"
$lncmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lncmd="ln -sf local/gitosis-admin.git/local.ini local.ini"
print_color.sh -g "$lncmd"
$lncmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lncmd="ln -sf local/gitosis-admin.git/mirror.ini mirror.ini"
print_color.sh -g "$lncmd"
$lncmd

