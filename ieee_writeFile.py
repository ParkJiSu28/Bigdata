
from selenium import webdriver
from bs4 import BeautifulSoup
import time
def readIEEE():
    f=open('result3.txt','w')
    driver = webdriver.PhantomJS()
    for i in range(2):
        print '--- pos ',i,'---'
        ieeeUrl='https://conferences.ieee.org/conferences_events/conferences/search?q=*&date=all&from=2018-01-01&to=2018-12-31https://conferences.ieee.org/conferences_events/conferences/search?q=*&date=all&from=2018-01-01&to=2018-12-31&pos='+str(i)
        driver.get(ieeeUrl)
        time.sleep(3)
        res=driver.find_elements_by_css_selector('div.conference-item')
        for e in res:
            f.write(e.find_element_by_class_name('item-title').text)
            f.write(e.find_element_by_class_name('item-date').text)
            f.write(e.find_element_by_class_name('item-details').text)
            f.write(e.find_element_by_class_name('item-about').text)
            f.write('---------------------------------------------------------------------------------------------')
    f.close()
def main():
    readIEEE()

if __name__=="__main__":
    main()