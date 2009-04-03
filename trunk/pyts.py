import sys
import urllib2
import json

def printTweet(result):
    print(result['from_user'] + " said: " + result['text'])

def getTweets(searchTerm):
    url = 'http://search.twitter.com/search.json?q='+searchTerm
    tweets = json.loads(urllib2.urlopen(url).read())['results']
    map(printTweet, tweets)

if __name__ == "__main__":
    searchTerms = []
    searchTerms = sys.argv[1:]
    map(getTweets, searchTerms)
