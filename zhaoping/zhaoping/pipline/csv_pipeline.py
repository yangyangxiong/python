import csv
class CSVPipeline(object):

    def __init__(self):
        self.csvf = open('data.csv', 'a+', encoding='gbk', newline='')
        self.writer = csv.writer(self.csvf)
        self.writer.writerow(('nickname', 'description', 'followed', 'fpllowing', 'articles', 'charlength', 'likes'))
        self.csvf.close()

    def process_item(self, item, spider):
        with open('data.csv', 'a+', encoding='gbk', newline='') as f:
            writer = csv.writer(f)
            writer.writerow((item['nickname'], item['description'], item['followed'], item['following'],
                             item['articles'], item['charlength'], item['likes']))
        return item