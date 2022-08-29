#year, month, date, 0, TEAM
#202110190MIL
import pandas as pd
from bs4 import BeautifulSoup
import requests



#Set the study period
years = list(range(2015,2023)) #2015 and 2023 season

#Create a url template
url_start = 'https://www.basketball-reference.com/leagues/NBA_{}_games.html'

#Retrieve html files from web
for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    with open("season_schedule/{}.html".format(year), "w+") as f:
        f.write(data.text)

#Create a list of month names 
months = ['october','november','december','january','february','march','april','may','june']
months_2020 = ['october-2019','november','december','january','february','march','july','august','september','october-2020'] #different starting & ending month for 2019-20 season due to COVID-19
months_2021 = ['december','january','february','march','april','may','june','july'] #different starting & ending month for 2020-21 season due to COVID-19

url_start = 'https://www.basketball-reference.com/leagues/{}.html'

#Save each season & month's webpage
for year in years:
    if year == 2020: 
        months_temp = months_2020
    elif year == 2021:
        months_temp = months_2021
    else:
        months_temp = months
    for month in months_temp:
        fill = 'NBA_' + year + '_games-' + month          
        url = url_start.format(fill)
        data = requests.get(url)
        name = year + ' (' + month + ')'
        with open("season_schedule/{}.html".format(name), "w+") as f:
            f.write(data.text)                

#Create an empty list for starting_date and ending_date
starting_date = []
ending_date = []

for year in years:
    if year == 2020:
        start_month = months_2020[0]
        end_month = months_2020[-1]
    elif year == 2021:
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
    season_schedule2020 = pd.read_html(str(season_schedule_table))[0]
    first_date = season_schedule2020['Date'][0]
    first_date_form = pd.to_datetime(first_date).strftime('%Y%m%d' + '0')
    starting_date.append(first_date_form)
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
               
               
 




               
game_schedule = pd.DataFrame(, columns = ['Season','Date','Home'])
               
for year in years:
    if year == 2020:
        months_temp = months_2020
    elif year == 2021:
        months_temp = months_2021
    else:
        months_temp = months
    for month in months_temp:
        name = year + ' (' + months1 + ')'
        with open("season_schedule/{}.html".format(name)) as f:
            page = f.read()
        soup = BeautifulSoup(page, "html.parser")
        season_schedule_table = soup.find(id="schedule")
        season_schedule = pd.read_html(str(season_schedule_table))[0]
        date = season_schedule['Date']
        home = season_schedule['Home/Neutral']
        date_formatted = pd.to_datetime(date)
        
               
               game_schedule_temp = pd.DataFrame({'Season':year,
                                          }
                                          
                                          
                                          
        game_schedule.append(first_date_form)          
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


