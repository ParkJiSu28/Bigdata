# -*- coding:utf-8 -*-
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
