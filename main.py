from selenium import webdriver 
import time

PATH = "./chromedriver.exe"
username = input("enter your username:")
driver = webdriver.Chrome(executable_path= PATH)
driver.get("https://instagram.com/"+ username)
time.sleep(4)
driver.close()
