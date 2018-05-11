# -*- coding:utf-8 -*

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
    
        
    