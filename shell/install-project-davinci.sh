#/bin/sh

EXEC_DIR=$EXE_INSTALL"/dm814x-evm/project"
FILESYS_INSTALL_PATH=$NFSBOOT"/filesys-dm814x-evm"

if [ -d $EXEC_DIR ]; then
	if [ -d $FILESYS_INSTALL_PATH ]; then
		CMD="cp -rf  $EXEC_DIR/* $FILESYS_INSTALL_PATH"
		echo $CMD
		$CMD
	else
		echo "$FILESYS_INSTALL_PATH - not exist !"
	fi
else
	echo "$EXEC_DIR - not exist !"
fi

