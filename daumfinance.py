
# -*- coding:utf-8 -*-
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