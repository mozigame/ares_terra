# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
import configparser
import codecs 
#local='online'
runType='dev'

def getConfig(type,name):
    cf = configparser.ConfigParser()
    if('dev'!=runType):
        cf.read("conf/prod/api.conf")
    else:
        cf.read("conf/dev/api.conf")
    return cf.get(type, name)



