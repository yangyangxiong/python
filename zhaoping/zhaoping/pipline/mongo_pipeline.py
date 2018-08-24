import pymongo
from zhaoping import settings
class PymongoPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        tablename = settings["MONGODB_DOCNAME"]
        client = pymongo.MongoClient(host=host, port=port)
        jdstore = client[dbname]
        self.goods_list = jdstore[tablename]

    def process_item(self, item, spider):
        goodsinfos = dict(item)
        self.goods_list.insert(goodsinfos)
        return item