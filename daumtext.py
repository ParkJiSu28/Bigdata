
# -*- coding:utf-8 -*-
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