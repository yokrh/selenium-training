# coding: UTF-8
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup as Soup

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()

players = [] 

# me
#print "me begin"
my_profile_url = "https://p.eagate.573.jp/game/sdvx/iv/p/playdata/profile/index.html"
driver.get(my_profile_url)
driver.add_cookie({'name': 'M573SSID','value': '66ca45fb-2890-4b41-a9ba-dac1c6c054b2', 'domain': 'p.eagate.573.jp'})
driver.get(my_profile_url)
soup = Soup(driver.page_source, "html5lib")

name = soup.select('#name_str')[0].string
volforce = soup.select('#force_point')[0].string
me = { "name": name, "volforce": volforce }
players.append(me)
#print "me end"


# rival
#print "rival begin"
rival_list_page_url = "https://p.eagate.573.jp/game/sdvx/iv/p/playdata/rival/index.html"
driver.get(rival_list_page_url)
soup = Soup(driver.page_source, "html5lib")

rival_profile_a_tags = soup.select('#list_col_01 a')
for a in rival_profile_a_tags:
  rival_profile_url = "https://p.eagate.573.jp" + a.get("href")
  driver.get(rival_profile_url)
  soup = Soup(driver.page_source, "html5lib")
  
  name = a.string
  volforce = "????"
  if soup.select('#force_point'):
    volforce = soup.select('#force_point')[0].string

  player = { "name": name, "volforce": volforce }
  players.append(player)
  #print name + " done"
#print "rival end"

# sort
players.sort(key=lambda x: x["volforce"], reverse=True)


driver.quit()
display.stop()

