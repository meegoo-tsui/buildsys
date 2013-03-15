#!/bin/sh

# name and email
git config --global user.name "meegoo tsui"
git config --global user.email "meegoo.tsui@gmail.com"

# chinese font
git config --global gui.encoding utf-8
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding gbk

# fie mode and edit
git config --global core.fileMode false
git config --global core.editor vim

# global ignore
git config --global core.excludesfile '~/.gitignore'

