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
driver.implicitly_wait(10)
driver.get("https://universityliving.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[text()='Accept']").click()

driver.find_element(By.ID,"newsletter-email").send_keys("test.0@yopmail.com")


driver.find_element(By.XPATH,"//div[text()='Subscribe']").click()

time.sleep(5)
driver.find_element(By.XPATH,"//button[@class='z-[2] p-1.5 absolute rounded-full border leading-none outline focus:outline-none transition-colors -top-2 -right-2 md:-right-3 bg-white border-gray-300 hover:bg-gray-100']").click()

driver.refresh()
time.sleep(5)

driver.quite()
