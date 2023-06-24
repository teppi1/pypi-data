#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

rm -rf .git/
git init -b main .

mkdir -p squash/
fd -H --ignore -t=f | rg -v "^.git/" >squash/all_files.txt
pv -N "Creating import" squash/all_files.txt | python3 scripts/import.py squash/import_stream.txt | python3 scripts/create_commit.py >squash/commit_stream.txt

pv -N "Importing" squash/import_stream.txt squash/commit_stream.txt | git fast-import
rm -rf squash/

#echo "Addding"
#fd . -t=f --exclude="release_data/" | parallel --eta --progress --xargs "git add"
#git commit -m "Fresh start, all files"
