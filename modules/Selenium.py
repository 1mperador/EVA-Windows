from time import sleep 
import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()
driver.get('chrome://newtab')
sleep(1)

#  Deu certo ?

entrar_site = driver.find_element(By.XPATH, "//ytd-thumbnail-overlay-now-playing-renderer[@class='style-scope ytd-thumbnail']")
entrar_site.click()






