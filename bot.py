# -*- coding: utf-8 -*-
import twitter_key
import tweepy
import markovtweet

def auth():
    auth = tweepy.OAuthHandler(twitter_key.CONSUMER_KEY, twitter_key.CONSUMER_SECRET)
    auth.set_access_token(twitter_key.ACCESS_TOKEN, twitter_key.ACCESS_SECRET)
    return tweepy.API(auth)

if __name__ == "__main__":
    api = auth()
    markovtweet.markovtweet(api)
