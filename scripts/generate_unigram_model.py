#!/usr/bin/env python
#-*- coding:utf-8 -*-
import mecabCaller
import cpickler


def generate_unigram_model(favs):
    try:
        freqfav = cpickler.frompickle(filename='favs_model_unigram.dump')
    except:
        freqfav = {}

    for favlist in favs:
        for fav in favlist:
            print type(fav.text)
            itemlist = mecabCaller.parse(fav.text)
            for item in itemlist:
                if item in freqfav:
                    freqfav[item] += 1
                else:
                    freqfav[item] = 1
    cpickler.topickle(freqfav, filename='favs_model_unigram.dump')

    return freqfav

__author__ = 'haruka'
