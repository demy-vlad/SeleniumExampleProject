import time
from re import T
from loguru import logger
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib3.packages.six import u


BANDCAMP_FRONTPAGE='https://hotline.ua/'

class Hotline(unittest.TestCase):
   def setUp(self):
      options = Options()
      # options.holdBrowserOpen = True;
      options.headless = False # Using a headless browser version
      self.driver = webdriver.Chrome(chrome_options=options)
      self.driver.get(BANDCAMP_FRONTPAGE)

   def test_1_response_status_code(self):
      '''
      Success status response code 200"
      '''
      headers = {
        "accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
      }
      url = "https://hotline.ua/"
      response = requests.get(url, headers=headers)
      if response.status_code !=200:
         logger.error(f"{response} - {url}")
      else:
         logger.info(f"{response} - {url}")

   def test_2_language_change_ua(self):
      '''
      The language change to Ukraine"
      '''
      self.driver.find_element_by_xpath("//header/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[2]").click()
      assert self.driver.title == "Hotline - порівняти ціни в інтернет-магазинах України"

   def test_3_language_change_ru(self):
      '''
      The language change to Russian"
      '''
      self.driver.find_element_by_xpath("//header/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]").click()
      assert self.driver.title == "Hotline - сравнить цены в интернет-магазинах Украины"

   def test_4_lowest_price(self):
      '''
      The lowest price should be in the store "Robby"
      '''
      t = 2
      # searchbox
      elem = self.driver.find_element_by_xpath("//input[@id='searchbox']")
      elem.send_keys("Xiaomi Mi Electric Scooter 1s Black")
      time.sleep(t)      
      # doSearch
      self.driver.find_element_by_xpath("//input[@id='doSearch']").click()
      time.sleep(t)     
      # from the minimum price
      self.driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[1]/div[3]/div[4]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/span[1]").click()
      time.sleep(t)
      # price
      price = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]/a[1]")
      # shop
      shop = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/a[1]")
      time.sleep(t)
      logger.info(f"{shop.text}: {price.text}")
      assert shop.text == "Robby"

   def tearDown(self):
      self.driver.close()
      # pass

if __name__ == "__main__":
   unittest.main()