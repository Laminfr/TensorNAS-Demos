#!/usr/bin/bash

directory="."
script="DemoEASimple.py"
execution="."
py="python"

Help()
{
   echo "Run multiple tests using multiple config files"
   echo
   echo "Syntax: scriptTemplate [-g|h|v|V]"
   echo "options:"
   echo "e     Execution directory"
   echo "s     Script path relative to execution directory"
   echo "d     Config file directory relative to execution directory"
   echo "-p    Python version to use"
   echo
}

while getopts d:s:e:p:h: flag
do
    case "${flag}" in
        e) execution=${OPTARG};;
        s) script=${OPTARG};;
        d) directory=${OPTARG};;
        p) py=${OPTARG};;
        h) Help
          exit;;
    esac
done

echo "Running script: $script"
echo "In execution directory: $execution"
echo "Using configs in: $directory"

script=${script//[\/]/.}
script=${script::-3}
echo $script

cd $execution
echo "Moved to $execution for execution"

for f in "$directory"/*.cfg; do
  echo "$f"
  command="$py -m $script --config $execution/$f"
  echo $command
  exec $command
done