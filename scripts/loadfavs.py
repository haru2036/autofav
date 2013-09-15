#!/usr/bin/env python
#-*- coding:utf-8 -*-
import tweepy


class loadfavs:
    def __init__(self, consumer, consumersec , accesstoken , accsesssec):
        self.consumer_key = consumer
        self.consumer_secret = consumersec
        self.access_token = accesstoken
        self.access_secret = accsesssec
        self.api = None
        self.favlist = []

    def authuser(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token , self.access_secret)
        self.api = tweepy.API(auth)

    def getfavs(self):
        if self.api:
            print "please authenticate user"
            return
        for page in tweepy.Cursor(self.api.favorites).pages():
            self.favlist.append(page)

    def getfavslist(self):
        #TODO:ふぁぼのリストをreturnする処理
        pass



__author__ = 'haruka'
