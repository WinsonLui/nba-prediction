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

