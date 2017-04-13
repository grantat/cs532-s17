#!/bin/bash

# list of blogs
blogList=data/blogList.txt
if [ -f "$blogList" ]; then
	rm -f $blogList
fi

touch $blogList

# downloaded html blogs
blogDir=data/blogs/
if [ -d "$blogDir" ]; then
  rm -r $blogDir
fi

mkdir $blogDir

curl -s "http://f-measure.blogspot.com/" > "${blogDir}b001.html"
curl -s "http://ws-dl.blogspot.com/" > "${blogDir}b002.html"

echo "b001.html http://f-measure.blogspot.com/" >> $blogList
echo "b002.html http://ws-dl.blogspot.com/" >> $blogList

for (( i = 3; i <= 200; i++ )); do
	num=`seq -f%03g $i $i`
	uri=`curl -Ls -o data/b$num.html -w %{url_effective} "http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"`
	
	echo "b$num.html $uri" >> $blogList
done

#remove duplicate uri and page files
sort -u -k2 $blogList > data/tempList
sort -k1 data/tempList> $blogList
rm data/tempList

for file in `cat $blogList | cut -d' ' -f1`; do
	mv data/$file $blogDir	
done

# cleanup duplicate downloaded files
toDelete=$(find ./data -maxdepth 1 -name "*b*.html")
for item in $toDelete
do
	rm $item
done
