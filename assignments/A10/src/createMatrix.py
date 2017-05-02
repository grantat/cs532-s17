
import feedparser
import re
import html


def remove_img_tags(data):
    '''
    Helper to remove img tags from description
    '''
    p = re.compile(r'<img.*?/>')
    return p.sub('', data)


def remove_emojis(data):
    '''
    Helper to remove emojis from description
    '''
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    d = emoji_pattern.sub(r'', data)
    return d


def getwordcounts(title, descrip):
    wc = {}

    # Extract a list of words
    words = getwords(title + ' ' + descrip)
    for word in words:
        wc.setdefault(word.strip(), 0)
        wc[word] += 1
    return title, wc


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


apcount = {}
wordcounts = {}
f = feedparser.parse('data/feed.xml')
counter = 0
for i, entry in enumerate(f.entries):
    t = html.unescape(entry["title"])
    t = t.replace('"', '')
    d = html.unescape(entry["description"])
    d = remove_img_tags(d)
    d = remove_emojis(d)
    d = d.replace('"', '')

    title, wc = getwordcounts(t, d)
    wordcounts[title] = wc
    for word, count in wc.items():
        apcount.setdefault(word, 0)
        if count > 1:
            apcount[word] += 1
    counter += 1
    if counter >= 100:
        break

wordlist = []
for w, bc in apcount.items():
    frac = float(bc) / 100
    # if frac>0.01 and frac<0.5:
    wordlist.append(w)
    if len(wordlist) >= 1000:
        break

out = open('data/feedData.txt', 'w')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for blog, wc in wordcounts.items():
    # print blog
    try:
        out.write(blog)
    except:
        out.write(str(blog.encode('utf-8')))
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')
