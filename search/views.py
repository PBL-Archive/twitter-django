from django.shortcuts import render
from django.http import JsonResponse
import tweepy
import keys
from tweepy import OAuthHandler
from dotenv import load_dotenv
import os
load_dotenv()

def home(request):
    tweets = [None]
    content = {
        'tweets': tweets,
        'length': 0
    }

    if 'find' in request.POST:
        search_query = request.POST.get('find')
        search_count = request.POST.get('count')
        if search_count == '':
            search_count = 100
        if search_query is not "":
            auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET"))
            auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))
            api = tweepy.API(auth, wait_on_rate_limit=True)
            search_query = search_query + " -filter:retweets"
            i = 1
            for tweet in tweepy.Cursor(
                api.search,
                count=int(search_count),
                q=search_query,
                tweet_mode='extended',
                lang='en',
                result_type='mixed',
            ).items():
                tweets.append(tweet)
                i = i+1
                if i > int(search_count):
                    break
            length = len(tweets)
            content.update({'tweets': tweets, 'length': length})

    return render(request, "search.html", content)
