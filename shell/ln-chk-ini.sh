#!/bin/bash

cd $WORKSPACE
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lncmd="ln -sf local/dm814x-dev.git/dm814x-dev.ini dm814x-dev.ini"
print_color.sh -g "$lncmd"
$lncmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lncmd="ln -sf local/gitosis-admin.git/mirror.ini mirror.ini"
print_color.sh -g "$lncmd"
$lncmd

