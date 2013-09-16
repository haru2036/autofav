#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scripts import tweepywrapper, settingloader
from tweepy import Stream, TweepError



secrets = settingloader.loadsettings('secret.json')
twpy = tweepywrapper.tweepywrapper(secrets['consumer_key'], secrets['consumer_secret'],
                         secrets['access_token_key'], secrets['access_token_secret'], classify=True)
twpy.authuser()
stream = Stream(twpy.auth, twpy, secure=True)
try:
    stream.userstream()
except(TweepError):
    print TweepError

__author__ = 'haruka'
