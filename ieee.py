#!
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