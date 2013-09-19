#!/usr/bin/env python
# -*- coding: utf-8 -*
import mecabCaller
import cpickler


class judger():
    def __init__(self):
        self.freq = cpickler.frompickle('favs_model_unigram.dump')

    def judge(self, text):
        sum = 0
        esc = [u'…', u'・', u'.', u',', u'、', u'。', u'!', u'?', u'！', u'？']
        words = mecabCaller.parse(text)
        for word in words:
            if word in esc:
                pass
            elif word in self.freq:
                sum = self.freq[word]
        print words
        print 'sum=' + str(sum)
        weightedsum = sum / len(words)
        print 'weightedsum=' + str(weightedsum)
        if weightedsum >= 5:
            return True
        else:
            return False

__author__ = 'haruka'
