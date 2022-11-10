from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging

def test_goodle():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.maximize_window()
  driver.implicitly_wait(5)
  driver.get('https://www.google.com/')
  assert driver.title == "Google"
  driver.quit()

def test_facebook():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.maximize_window()
  driver.implicitly_wait(5)
  driver.get('https://www.facebook.com/')
  assert driver.title == "Facebook – log in or sign up"
  driver.quit()

def test_instagram():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.maximize_window()
  driver.implicitly_wait(5)
  driver.get('https://www.Instagram.com/')
  assert driver.title == "Instagram"
  driver.quit()

def test_gmail():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.maximize_window()
  driver.implicitly_wait(5)
  driver.get('https://www.gmail.com/')
  assert driver.title == "Gmail"
  driver.quit()

def test_rediff():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.maximize_window()
  driver.implicitly_wait(5)
  driver.get('https://www.rediff.com/')
  assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
  driver.quit()