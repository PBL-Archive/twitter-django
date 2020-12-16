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
        search_count = int(request.POST.get('count'))
        if search_count == '':
            search_count = 100
        if search_query is not "":
            auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
            auth.set_access_token(keys.access_token, keys.access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            search_query = search_query + " -filter:retweets"
            i = 1
            for tweet in tweepy.Cursor(
                api.search,
                count=search_count,
                q=search_query,
                tweet_mode='extended',
                lang='en',
                result_type='mixed',
            ).items():
                tweets.append(tweet)
                i = i+1
                if i > search_count:
                    break
            length = len(tweets)
            content.update({'tweets': tweets, 'length': length})

    return render(request, "search.html", content)
