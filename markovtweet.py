# -*- coding: utf-8 -*-
import MeCab
import markov
import random
import re
import xml.sax.saxutils as xssu

START="__START__"
END="__END__"

def trimtext(rawtext):
    m = MeCab.Tagger("-Owakati")
    text = rawtext.encode("utf-8")
    putspace = lambda word: word if re.match(ur"^[A-Za-z]*$", word) == None else word + " "
    return [START] + [putspace(k) for i in text.split("\n") for k in m.parse(i).decode("utf-8").split(" ")] + [END]

favorite = lambda api, tl: [api.create_favorite(tweet.id) for tweet in tl if re.search(ur"てんきし|ten_kisi_bot", tweet.text) != None and not tweet.favorited]

def markovtweet(api):
    timeline = api.home_timeline(count=200)
    n = random.randint(2, 5)
    removeword = lambda text: re.sub(r"@|https?://\S*\s*", "", text)
    usabletimeline = [removeword(xssu.unescape(tw.text)) for tw in timeline if re.match("RT @\w{1,15}:", tw.text) == None]
    ngramdata = [markov.ngram(trimtext(text), n) for text in usabletimeline]
    data = markov.flatten2D(ngramdata)
    mar = markov.Markov(data, n)
    tweet = "".join(mar.markov(100, START, END, lambda x: len("".join(x)), 140)[1:-1])
    
    #print tweet
    favorite(api, timeline)
    api.update_status(status=tweet)

