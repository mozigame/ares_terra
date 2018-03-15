# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
import configparser
import os

# local='online'
runType = 'prod'

configObj = None


def initConfig():
    path = os.getcwd()
    path = path[0:path.find('ares_terra')] + 'ares_terra%suaa' % os.sep
    cf = configparser.ConfigParser()
    if 'dev' != runType:
        cf.read(path + format("{}conf{}prod{}api.conf").format(os.sep, os.sep, os.sep))
    else:
        cf.read(path + format("{}conf{}dev{}api.conf").format(os.sep, os.sep, os.sep))
    return cf


def getConfig(type, name):
    configObj = initConfig()
    if type and name:
        return configObj.get(type, name)
