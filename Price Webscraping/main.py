import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.inet.se/")

time.sleep(1)

search_term = driver.find_element(by="xpath", value='//*[@id="react-root"]/div[3]/div/button[1]')
search_term.click()

time.sleep(1)

search_term = driver.find_element(by="xpath", value='//*[@id="react-root"]/header/div[2]/div[2]/div/div/div/nav/div[2]/button')
search_term.click()

time.sleep(1)

search_term = driver.find_element(by="xpath", value='//*[@id="react-root"]/header/div[2]/div[2]/div/div/div/nav/div[5]/div/div/div/div[3]/div/a/div[2]')
search_term.click()

section = driver.find_elements(By.CLASS_NAME, value="c1azk1h0")
titles = driver.find_elements(By.CLASS_NAME, value="pb43vjj e15lm9hx")
#boxes = section.find_elements(By.CLASS_NAME, value='p11zknib')
for box in section:
    boxi = box.find_element(By.CLASS_NAME, value="f1ptcakq")
    print('-------------------------')
    title = box.find_element(By.CSS_SELECTOR, value='h3')
    print(title.text)
    price = boxi.find_elements(By.CSS_SELECTOR, value='span')
    for text in price:
        print(text.text)

