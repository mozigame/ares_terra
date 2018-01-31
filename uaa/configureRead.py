# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
import configparser
import os

# local='online'
runType = 'dev'


def getConfig(type, name):
    path = os.getcwd()
    path = path[0:path.find('ares_terra')] + 'ares_terra' + '\\uaa'
    cf = configparser.ConfigParser()
    if 'dev' != runType:
        cf.read(path + "\\conf\\prod\\api.conf")
    else:
        cf.read(path + "\\conf\\dev\\api.conf")
    return cf.get(type, name)
