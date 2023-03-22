from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Bs
import time
PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.chessarbiter.com/")
html = driver.page_source
time.sleep(2)
print(html)
with open("html.html", "w",encoding="utf-8") as html_file:
    html_file.write(html)
    

def get_tournament_info(html):
    soup = Bs(html, "html.parser")
    tr_list = soup.find("tr")
    link_and_name = str(tr_list.find("a")).split('"')
    place_and_type = tr_list.find_all("div", class_="szary")[1:]

    link = link_and_name[1]
    tournament_name = link_and_name[4].split("\n")[1].strip()
    time_control = str(place_and_type[1]).split("\n")[1].strip()
    place = str(place_and_type[0]).split("\n")[1].strip().split("  ")[0]
    province = str(tr_list.find("td", {"width": "12%"})).split("\n")[1][-2:]
    date = str(tr_list.find("td", {"width": "10%"})).split("\n")[1].strip()
    try:
        is_fide = str(place_and_type[1]).split("\n")[3].strip()
    except:
        is_fide = "bez Fide"
