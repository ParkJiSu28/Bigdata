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
