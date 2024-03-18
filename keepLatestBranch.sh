#!/bin/bash
username="menlin"
password="Qazwsx_112"

cur_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

while true
do
   git reset --hard
   git clean -fd
   git branch -D master-use
   git fetch origin master-use
   git checkout master-use
   git pull --rebase origin master-use
   sleep 6
   chmod -R 777 *
   exit 2
done
