#!/usr/bin/env python
# -*- coding: utf-8 -*
import MeCab 
def parse(sentence):
    itemlist=[]
    bytesentence=sentence
    bytesentence=bytesentence.encode('utf-8')
    m=MeCab.Tagger("-Owakati")
    wakati=m.parse(bytesentence).decode('utf-8')
    wakatistrip=wakati.strip()
    itemlist+=wakatistrip.split(" ")
    #return [x.decode('utf-8') for x in itemlist]
    return itemlist

