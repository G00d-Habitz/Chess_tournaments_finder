from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Bs
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

unusual_stations = {"chorzów": "Chorzów miasto", "biskupiec": "Biskupiec Pomorski", "bieruń": "Nowy Bieruń",
                 "czerwionka-leszczyny": "Czerwionka", "gdynia": "Gdynia Główna", "bydgoszcz": "bydgoszcz Główna",
                 "radom": "Radom Główny", "rzeszów": "Rzeszów Główny", "zielona góra": "Zielona Góra Główna",
                 "lublin": "Lublin Główny", "wrocław": "Wrocław Główny", "bielsko-biała": "Bielsko-Biała Główna",
                 "poznań": "Poznań Główny", "wieliczka": "Wieliczka Rynek-Kopalnia", "jaworzno": "Jaworzno Szczakowa",
                 "strzelce krajeńskie": "Strzelce Krajeńskie-wschód", "łowicz": "Łowicz Główny",
                 "szczecin": "Szczecin Główny", "przemyśl":"przemyśl główny",
                 "świdnica": "Świdnica Miasto", "szklarska poręba": "Szklarska Poręba Górna"}

driver.get("http://www.chessarbiter.com/")
time.sleep(2)
html = driver.page_source
chess_soup = Bs(html, "html.parser").prettify()
tournaments_only_html = chess_soup.find_all("tr", class_=["tbl1", "tbl2"])
    

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
    except IndexError:
        is_fide = "bez Fide"
        
    turnieje.append(Turniej(place, province, date, time_control, is_fide, tournament_name, link))
