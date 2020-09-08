from django.shortcuts import render
from django.http import JsonResponse
import tweepy
from tweepy import OAuthHandler

consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX"
access_token_secret = "XXX"


def home(request):

    content = {
        'tweets': None,
        'length': 0
    }

    if 'find' in request.POST:
        search_query = request.POST.get('find')
        if search_query is not "":
            print(search_query)
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            search_query = search_query + " -filter:retweets"
            tweets = api.search(search_query, count=100,
                                tweet_mode='extended', result_type='mixed')
            length = len(tweets)
            content.update({'tweets': tweets, 'length': length})

    return render(request, "index.html", content)
