from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

def scrape():
   site = 'https://www.paddypower.com/football/2018-fifa-world-cup?tab=outrights'
   results = []

   driver = webdriver.Firefox()
   try:
      driver.get(site)

      sleep(3)

      show_more = driver.find_elements_by_xpath("//*[contains(text(), 'Show More')]")
      if len(show_more) > 0:
         show_more[0].click()
      sleep(0.3)

      outright_items = driver.find_elements_by_xpath("//outright-item")
      
      for item in outright_items:
         outright = BeautifulSoup(item.get_attribute('innerHTML'), 'html.parser').div
         country = outright.div.p.string
         odds = outright.find_all('div', recursive=False)[1].find('btn-odds').button.text.strip()
         results.append((country, odds))
   except Exception as e:
      print('Error: Paddypower: ', e)

   sleep(1)
   driver.quit()

   return results
