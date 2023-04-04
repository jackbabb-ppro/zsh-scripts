#!/bin/zsh
if [ $# -lt 1 ]; then
	echo "Fetches all git repos in a folder"
	echo "Usage: $0 <parent folder>"
	return;
fi
cd $1
find . -type d -maxdepth 1 -exec git --git-dir={}/.git --work-tree=$1/{} fetch \;
