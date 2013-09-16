#/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
reset
git.py -s -p $WORKSPACE/buildsys.git
git.py -s -p $WORKSPACE/davinci-env.git
git.py -s -p $WORKSPACE/davinci-dev.git
git.py -s -p $WORKSPACE/$DAVINCI_SDK

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
exit 0

