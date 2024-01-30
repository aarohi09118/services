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
driver.find_element(By.XPATH,"(//p[text()='Pack Light! Explore a range of room essentials for an effortless move-in'])[2]").click()
driver.find_element(By.XPATH,"//select[@id='country']").click()
driver.find_element(By.XPATH,"//option[text()='Ireland']").click()
driver.implicitly_wait(10)
driver.refresh()
driver.find_element(By.XPATH,"//div[text()='Submit']").click()
driver.find_element(By.XPATH,"(//div[text()='View Kit'])[1]").click()
driver.find_element(By.XPATH,"//span[text()='Silver']").click()
driver.find_element(By.XPATH,"//span[text()='Single']").click()
driver.find_element(By.XPATH,"//input[@id='White']").click()
driver.find_element(By.XPATH,"//div[text()='Buy Now']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()

driver.find_element(By.NAME, "otp0").send_keys("1")
driver.find_element(By.NAME, "otp1").send_keys("2")
driver.find_element(By.NAME, "otp2").send_keys("3")
driver.find_element(By.NAME, "otp3").send_keys("4")
driver.find_element(By.NAME, "otp4").send_keys("5")
driver.find_element(By.CSS_SELECTOR, "form button div").click()
driver.find_element(By.XPATH,"//div[text()='Buy Now']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Type Address manually']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Address 1']").send_keys("testing")
driver.find_element(By.XPATH,"//input[@placeholder='Address 2']").send_keys("testing2")
driver.find_element(By.XPATH,"//input[@placeholder='City']").send_keys("Noida")
driver.find_element(By.XPATH,"//input[@placeholder='Postal Code']").send_keys("2300")
driver.find_element(By.XPATH,"//select[@name='country']").click()
driver.find_element(By.XPATH,"//option[text()='Ireland']").click()
driver.find_element(By.XPATH,"//option[text()='Select Province']").click()
driver.find_element(By.XPATH,"//input[@id='arriving']").click()
driver.find_element(By.XPATH,"(//td[text()='29'])[2]").click()
driver.find_element(By.XPATH,"(//button[@type='button'])[3]").click()
driver.find_element(By.XPATH,"(//div[@tabindex='0'])[3]").click()
driver.find_element(By.XPATH,"//td[text()='31']").click()
driver.find_element(By.XPATH,"//div[text()='Continue']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='Continue']").click()
time.sleep(10)
