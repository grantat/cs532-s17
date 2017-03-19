# Assignment 3

Written in python 3.6.

Dependencies used:

- beautifulsoup

To install dependencies use the following command:

```shell
$ pip3 install -r requirements.txt
```

There is also an R dependency used for this assignment:

- Kendall

Used to calculate Kendall Tau_b.

# Assignment Details

Due: 11:59pm February 23

## 1.  Download the 1000 URIs from assignment #2.  

"curl", "wget", or "lynx" are all good candidate programs to use.  We want just the raw HTML, not the images, stylesheets, etc.

from the command line:

% curl http://www.cnn.com/ > www.cnn.com

% wget -O www.cnn.com http://www.cnn.com/

% lynx -source http://www.cnn.com/ > www.cnn.com

"www.cnn.com" is just an example output file name, keep in mind
that the shell will not like some of the characters that can occur
in URIs (e.g., "?", "&").  You might want to hash the URIs, like:

% echo -n "http://www.cs.odu.edu/show_features.shtml?72" | md5
41d5f125d13b4bb554e6e31b6b591eeb

("md5sum" on some machines; note the "-n" in echo -- this removes
the trailing newline.) 

Now use a tool to remove (most) of the HTML markup.  "lynx" will
do a fair job:

% lynx -dump -force_html www.cnn.com > www.cnn.com.processed

Use another (better) tool if you know of one.  

A "better" approach is to use BeautifulSoup, see:

http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text

for some hints on how to start.  Note that none of these methods 
are going to be perfect.

Keep both files for each URI (i.e., raw HTML and processed). 
Upload both sets of files to your github account.

## 2.  Choose a query term (e.g., "shadow") that is not a stop word (see week 5 slides) and not HTML markup from step 1 (e.g., "http") that matches at least 10 documents (hint: use "grep" on the processed files).  

If the term is present in more than 10 documents, choose
any 10 from your list.  (If you do not end up with a list of 10
URIs, you've done something wrong).

As per the example in the week 5 slides, compute TFIDF values for
the term in each of the 10 documents and create a table with the
TF, IDF, and TFIDF values, as well as the corresponding URIs.  The
URIs will be ranked in decreasing order by TFIDF values.  For
example:

Table 1. 10 Hits for the term "shadow", ranked by TFIDF.

TFIDF	TF	IDF	URI
-----	--	---	---
0.150	0.014	10.680	http://foo.com/
0.044	0.008	10.680	http://bar.com/


You can use Google or Bing for the DF estimation.  To count the
number of words in the processed document (i.e., the deonminator
for TF), you can use "wc":

% wc -w www.cnn.com.processed
    2370 www.cnn.com.processed

It won't be completely accurate, but it will be probably be
consistently inaccurate across all files.  You can use more 
accurate methods if you'd like, just explain how you did it.  

Don't forget the log base 2 for IDF, and mind your significant
digits!

https://en.wikipedia.org/wiki/Significant_figures#Rounding_and_decimal_places

## 3.  Now rank the same 10 URIs from question #2, but this time by their PageRank.  Use any of the free PR estimaters on the web, such as:

http://pr.eyedomain.com/
http://www.prchecker.info/check_page_rank.php
http://www.seocentro.com/tools/search-engines/pagerank.html
http://www.checkpagerank.net/

If you use these tools, you'll have to do so by hand (they have
anti-bot captchas), but there are only 10 to do.  Normalize the
values they give you to be from 0 to 1.0.  Use the same tool on all
10 (again, consistency is more important than accuracy).  Also
note that these tools typically report on the domain rather than
the page, so it's not entirely accurate.  

Create a table similar to Table 1:

Table 2.  10 hits for the term "shadow", ranked by PageRank.

PageRank	URI
--------	---
0.9		http://bar.com/
0.5		http://foo.com/

Briefly compare and contrast the rankings produced in questions 2
and 3.


## Question 4 is for 3 points extra credit

4.  Compute the Kendall Tau_b score for both lists (use "b" because
there will likely be tie values in the rankings).  Report both the
Tau value and the "p" value.

See: 
http://stackoverflow.com/questions/2557863/measures-of-association-in-r-kendalls-tau-b-and-tau-c
http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient#Tau-b
http://en.wikipedia.org/wiki/Correlation_and_dependence

## Question 5 is for 3 points extra credit

5.  Compute a ranking for the 10 URIs from Q2 using Alexa information
(see week 4 slides).  Compute the correlation (as per Q4) for all
pairs of combinations for TFIDF, PR, and Alexa.


## Question 6 is for 2 points extra credit

6.  Give an in-depth analysis, complete with examples, 
graphs, and all other pertinent argumentation for 
Kristen Stewart's (of "Twilight" fame) Erdos-Bacon number.


## Question 7 is for 2 points extra credit

7.  Build a simple (i.e., no positional information) inverted file
(in ASCII) for all the words from your 1000 URIs.  Upload the entire
file to github and discuss an interesting portion of the file in
your report.