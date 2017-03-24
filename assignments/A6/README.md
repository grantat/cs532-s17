# Assignment 6

Written in Python 3.6 and Javascript. Javascript dependencies are already inside this repository, the main script being twitterFriendships.js.

D3 Visualizations hosted here (takes a few seconds for graphs to center):

https://cdn.rawgit.com/grantat/cs532-s17/b410d0d7/assignments/A6/src/index.html

Python Dependencies used:

- tweepy

To install dependencies use the following command:

```shell
$ pip3 install -r requirements.txt
```

# Assignment Details

Due: 11:59pm March 23

## 1.  D3 graphing (10 points)

Use D3 to visualize your Twitter followers.  Use my twitter account
("@phonedude_mln") if you do not have >= 50 followers.  For example,
@hvdsomp follows me, as does @mart1nkle1n.  They also follow each
other, so they would both have links to me and links to each other.

To see if two users follow each other, see:
https://dev.twitter.com/rest/reference/get/friendships/show

Attractiveness of the graph counts!  Nodes should be labeled (avatar
images are even better), and edge types (follows, following) should
be marked.

Note: for getting GitHub to serve HTML (and other media types), see:
http://stackoverflow.com/questions/6551446/can-i-run-html-files-directly-from-github-instead-of-just-viewing-their-source

Be sure to include the URI(s) for your D3 graph in your report. 

## Extra credit: (5 points) 2.  Gender homophily in your Twitter graph 

Take the Twitter graph you generated in question #1 and test for
male-female homophily.  For the purposes of this question you can
consider the graph as undirected (i.e., no distinction between
"follows" and "following").  Use the twitter name (not "screen
name"; for example "Michael L. Nelson" and not "@phonedude_mln")
and programatically determine if the user is male or female.  Some
sites that might be useful:

https://genderize.io/

https://pypi.python.org/pypi/gender-detector/0.0.4

Create a table of Twitter users and their likely gender.  List any 
accounts that can't be determined and remove them from the graph.

Perform the homophily test as described in slides 11-16, Week 8.

Does your Twitter graph exhibit gender homophily?

## Extra credit: (3 points) 3.  Using D3, create a graph of the Karate club before and after the split.

- Weight the edges with the data from: 
http://vlado.fmf.uni-lj.si/pub/networks/data/ucinet/zachary.dat

- Have the transition from before/after the split occur on a mouse
click.  This is a toggle, so the graph will go back and forth beween
connected and disconnected.
