Crawling
========

BigData를 공부하면서 BigData의 기본조건인 Crawling를 공부하게 되었고 git에 upload하는 목적은 상업용이 아닌 학습용으로 올리게 되었습니다. 웹상에 데이터를 가져와 데이터를 분석하여 더 나은 데이터로 활용할 수 있고 그 데이터를 활용해서 또 다른 무언가를 생산할 수 있다는게 BigData의 매력이지 않을까 싶습니다. Crawling을 연습하기 위해 원래는 Crawling이 허락되지 않는 사이트들도 있지만 학업용은 괜찮다고 합니다. Crawling을 배우고 싶은 학생들이나 모든 사람들에게 참고가 되었으며 합니다. 처음 파싱이라는것이 무엇인지 어떻게 데이터가 파싱되고 저장되어 어떤 형식으로 가져오는 것인지에 대한 공부를 먼저 진행하였고 다음에 <bold>BeautifulSoup을 연습하고 그 다음 BeautifulSoup으로 하기 힘든 동적인페이지를 Crawling하기 위해 <bold>Selenium 을 연습하고 드라이버로는 <bold>PhantomJS를 많이 사용한것 같습니다. 밑의 예제들은 소스코드로도 올려 놓았고 참고 하시면 될것같습니다. 추후 Spark를 사용해 좀더 정밀한 데이터분석을 연습해보려고 합니다.

네이버 뮤직 크롤링
------------------

---

```
# -*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs

def music():
    driver = webdriver.Chrome()
    naver_music ='http://music.naver.com/search/search.nhn?query={}&target=track&page{}'
    for page in range(1,6):
        driver.get(naver_music.format('비오는',page))
    html =driver.page_source
    soup = bs(html,'html5lib')
    table= soup.select_one('#content > div.section > div._tracklist_mytrack.tracklist_table._searchTrack > table > tbody')
    tr_list=table.find_all('tr')
    for tr in tr_list[1:]:
        td=tr.find_all('td')
        print u' {}--{}--{}'.format(
        td[2].span.text,
        td[3].text.strip(),
        td[4].text.strip()
        )
def main():
    music()


if __name__ == "__main__":
    main()
```

네이버 뮤직페이지를 크롤링하였다. ''비오는''이라는 단어를 쿼리로보내 검색하고 페이지를 넘겨가며 음악의 제목과 가수 앨범이름을 페이지로별로 묶어서 터미널 환경에서 프린트 하였다.

---

기상청날씨 크롤링
=================

```

\-*- coding:utf-8 -*\-
======================

from selenium import webdriver
from bs4 import BeautifulSoup as bs

def weather():
    driver = webdriver.Chrome()
    driver.get('http://www.weather.go.kr/weather/main.jsp')
    html = driver.page_source
    soup = bs(html, 'html5lib')
    weather_list =soup.find_all( 'table', class_='forecastNew5')
    print('시간 기온 ')
for data in weather_list[1:]:
    print '{} - {}'.format(
    data.find('td', class_='time').text.strip() ,
    data.find('td', class_='degree').text
    )

def main():
    weather()


if __name__ == "__main__":
    main()


```

기상청에서 시간과 기온을 크롤링하여 시간과 기온으로 프린트하였고 셀레니움과 웹드라이버 그리고 BeautifulSoup을 사용함.

---

ieee 크롤링하기 selenium
========================

```

from selenium import webdriver
from bs4 import BeautifulSoup

def readIEEE():
    driver = webdriver.PhantomJS()
    for i in range(5):
        print '--- pos ',i,'---'
        ieeeUrl='https://conferences.ieee.org/conferences_events/conferences/search?q=*&date=all&from=2018-01-01&to=2018-12-31&region=all&country=all&pos='+str(i)
        driver.get(ieeeUrl)
        driver.implicitly_wait(10)
        res=driver.find_elements_by_css_selector('div.conference-item')
        for e in res:
            print e.find_element_by_class_name('item-title').text
            print e.find_element_by_class_name('item-date').text
            print e.find_element_by_class_name('item-details').text
            print e.find_element_by_class_name('item-about').text

def main():
    readIEEE()

if __name__=="__main__":
    main()
```

ieee 학술 페이지에서 최근 컨퍼런스를 목차별로 페이지별로 긁어와서 title,datail과같은 항목으로 나누어서 프린트 하였다.

---

다음댓글 크롤링하기
===================

```

from selenium import webdriver
from bs4 import BeautifulSoup as bs

def daum() :
    f=open('댓글.txt' ,  'w')
    driver = webdriver.PhantomJS()
    driver.get('http://v.media.daum.net/v/20170926225302536')
    html =driver.page_source
    for i in range(0,5):
        f.write("i")
        more=driver.find_element_by_css_selector("a[href='#more']")
        more.click()
        res =driver.find_elements_by_class_name('cmt_info')
        for x in res:
            f.write(x.find_element_by_css_selector('strong').text.encode('utf-8'))   
            f.write(x.find_element_by_css_selector('p').text.encode('utf-8'))
    f.close()


def main():
    daum()


if __name__=="__main__":
    main()

```

다음에서 댓글들을 크롤링하였다.크롤링한 정보들을 파일에 적고 파일을 생성하였다.

---

다음환율크롤링
==============

```
from selenium import webdriver
from bs4 import BeautifulSoup as bs

def exchange():
    driver = webdriver.Chrome()
    driver.get('http://finance.daum.net/exchange/exchangeMain.daum')
    html = driver.page_source
    soup = bs(html, 'html5lib')
    table=soup.select('#exchangeTbody')
    for tr in table:
        for data in tr.find_all('td',class_='trData'):
            print data.text

def main():
    exchange()


if __name__ == "__main__":
    main()

```

다음환율페이지에서 환율 전체를 크롤링하였다. 실시간으로 변하는 데이터라 파일에 담지 않고 필요할때 정보를 얻을 수 있게 작성하였다.동적 페이지라 처음에 에로사항이 많았지만 셀레니움을 활용하여 크롤링을 하였다.

---

네이버실시간검색어
==================

```
from bs4 import BeautifulSoup as bs from selenium import webdriver

def main():
driver = webdriver.PhantomJS()
driver.get('https://www.naver.com')
 html = driver.page_source
 soup=bs(html,'lxml')
 naver=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base')
  for x in naver:
    for y in x.find_all('ul'):
      for k in y.find_all('li'):
        print k.text.strip()

```

함수로 구현하지않고 간단하게 셀레니움을 사용하여 작성하였다.

---

선수 기록
=========

```

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time driver = webdriver.PhantomJS() kbl='https://www.koreabaseball.com/Record/Main.aspx'
driver.get(kbl)
list_=driver.find_elements_by_class_name('player_top5')
for x in list_:
  print x.text

```

koreabaseball 페이지에서 메인 선수들중 TOP5안에드는 선수들을 간단하게 뽑아보았다.

---

야구 기사
=========

```

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time driver = webdriver.PhantomJS() kbl='https://www.koreabaseball.com/News/Preview/List.aspx'
driver.get(kbl)
list*=driver.find_elements_by_class_name('boardPhoto')
for x in list*:
  print x.text

```

위와 마찬가지로 기사의 내용을 크롤링해보았다.

---

pycon 검색해서 들어가서 크롤링하기
==================================

```

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time driver = webdriver.PhantomJS() driver.get("http://www.python.org")
asd=driver.find_element_by_name('q')
asd.send_keys('pycon')
 asd.send_keys(Keys.RETURN) sdsd=driver.find_elements_by_class_name('list-recent-events')
 for x in sdsd:
  print x.text

```

python홈페이지에 검색란에 Key함수를 사용해 검색하고 들어가 검색한 내용들을 크롤링해보았다. 어떻게 검색하고 쿼리를 보내는지 다시 한번 더 공부 할 수 있었다.

---

네이버 영화 순위
================

```

def movie():
    f=open('movie.txt' ,  'w')
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    driver = webdriver.PhantomJS()
    driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    das=driver.find_elements_by_class_name('tit3')
    count=1
    for x in das:
        f.write('{}-{}\n'.format(
            count,
            x.text.encode('utf-8)')
        ))
        count=count+1
    f.close()

def main():
    movie()

if __name__=='__main__':
    main()
```

네이버 영화 페이지에서 영화순위를 크롤링하였고 그 내용을 파일로 작성해 보았다.
