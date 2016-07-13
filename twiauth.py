import tweepy
import twikeys

def getauth():
    
    auth = tweepy.OAuthHandler(twikeys.keys["consumer_key"], twikeys.keys["consumer_secret"]) 
    auth.set_access_token(twikeys.keys["access_token"], twikeys.keys["access_secret"])
    return auth
