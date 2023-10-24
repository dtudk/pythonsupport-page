#!/usr/bin/bash

# Copyright 2023
# Python Installation Support
# The Technical University of Denmark

echo Will now delete all Pythons in $HOME/Library/Python
sudo rm -rf ~/Library/Python
echo Will now delete all Pythons in /Application/Python
sudo rm -rf /Applications/Python*
echo Will now delete all Pythons in /Library/Frameworks/Python.framework
sudo rm -rf /Library/Frameworks/Python.framework

names="pip pydoc python idle 2to3"

for name in ${names} ; do
	echo Searching for executable named: $name
	for file in /usr/local/bin/${name}* ; do 
	echo Checking file $file
  # TODO typo? &&
		[ -e $file ] || sudo rm $file
	done 
done

echo Now deleting anaconda and/or miniconda

# if anaconda is installed, delete it
if [ -d ~/anaconda* ] ; then
	source ~/anaconda3/bin/activate
	conda install anaconda-clean --yes
	anaconda-clean --yes
	conda deactivate
	rm -rf ~/anaconda*
	rm -rf ~/.anaconda_backup
fi

# if miniconda is installed, delete it
if [ -d ~/miniconda* ] ; then
	rm -rf ~/miniconda*
fi

echo script finished

# TODO:
# skal man eventuelt slette den der 'path' linje? -- se guide evt. 
# Removing Anaconda path from .bash_profile
