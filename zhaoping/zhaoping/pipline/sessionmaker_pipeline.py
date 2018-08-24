# class DatabaseGenerationPipeline(object):
#     def open_spider(self, spider):
#         DB_Util.init_db()  # 表不存在时候,初始化表结构
#
#     def process_item(self, item, spider):
#         session = DB_Util.get_session()
#         tm_list = []
#         pdt = ZhilianCompany()
#         pdt.job = item['job']
#         pdt.salary = item['salary']
#         pdt.position = item['position']
#         pdt.education = item['education']
#         pdt.operatinghours = item['operatinghours']
#         pdt.company = item['company']
#         tm_list.append(pdt)
#         session.add_all(tm_list)
#         session.commit()
#         session.close()