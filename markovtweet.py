# -*- coding: utf-8 -*-
import twitter_key
import tweepy
import MeCab
import markov
import sys
import random
import re
import xml.sax.saxutils as xssu

def trimtext(rawtext):
    m = MeCab.Tagger("-Owakati")
    text = rawtext.encode("utf-8")
    return ["__start__"] + [k if re.match(ur"^[A-Za-z]*$", k) == None else k + " " for i in text.split("\n") for k in m.parse(i).decode("utf-8").split(" ")] + ["__end__"]

favorite = lambda tl: [api.create_favorite(tweet.id) for tweet in tl if re.search(ur"てんきし|ten_kisi_bot", tweet.text) != None and not tweet.favorited]

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(twitter_key.CONSUMER_KEY, twitter_key.CONSUMER_SECRET)
    auth.set_access_token(twitter_key.ACCESS_TOKEN, twitter_key.ACCESS_SECRET)
    api = tweepy.API(auth)

    timeline = api.home_timeline(count=200)

    favorite(timeline)

    n = random.randint(3, 6)
    usabletimeline = [re.sub(r"@|https?://\S*\s*", "", xssu.unescape(i.text)) for i in timeline if re.match("RT @\w{1,15}:", i.text) == None]
    ngramdata = [markov.ngram(trimtext(i[:-1]), n) for i in usabletimeline]
    data = markov.flatten2D(ngramdata)
    mar = markov.Markov(data, n)
    tweet = "".join(mar.markov(100, "__start__", "__end__", lambda x: len("".join(x)), 140)[1:-1])
    
    #print tweet
    api.update_status(status=tweet)

