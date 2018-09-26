import pymysql
#插入数据到数据库
def mysqldb(name,renqi):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='root',
                         db='testinfo',
                         charset='utf8')
    cursor = db.cursor()
    name1="'"+name+"'"
    renqi1="'"+renqi+"'"
    sql="INSERT into renqiinfo(id,name,renqi) VALUES(1,%s,%s)"%(name1,renqi1)
    print(sql)
    cursor.execute(sql)
    db.commit()
