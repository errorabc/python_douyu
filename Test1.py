import pymysql
#查询入库的数据
def mysqldb():
    db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='testinfo',
                     charset='utf8')
    cursor = db.cursor()
    sql = """select * from renqiinfo"""
    cursor.execute(sql)
    results = cursor.fetchall();

    return results

if __name__=="__main__":
    results=mysqldb()
    for row in results:
        print("id:"+str(row[0]))
        print("name:" + row[1])
        print("renqi:" + row[2])
        print()