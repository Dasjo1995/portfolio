import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


stock_list = ['kancera', 'apple', 'tesla', 'walmart']

for company in stock_list:
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.investing.com/")

    cookies = driver.find_element(By.ID, value='onetrust-accept-btn-handler')
    cookies.click()

    time.sleep(2)

    search = driver.find_element(by="xpath", value='/html/body/div[5]/header/div[1]/div/div[3]/div[1]/input')
    search.click()
    search.send_keys(f"{company}")
    search.send_keys(Keys.ENTER)

    time.sleep(1)

    stock = driver.find_element(by="xpath", value='//*[@id="fullColumn"]/div/div[2]/div[2]/div[1]/a/span[2]')
    stock.click()

    time.sleep(3)


    chart = driver.find_element(By.XPATH, value="//li[@data-test='Technical']") # IMPORTANT LESSON: use this to find specific values, include the html function first (in this case 'li') and then the function=value!
    chart.click()

    list = []

    rsi = driver.find_elements(by='xpath', value='//*[@id="curr_table"]/tbody/tr[1]/td[2]')
    for element in rsi:
        list.append(element.text)

    print(f"Company: {company}")
    print(f"RSI: {list[1]}")
    print("----------------------------------")

    list.clear()

    driver.close()
