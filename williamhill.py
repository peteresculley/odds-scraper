from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

def scrape():
   site = 'http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html'
   results = []

   driver = webdriver.Firefox()
   try:
      driver.get(site)

      sleep(4)

      outright_items = driver.find_elements_by_css_selector("table.tableData > tbody > tr > td > div")
      
      for item in outright_items:
         outright = BeautifulSoup(item.get_attribute('innerHTML'), 'html.parser')
         elements = outright.find_all('div', recursive=False)
         country = elements[1].string.strip()
         odds = elements[0].string.strip()
         results.append((country, odds))
   except Exception as e:
      print('Error: William Hill: ', e)

   sleep(1)
   driver.quit()

   return results
