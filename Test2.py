import Test3
import urllib.request
from  bs4 import BeautifulSoup
import json
    # 添加头部，伪装浏览器
def Reptilian(url):
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
    for i in range(0,120):
       Test3.mysqldb(links1[i].get_text(),links2[i].get_text())

if __name__=="__main__":
    url = "https://www.douyu.com/directory/game/LOL"
    Reptilian(url)