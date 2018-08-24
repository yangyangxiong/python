import pymysql
class MysqlPipeline(object):
    def process_item(self, item, spider):
        try:
            db = pymysql.connect("localhost", "root", "root", "liepingdatabase", charset='utf8mb4')
            cursor = db.cursor()
            insert_sql = """insert into lieping(job, salary, position, education, operatinghours, company) VALUES (%s, %s, %s, %s, %s, %s)"""
            job=item['job']
            salary=item['salary'][0]
            position=item['position']
            education=item['education']
            operatinghours=item['operatinghours']
            company=item['company']
            cursor.execute(insert_sql, (job, salary, position, education, operatinghours, company))
            db.commit()
        except Exception as e:
            print(e)
        cursor.close()
