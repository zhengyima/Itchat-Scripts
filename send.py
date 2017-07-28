import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from time import ctime
from bs4 import BeautifulSoup
import itchat
def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    page = urllib2.urlopen(site)
    html = page.read();
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")
    city = soup.find(class_='bi_loaction_city')
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})
    quality = soup.select(".bi_aqiarea_right span")
    result = soup.find("div", class_='bi_aqiarea_bottom')
    output=city.text + u'AQI:' + aqi.text + u'\nthe weather quality:' + quality[0].text + result.text
    print(output)
    print('*' * 20 + ctime() + '*' * 20)
    return output
itchat.auto_login(enableCmdQR=2)
Help="""
tips:
Please input a city in pinyin or english!
"""
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def getcity(msg):
    print(msg['Text'])
    cityname=msg['Text']
    result=getPM25(cityname)
    return result

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send('%s'%(getcity(msg)),msg['FromUserName'])
if __name__ == '__main__':
    itchat.run()


