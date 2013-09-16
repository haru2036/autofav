#!/usr/bin/env python
#-*- coding:utf-8 -*-
import tweepy
import judger
from tweepy.streaming import StreamListener

class tweepywrapper(StreamListener):
    def __init__(self, consumer, consumersec , accesstoken , accsesssec, classify=False):
        self.consumer_key = consumer
        self.consumer_secret = consumersec
        self.access_token = accesstoken
        self.access_secret = accsesssec
        self.auth = None
        if classify:
            self.api = None
            self.judger = judger.judger()


    def authuser(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.auth)

    def getfavs(self, test=False):
        if not self.api:
            print "please authenticate user"
            return

        favs=[]

        if not test:
            try:
                for page in tweepy.Cursor(self.api.favorites).pages():
                    favs.append([x for x in page])
            except tweepy.TweepError:
                print 'rate limit'
        else:
            print 'test mode'
            try:
                favlist = self.api.favorites()
                favs.append([x for x in favlist])

            except tweepy.TweepError:
                print 'rate limit'

        return favs

    def setfav(self, id):
        self.api.create_favorite(id)

    def on_status(self, status):

        print 'status recieved'
        if hasattr(status, 'text'):
            text = status.text
            judge = self.judger.judge(text)
            if judge:
                print 'fav'
                self.setfav(status.id)
        else:
            print 'status has no attribute text'



__author__ = 'haruka'
