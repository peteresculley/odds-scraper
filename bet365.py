from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

def scrape():
   site = 'https://mobile.bet365.com/?apptype=&appversion=&cb=1529503663#type=Coupon;key=1-172-1-26326924-2-0-0-0-2-0-0-0-0-0-1-0-0-0-0-0-0;ip=0;lng=1;anim=1'
   results = []

   driver = webdriver.Firefox()
   try:
      driver.get(site)

      sleep(4)

      outright_items = driver.find_elements_by_css_selector("div.podEventRow.singleRow > div > span.opp")
      
      for item in outright_items:
         outright = BeautifulSoup(item.get_attribute('innerHTML'), 'html.parser')
         outright_str = str(outright)
         country = outright_str[0:outright_str.find('<')].strip()
         odds = outright.span.string
         results.append((country, odds))
   except Exception as e:
      print('Error: bet365: ', e)

   sleep(1)
   driver.quit()

   return results
