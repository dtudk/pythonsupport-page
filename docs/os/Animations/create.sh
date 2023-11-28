#!/bin/bash
#
# Create all the terminalizer stuff
#

run=commands.run
rm -f $run
rm -rf tmp
mkdir tmp
echo "Running creation of $run script"
python merge.py $run 

echo "Will run:"
cat $run
echo "in parallel"

parallel -j2 < $run
