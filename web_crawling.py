from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="C:/Users/andiac/Desktop/chromedriver_win32", chrome_options=option)

browser.get("https://www.cechovninormy.cz/vyrobky/")

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="execphp-2"]/div/div/div[3]/a/img')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()


# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[3]/a')
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')
