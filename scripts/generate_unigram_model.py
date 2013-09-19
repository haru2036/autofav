#!/usr/bin/env python
#-*- coding:utf-8 -*-
import mecabCaller
import cpickler


def generate_unigram_model(favs):
    try:
        freqfav = cpickler.frompickle(filename='favs_model_unigram.dump')
    except:
        freqfav = {}

    esc = [u'…', u'・', u'.', u',', u'、', u'。', u'!', u'?', u'！', u'？']
    for favlist in favs:
        for fav in favlist:
            itemlist = mecabCaller.parse(fav.text)
            for itemraw in itemlist:
                item = [x for x in itemraw if x in esc]
                if item in freqfav:
                    freqfav[item] += 1
                else:
                    freqfav[item] = 1
    cpickler.topickle(freqfav, filename='favs_model_unigram.dump')

    return freqfav

__author__ = 'haruka'
