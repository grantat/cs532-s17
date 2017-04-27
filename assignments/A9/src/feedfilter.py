import feedparser
import re
import html

# Takes a filename of URL of a blog feed and classifies the entries


def read(feed, classifier, trainCount):
    # Get feed entries and loop over them
    f = feedparser.parse(feed)
    # open known classified feeds
    cat = {}
    with open("data/classifiedFeeds.txt", "r") as cfeeds:
        for j, item in enumerate(cfeeds):
            cat[j] = item

    # store results for probability later
    results = []
    for i, entry in enumerate(f.entries):
        if(i == 100):
            break
        print()
        print('-----')
        # Print the contents of the entry
        t = html.unescape(entry["title"])
        t = t.replace('"', '')
        d = html.unescape(entry["description"])
        d = remove_img_tags(d)
        d = remove_emojis(d)
        d = d.replace('"', '')
        print('Title:     ' + t)
        print()
        print(d)

        entryDict = {}
        entryDict['Title'] = t

        # Combine all the text to create one item for the classifier
        fulltext = '%s\n%s' % (t, d)

        # Print the best guess at the current category
        guess = str(classifier.classify(fulltext))
        entryDict['Guess'] = guess
        print('Guess: ' + guess)
        cl = ""
        for key, val in cat.items():
            if(i == key):
                cl = val
                break

        # remove newline
        cl = cl.rstrip()
        print('Actual Category: ' + cl)
        entryDict['Actual'] = cl
        results.append(entryDict)

        if i <= trainCount:
            # train on already known category
            classifier.train(fulltext, cl)

    return results


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


def entryfeatures(entry):
    splitter = re.compile('\\W*')
    f = {}

    # Extract the title words and annotate
    titlewords = [s.lower() for s in splitter.split(entry['title'])
                  if len(s) > 2 and len(s) < 20]
    for w in titlewords:
        f['Title:' + w] = 1

    # Extract the summary words
    summarywords = [s.lower() for s in splitter.split(entry['summary'])
                    if len(s) > 2 and len(s) < 20]

    # Count uppercase words
    uc = 0
    for i in range(len(summarywords)):
        w = summarywords[i]
        f[w] = 1
        if w.isupper():
            uc += 1

        # Get word pairs in summary as features
        if i < len(summarywords) - 1:
            twowords = ' '.join(summarywords[i:i + 1])
            f[twowords] = 1

    # Keep creator and publisher whole
    f['Publisher:' + entry['publisher']] = 1

    # UPPERCASE is a virtual word flagging too much shouting
    if float(uc) / len(summarywords) > 0.3:
        f['UPPERCASE'] = 1

    return f
