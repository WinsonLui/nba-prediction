#year, month, date, 0, TEAM
#202110190MIL

import pandas as pd
from bs4 import BeautifulSoup
import requests

#READ NBA
years = list(range(2015,2023)) #2019 and 2020 season

#Create a list of month names 
months = ['october','november','december','january','february','march",'april','may','june']
months_2020 = ['october-2019','november','december','january','february','march",'july','august','september','october-2020'] #different starting & ending month for 2019-20 season due to COVID-19
months_2021 = ['december','january','february','march','april','may','june','july'] #different starting & ending month for 2020-21 season due to COVID-19

url_start = 'https://www.basketball-reference.com/leagues/{}.html'

for year in years:
    if year = 2020: 
        for month in months_2020:
            fill = 'NBA_' + year + '_games-' + month          
            url = url_start.format(fill)
            data = requests.get(url)
            name = year + ' (' + month + ')'
            with open("season_schedule/{}.html".format(name), "w+") as f:
                f.write(data.text)
    elif year = 2021: 
        for month in months_2021:
            fill = 'NBA_' + year + '_games-' + month          
            url = url_start.format(fill)
            data = requests.get(url)
            name = year + ' (' + month + ')'
            with open("season_schedule/{}.html".format(name), "w+") as f:
                f.write(data.text)   
    else:
        for month in months:
            fill = 'NBA_' + year + '_games-' + month          
            url = url_start.format(fill)
            data = requests.get(url)
            name = year + ' (' + month + ')'
            with open("season_schedule/{}.html".format(name), "w+") as f:
                f.write(data.text)
        
             
starting_date = []
ending_date = []
               
for year in years:
    if year = 2020:
        start_month = months_2020[0]
        end_month = months_2020[-1]
    elif year = 2021:
        start_month = months_2021[0]
        end_month = months_2021[-1]
    else:
        start_month = months[0]
        end_month = months[-1]
    start_name = year + ' (' + start_month + ')'
    end_name = year + ' (' + end_month + ')'   
    with open("season_schedule/{}.html".format(start_name)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    season_schedule_table = soup.find(id="schedule")
    season_schedule = pd.read_html(str(season_schedule_table))[0]
    first_date = season_schedule['Date'][0]
    first_date_form = pd.to_datetime(first_date)
    starting_date.append(first_date_form)          
    with open("season_schedule/{}.html".format(end_name)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    season_schedule_table = soup.find(id="schedule")
    season_schedule = pd.read_html(str(season_schedule_table))[0]
    last_date = season_schedule['Date'][-1]
    last_date_form = pd.to_datetime(last_date)
    ending_date.append(last_date_form) 
               
print(starting_date)
print(ending_date)


