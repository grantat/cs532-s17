#!/bin/bash

# src directory
script_dir=$(dirname $0)

queryTerm="California"
grepList=$(grep "$queryTerm" $script_dir/output/processed -rli | head -n 10)

# save 10 found
tenFromQuery=$(echo $script_dir/output/tenFromQuery.txt)

if [ -f $tenFromQuery ]; then
	echo "FILE EXISTS: $tenFromQuery"
	rm "$tenFromQuery"
fi

$(echo "$grepList" | sed 's/\(.*\).\/output\/processed\//\1 /' >> "$script_dir/output/tenFromQuery.txt")

# csv setup for output
csv=$(echo $script_dir/output/tfidf.csv)

if [ -f $csv ]; then
	echo "FILE EXISTS: $csv"
	rm "$csv"
fi

$(echo "TFIDF, TF, IDF, URI" >> $csv)

# loop through 10 items
for item in $grepList
do
	wordCount=$(grep -io "$queryTerm" $item | wc -l | bc)
	totalWords=$(wc -w < $item | bc)

	md5hash=$(echo $item | sed 's/\(.*\).\/output\/processed\//\1 /' | sed 's/\(.*\).txt/\1 /')
	# commas not legal in filenames so just search for first comma delimiter
	uri=$(grep $md5hash "$script_dir/output/md5Mapping.csv" | sed 's/,.*//')
	echo $uri

	echo "WordCount = $wordCount   totalWords= $totalWords"

	# TF-IDF = TF × IDF 
 	# = occurrence in doc / words in doc × 
	# log2(total docs in corpus / docs with term)
	# source http://www.worldwidewebsize.com/
	# 51 billion pages indexed by google
	# 1.66 billion results for 'California'

	idf=4.9412
	tf=$(echo "scale=5; $wordCount / $totalWords" | bc)
	tfidf=$(echo "scale=5; $tf * $idf" | bc)

	$(echo "$tfidf,$tf,$idf,$uri" >> $csv)
done


