import pymysql
class MysqlPipeline(object):
    def process_item(self, item, spider):
        try:
            db = pymysql.connect("localhost", "root", "root", "liepingdatabase", charset='utf8mb4')
            cursor = db.cursor()
            insert_sql = """insert into lieping(salary, position, education, operatinghours, company) VALUES (%s, %s, %s, %s, %s)"""
            salary=item['salary'][0]
            position=item['position'][0]
            education=item['education']
            operatinghours=item['operatinghours']
            company=item['company'][0]
            cursor.execute(insert_sql, (salary, position, education, operatinghours, company))
            db.commit()
        except Exception as e:
            print(e)
        cursor.close()
