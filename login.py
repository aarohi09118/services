# Login
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

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[@class='content-font']").click()

driver.find_element(By.ID,"email").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()

driver.find_element(By.NAME, "otp0").send_keys("1")
driver.find_element(By.NAME, "otp1").send_keys("2")
driver.find_element(By.NAME, "otp2").send_keys("3")
driver.find_element(By.NAME, "otp3").send_keys("4")
driver.find_element(By.NAME, "otp4").send_keys("5")

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "form button div").click()

time.sleep(10)

# driver.find_element(By.CSS_SELECTOR, 'div[class="hidden items-center justify-end lg:flex ml-4"] button').click()
