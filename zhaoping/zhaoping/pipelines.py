# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from openpyxl import Workbook
class XlsxPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.ws = self.workbook.active
        self.ws.append(['工作地点', '职位名称', '经验要求', '薪资待遇','公司名称'])  # 设置表头
        #self.file = codecs.open('lagou2.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        salary=str(item['salary'][0]).encode('gbk').decode('gbk').encode('utf8')
        position=str(item['position'][0]).encode('gbk').decode('gbk').encode('utf8')
        education=str(item['education']).encode('gbk').decode('gbk').encode('utf8')
        operatinghours=str(item['operatinghours']).encode('gbk').decode('gbk').encode('utf8')
        company=str(item['company'][0]).encode('gbk').decode('gbk').encode('utf8')
        line = []
        line.append(salary)
        line.append(position)
        line.append(education)
        line.append(operatinghours)
        line.append(company)
        self.ws.append(line)
        self.workbook.save('lagou2.xlsx')  # 保存xlsx文件
        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()























