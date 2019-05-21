import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="C:\\Users\\andiac\\Desktop\\chromedriver_win32\\chromedriver.exe", chrome_options=option)

browser.get("https://www.cechovninormy.cz/vyrobky/")

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="execphp-2"]/div/div/div[3]/a/img')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()


products = []
eans = []
manufacturers = []

wait = WebDriverWait(browser, 10)

page_info = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0_info"]')

# Parse every page, except the last one.
for y in page_info:
    while y.text[19:24] != y.text[34:39]:
        next_button = browser.find_element_by_id('DataTables_Table_0_next')

        # (Product Names)
        products_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[3]/a')
        for x in products_element:
            products.append(x.text)

        # (EANS)
        EANS_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[4]')
        for x in EANS_element:
            eans.append(x.text)

        # (Manufacturers)
        manufacturers_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[5]')
        for x in manufacturers_element:
            manufacturers.append(x.text)
        next_button.click()

# Parse the last page.
products_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[3]/a')
for x in products_element:
    products.append(x.text)

EANS_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[4]')
for x in EANS_element:
    eans.append(x.text)

manufacturers_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[5]')
for x in manufacturers_element:
    manufacturers.append(x.text)

# Create the file - date will be included in its name.
file = 'CZ_Cechovninormy_' + time.strftime('%Y%m%d') + '.txt'

# Write the header of the file.
with open(file, 'w', encoding="utf-8") as f:
    f.write('CZ\tCPSHub\tCechovninormy.cz\tPublic\n')

# Write the contents of the file.
with open(file, 'a', encoding="utf-8") as f:
    for product, ean, manufacturer in zip(products, eans, manufacturers):
        if ean:
            f.write(f"{ean}" + '\t' + f"{product}" + ' | ' + f"{manufacturer}" + '\n')

print('File has been written!')
