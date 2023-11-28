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
mkdir -p tmp
echo "Running creation of $run script"
python merge.py $run 

echo "Will run:"
cat $run
echo "in parallel"

if [[ $np -eq 1 ]]; then
  while read line ; do
    echo "Running: ${line}"
    ${line}
  done < $run
else
  parallel -j$np < $run
fi
