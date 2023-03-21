from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.chessarbiter.com/")
html = driver.page_source
time.sleep(2)
print(html)
with open("html.html", "w",encoding="utf-8") as html_file:
    html_file.write(html)
