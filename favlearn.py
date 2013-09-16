#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scripts import tweepywrapper, settingloader, generate_unigram_model


secrets = settingloader.loadsettings('secret.json')
setting = settingloader.loadsettings('settings.json')
loadfav = tweepywrapper.tweepywrapper(secrets['consumer_key'], secrets['consumer_secret'],
                         secrets['access_token_key'], secrets['access_token_secret'])


loadfav.authuser()
favs = loadfav.getfavs(test=False)
print favs

print 'model generate start.'

model = generate_unigram_model.generate_unigram_model(favs)

print model
print 'model generated.'


__author__ = 'haruka'

