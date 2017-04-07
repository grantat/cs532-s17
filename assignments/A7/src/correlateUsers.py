
import csv
from math import sqrt
from pprint import pprint as pp


def sim_pearson(prefs, p1, p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def findCorrelations(prefs):
    most_correlated = []
    least_correlated = []
    correlations = {}
    substituteMe = str(868)

    users = {}
    for line in open('data/u.user'):
        (user, age, gender, job, zipcode) = line.split('|')
        users.setdefault(user, {})
        users[user] = {'age': age, 'gender': gender,
                       'job': job, 'zipcode': zipcode}

    for user, rest in users.items():
        if substituteMe == user:
            pass
        else:
            r = sim_pearson(prefs, substituteMe, user)
            correlations[int(user)] = r

    correlations = sorted(correlations.items(), key=lambda x: x[1])
    pp(correlations)
    least_correlated = correlations[:5]
    most_correlated = correlations[-5:]

    with open("data/correlatedUsers.txt", 'w') as f:
        print("Most Correlated:", file=f)
        pp(most_correlated, stream=f)
        print("Least Correlated:", file=f)
        pp(least_correlated, stream=f)


def transformPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result


def getRecommendations(prefs, person, similarity=sim_pearson):
    '''
    Gets recommendations for a person by using a weighted average
    of every other user's rankings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
        # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    # Return the sorted list
    rankings.sort()

    lowestRankings = rankings[:5]
    topRankings = rankings[-5:]

    return (lowestRankings, topRankings)


def topMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson,
):
    '''
    Returns the best matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()
    # scores.reverse()
    lowestScores = scores[:n]
    highestScores = scores[-n:]
    return (lowestScores, highestScores)


def loadMovieLens(path='./'):
    # Get movie titles
    movies = {}
    for line in open(path + 'data/u.item', encoding="ISO-8859-1"):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    # Load data
    prefs = {}
    for line in open(path + 'data/u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs


def saveScores(filename, lowScores, highScores):
    with open(filename, 'w') as f:
        print("Lowest Scores:", file=f)
        pp(lowScores, stream=f)
        print("Highest Scores:", file=f)
        pp(highScores, stream=f)


if __name__ == "__main__":
    # q2
    prefs = loadMovieLens()
    findCorrelations(prefs)
    # 868 is substiteMe
    # q3
    getRecommendations(prefs, '868')
    # q4
    prefs = transformPrefs(prefs)
    (lowestScore, highestScore) = topMatches(prefs, 'Citizen Kane (1941)')
    saveScores("data/favoriteFilmCorrelation.txt", lowestScore, highestScore)
    (lowestScore, highestScore) = topMatches(prefs, 'Mars Attacks! (1996)')
    saveScores("data/worstFilmCorrelation.txt", lowestScore, highestScore)
