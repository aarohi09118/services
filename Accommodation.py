from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = "/Users/apple/Desktop/cd"

opt = Options()
# driver = webdriver.Chrome(service=s, options=opt)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(opt)
driver.get("https://universityliving.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@class='text-sm lg:text-xs bg-theme-blue w-5 h-5 px-1 rounded-full text-white btn-cookie fixed bottom-8 -right-1 md:bottom-4 mr-2 md:mr-0']").click()
driver.find_element(By.XPATH,"//a[text()='Services']").click()
driver.find_element(By.XPATH,"//div[text()='Explore All Services']").click()
driver.find_element(By.XPATH,"(//p[text()='Find the perfect home, close to university and close to life'])[2]").click()
time.sleep(5)
driver.refresh()

driver.find_element(By.XPATH,"//input[@placeholder='University (eg. London University)']").click()
driver.find_element(By.XPATH,"//p[text()='Birmingham']").click()
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("testing")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("test")
driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("pravin.garg@universityliving.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='contactNumber']").send_keys("9012546723")
driver.find_element(By.XPATH,"//span[text()='300 - 400']").click()
driver.find_element(By.XPATH,"//div[text()='Explore Properties']").click()
time.sleep(10)
driver.back()
time.sleep(5)

