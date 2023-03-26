from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as Bs
import time


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
    
    if date in search_dates and time_control in search_time_control:
            tournaments.append(Tournament(place, province, date, time_control, is_fide, tournament_name, link))
        
        
def get_ticket_prices(start, destiny, date):
    for tournament in tournaments:
        if destiny.lower() == tournament.place.lower() and date == tournament.date and tournament.ticket_cost != 0:
            element.ticket_cost = tournament.ticket_cost
            return None
        elif destiny.lower() in unusual_stations.values():
            if destiny.lower() == unusual_stations.get(tournament.place.lower(), False) and date == tournament.date and tournament.ticket_cost != 0:
                element.ticket_cost = tournament.ticket_cost
                return None

    driver.get(f"https://koleo.pl/rozklad-pkp/{start}/{destiny}/{date}-2023_04:00/all/all")
    time.sleep(3)
    trains_html = driver.page_source
    soup = Bs(trains_html, "html.parser")
    price_list = soup.find_all("span", class_="price-parts")
    naked_prices = [e.contents[0].strip().replace(",", ".") for e in price_list]
    nakeder_prices = [float(e) if e[-2:] != "zł" else float(e[0:-3]) for e in naked_prices]
    lowest_price = float(sorted(nakeder_prices)[0]) if len(nakeder_prices) > 0 else 9999
    element.ticket_cost = round(lowest_price * discount, 2)
    

unusual_stations = {"chorzów": "Chorzów miasto", "biskupiec": "biskupiec pomorski", "bieruń": "nowy bieruń",
                    "czerwionka-leszczyny": "czerwionka", "gdynia": "gdynia główna", "bydgoszcz": "bydgoszcz główna",
                    "radom": "radom główny", "rzeszów": "rzeszów główny", "zielona góra": "zielona góra główna",
                    "lublin": "lublin główny", "wrocław": "wrocław główny", "bielsko-biała": "bielsko-biała główna",
                    "poznań": "poznań główny", "wieliczka": "wieliczka rynek-kopalnia",
                    "jaworzno": "jaworzno szczakowa", "opole": "opole główne",
                    "strzelce krajeńskie": "strzelce krajeńskie-wschód", "łowicz": "łowicz główny",
                    "szczecin": "szczecin główny", "przemyśl": "przemyśl główny",
                    "świdnica": "świdnica miasto", "szklarska poręba": "szklarska poręba górna"}
tournaments = []
starting_station = input("Jaka jest Twoja stacja początkowa? \n")
search_dates = input('Wypisz daty w jakich możesz grać w turniejach ("24-03,02.11..."):\n').split(",")
search_time_control = input('Wypisz jakie szachy Cię interesują ("klasyczne,szybkie",blitz"):\n').split(",")
discount = 1 - float(input('Ile % wynosi twoja zniżka? (po prostu np. "0", "51"):\n')) / 100


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.chessarbiter.com/")
time.sleep(2)
html = driver.page_source
chess_soup = Bs(html, "html.parser").prettify()
chess_soup = Bs(chess_soup, "html.parser")
tournaments_only_html = chess_soup.find_all("tr", class_=["tbl1", "tbl2"])
    
    
if starting_station.lower() in unusual_stations:
    starting_station = unusual_stations[starting_station.lower()]
    
for element in tournaments_only_html:
    get_tournament_info(element)
    
for element in tournaments:
    if element.place.lower() in unusual_stations:
        destination = unusual_stations[element.place.lower()]
    else:
        destination = element.place
    
    if starting_station.lower() == destination.lower():
        element.ticket_cost = 0
    else:
        get_ticket_prices(starting_station, destination, element.date)
    
tournaments.sort(key=lambda x: x.ticket_cost)

for i, t in enumerate(tournaments):
    print(i, t.ticket_cost, t.date, t.place, t.province, t.time_control, t.is_fide, t.tournament_name, t.link)
