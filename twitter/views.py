from django.shortcuts import render
from django.http import JsonResponse
import tweepy
import keys
from tweepy import OAuthHandler


def home(request):
    tweets = [None]
    content = {
        'tweets': tweets,
        'length': 0
    }

    if 'find' in request.POST:
        search_query = request.POST.get('find')
        if search_query is not "":
            print(search_query)
            auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
            auth.set_access_token(keys.access_token, keys.access_token_secret)
            api = tweepy.API(auth)
            search_query = search_query + " -filter:retweets"
            i = 1
            for tweet in tweepy.Cursor(api.search, count=150, q=search_query, tweet_mode='extended',                                        lang="en",
                                       since="2006-06-15", result_type="recent").items():
                tweets.append(tweet)
                i = i+1
                if i == 5:
                    break
            length = len(tweets)
            content.update({'tweets': tweets, 'length': length})

    return render(request, "index.html", content)
