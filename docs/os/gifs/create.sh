#!/bin/bash
#
# Create all the terminalizer stuff
#

# Detect whether parallel is here
which parallel
has_parallel=$?

only_hash=0
np=1
while [[ $# -gt 0 ]]; do

  arg=$1
  shift
  case $arg in
    -n)
      if [[ $has_parallel -eq 0 ]]; then
        np=$1
      fi
      shift
      ;;
    --hash)
      only_hash=1
      shift
      ;;
    *)
      echo "Unknown argument: $arg"
      exit 1
      ;;
  esac

done

run=commands.run
rm -f $run
mkdir -p tmp
echo "Running creation of $run script"
python3 merge.py $run

if [ $only_hash -eq 1 ]; then
  echo "Only created the hash tables"
  exit 0
fi

echo "Will run:"
cat $run

if [[ $np -gt 1 ]]; then
  while read line ; do
    echo "Running: ${line}"
    ${line}
  done < $run
else
  parallel -j$np < $run
fi
