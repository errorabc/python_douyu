# python_douyu
python爬取斗鱼主播等信息
**<font size="32" >python 3爬取斗鱼某些版块的主播人气</font>**

**<font size="5" >1.爬虫版块</font>**

    import Test3
    import urllib.request
    from  bs4 import BeautifulSoup
    import json
    
    def Reptilian(url):
    #添加头部,伪装浏览器
      headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}

      resquest = urllib.request.Request(url=url, headers=headers)
      response = urllib.request.urlopen(resquest)
 
      if response.code == 200:
        print("服务器连接成功")
      #读取数据
      data = response.read()

      html = data.decode('utf-8')
      #解析器
      soup = BeautifulSoup(
        html,
        'html.parser',
        from_encoding='utf-8'
       )

      links1 = soup.find_all('span', class_="dy-name ellipsis fl")  #主播的名字
      links2 = soup.find_all('span', class_="dy-num fr")  # 主播的人气

      #数据插入到数据库
      for i in range(0,120):#暂时只爬取了第一个,一页有120条数据
        Test3.mysqldb(links1[i].get_text(),links2[i].get_text())

      if __name__=="__main__":
       url = "https://www.douyu.com/directory/game/LOL"#爬取地址,这里爬取的是斗鱼DNF版块的
       Reptilian(url)

**<font size="5" >2.插入数据库版块</font>**

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
运行代码截图如下
<img src="/charu.png">

**<font size="5" >3.查询数据库版块</font>**

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
运行代码截图如下
<img src="/chaxun.png">


**<font size="5" >3.总结</font>**
       
       后续还会添加新的功能:
       1.例如分页爬取,把版块所有的主播信息都爬取下来.
       2.代理爬虫,绕开网站的反爬虫
	   3.多线程,同时爬取多个网站
       4.定时爬虫,间隔多长时间爬取网站
       5.我的Github地址	
