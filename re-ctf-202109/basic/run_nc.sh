#!/bin/bash
if [ $# != 1 ]; then
  echo "Usage: run_nc.sh ./program"
else
  ncat -klvne $1 127.0.0.1 9000
fi
