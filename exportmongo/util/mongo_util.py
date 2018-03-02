from pymongo import MongoClient

from exportmongo.util.config import *


class MongoUtil():
    def __init__(self):
        self.pathConfig = PathConfig()
        if not self.pathConfig:
            raise Exception("--> no path Config")
        self.mongoClient = MongoClient(self.pathConfig.cluster_host)

    def get_conn(self):
        return self.mongoClient[self.pathConfig.database]
