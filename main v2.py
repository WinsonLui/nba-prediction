#year, month, date, 0, TEAM
#202110190MIL

import pandas as pd
from bs4 import BeautifulSoup
import requests

#READ NBA
years = list(range(2015,2023)) #2019 and 2020 season
url_start = 'https://www.basketball-reference.com/leagues/NBA_{}_games.html'

for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    with open("season_schedule/{}.html".format(year), "w+") as f:
        f.write(data.text)

#Create a list of month names 
month_list = ['october','november','december','january','february','march",'april','may','june']
month_list_2020 = ['october-2019','november','december','january','february','march",'july','august','september','october-2020'] #different starting & ending month for 2019-20 season due to COVID-19
month_list_2021 = ['december','january','february','march','april','may','june','july'] #different starting & ending month for 2020-21 season due to COVID-19

        
starting_date = []
for year in years:
    with open("season_schedule/{}.html".format(year)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    season_schedule_table = soup.find(id="schedule")
    season_schedule2020 = pd.read_html(str(season_schedule_table))[0]
    first_date = season_schedule2020['Date'][0]
    first_date_form = pd.to_datetime(first_date).strftime('%Y%m%d' + '0')
    starting_date.append(first_date_form)

print(starting_date)

ending_date = []


          
