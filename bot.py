#!/opt/local/bin/python2.7 -u
# -*- coding: utf-8 -*-
import tweepy
import twiauth
import markovtweet

if __name__ == "__main__":
    auth = twiauth.getauth()
    api = tweepy.API(auth)
    markovtweet.markovtweet(api)
