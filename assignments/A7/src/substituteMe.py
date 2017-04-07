import csv
from pprint import pprint as pp


def chooseUsers():
    usersChosen = []
    with open("data/u.user") as f:
        reader = csv.reader(f, delimiter='|')

        for i in reader:
            age = int(i[1])
            # filter parameters
            if(i[2] == 'M' and i[3] == 'programmer' and
                    (age > 20 and age < 23)):
                usersChosen.append(i)

    return usersChosen


def findReviews(userIds):
    # pairs are user id -> array of reviews
    reviewDict = {}
    for i in userIds:
        reviewDict[i] = []
    with open("data/u.data", 'r') as f:

        for line in f:
            spl = line.split()
            for i in userIds:
                if(spl[0] == i):
                    reviewDict[i].append(spl)

    return reviewDict


def findMovie(movieId):
    with open("data/u.item", 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for i in reader:
            itemId = i[0]
            if movieId == itemId:
                # id, name, URI
                return (i[0], i[1], i[4])


def findMoviesMerge(reviewDict):
    userMovieDict = {}
    for userId, reviews in reviewDict.items():

        userMovieDict[userId] = {}
        moviesReviewed = []
        botMovies = []
        topMovies = []
        for r in reviews:
            movieId = r[1]
            rating = r[2]

            movie = findMovie(movieId)
            movie = tuple(rating) + movie
            moviesReviewed.append(movie)

        # botMovies.sort(key=lambda tup: tup[0])
        moviesReviewed.sort(key=lambda tup: tup[0])
        botMovies = moviesReviewed[:3]
        topMovies = moviesReviewed[-3:]
        userMovieDict[userId]["bottomMovies"] = botMovies
        userMovieDict[userId]["topMovies"] = topMovies

    return userMovieDict


if __name__ == "__main__":
    chosenUsers = chooseUsers()
    userIds = []
    for i in chosenUsers:
        userIds.append(i[0])

    reviewDict = findReviews(userIds)
    with open("data/closestUsers.txt", 'w') as f:
        pp(findMoviesMerge(reviewDict), stream=f)
