#!/bin/bash
#
# Create all the terminalizer stuff
#
np=1
if [[ $# -gt 0 ]]; then
  np=$1
  shift
fi

run=commands.run
rm -f $run
rm -rf tmp
mkdir tmp
echo "Running creation of $run script"
python merge.py $run 

echo "Will run:"
cat $run
echo "in parallel"

parallel -j$np < $run
