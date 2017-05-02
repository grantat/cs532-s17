#!/bin/bash

# create doirectories if not there
script_dir=$(dirname $0)

dir="$script_dir/data/html"
if [ ! -d "$dir" ]; then
	mkdir $dir
fi

csv="$script_dir/data/md5Mapping.csv"
if [ ! -f "$csv" ]; then
	touch $csv
fi


for uri in $(cat $script_dir/data/finalURIs.txt)
do
	# completed md5 on macbook
	hashedURI=$(echo -n $uri | md5)
	outputFile="$script_dir/data/html/$hashedURI.html"

	$(echo "$uri,$hashedURI" >> $csv)
	$(curl -L -m 3 -A "Mozilla/5.0" $uri > $outputFile)
done