from openpyxl import Workbook
class XlsxPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.ws = self.workbook.active
        self.ws.append(['职位', '薪资待遇', '工作地点', '经验要求', '工作时间','公司名称'])  # 设置表头
        #self.file = codecs.open('lagou2.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = [item['job'], item['salary'].decode('utf-8'), item['position'].decode('utf-8'), item['education'].decode('utf-8'), item['operatinghours'].decode('utf-8'), item['company'].decode('utf-8')]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.workbook.save('lagou2.xlsx')  # 保存xlsx文件
        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()