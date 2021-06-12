#!/bin/bash
# {
URL=$1
# re='^[0-9]+$'
# if ! [[ $URL =~ $re ]] ; then
#     URL="https://"$URL
# fi
mkdir outputs
echo "Searching with dirsearch: "
dir=$(pwd)
dirsearch -u $URL -r -o $dir/outputs/${URL:8:5}_$(date +"%m-%d-%y")_dirsearch.txt

echo "Searching with dirb: "
dirb $URL -o $dir/outputs/${URL:8:5}_$(date +"%m-%d-%y")_dirb.txt
echo "Searching with nikto: "
nikto -h $URL
# } |& tee $1_$(date +"%m-%d-%y").txt