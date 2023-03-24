from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Bs
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class Tournament:
    def __init__(self, place, province, date, time_control, is_fide, tournament_name, link, ticket_cost=0):
        self.place = place
        self.province = province
        self.date = date
        self.time_control = time_control
        self.is_fide = is_fide
        self.tournament_name = tournament_name
        self.link = link
        self.ticket_cost = ticket_cost

unusual_stations = {"chorzów": "Chorzów miasto", "biskupiec": "Biskupiec Pomorski", "bieruń": "Nowy Bieruń",
                 "czerwionka-leszczyny": "Czerwionka", "gdynia": "Gdynia Główna", "bydgoszcz": "bydgoszcz Główna",
                 "radom": "Radom Główny", "rzeszów": "Rzeszów Główny", "zielona góra": "Zielona Góra Główna",
                 "lublin": "Lublin Główny", "wrocław": "Wrocław Główny", "bielsko-biała": "Bielsko-Biała Główna",
                 "poznań": "Poznań Główny", "wieliczka": "Wieliczka Rynek-Kopalnia", "jaworzno": "Jaworzno Szczakowa",
                 "strzelce krajeńskie": "Strzelce Krajeńskie-wschód", "łowicz": "Łowicz Główny",
                 "szczecin": "Szczecin Główny", "przemyśl":"przemyśl główny",
                 "świdnica": "Świdnica Miasto", "szklarska poręba": "Szklarska Poręba Górna"}
tournaments = []
starting_station = input("What is the name of your starting station? \n")
search_dates = input('Input dates you want to search ("24-03,02.11..."): ').split(",")

driver.get("http://www.chessarbiter.com/")
time.sleep(2)
html = driver.page_source
chess_soup = Bs(html, "html.parser").prettify()
chess_soup = Bs(chess_soup, "html.parser")
tournaments_only_html = chess_soup.find_all("tr", class_=["tbl1", "tbl2"])
    

def get_tournament_info(tr_tag):
    link_and_name = str(tr_tag.find("a")).split('"')
    place_and_type = tr_tag.find_all("div", class_="szary")[1:]

    link = link_and_name[1]
    tournament_name = link_and_name[4].split("\n")[1].strip()
    time_control = str(place_and_type[1]).split("\n")[1].strip()
    place = str(place_and_type[0]).split("\n")[1].strip().split("  ")[0]
    province = str(tr_tag.find("td", {"width": "12%"})).split("\n")[1][-2:]
    date = str(tr_tag.find("td", {"width": "10%"})).split("\n")[1].strip()
    try:
        is_fide = str(place_and_type[1]).split("\n")[3].strip()
    except IndexError:
        is_fide = "bez Fide"
    
    if date in search_dates:
        tournaments.append(Tournament(place, province, date, time_control, is_fide, tournament_name, link))
    else:
        pass
    
for element in tournaments:
    if element.place.lower() in unusual_stations:
        destination = unusual_stations[element.place.lower()]
    else:
        destination = element.place
        
