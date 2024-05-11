import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.skysports.com/premier-league-table'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

t_body = soup.find('tbody')
data = []
headers=['Team', 'Played', 'Points']

for row in t_body.find_all('tr')[1:]:
    team = row.find('td', class_="standing-table__cell standing-table__cell--name").text.strip()
    played = row.find_all('td')[2].text.strip()
    points = row.find_all('td')[9].text.strip()
    data.append({'Team': team, 'Played': played, 'Points': points})

# Convert list of dictionaries into DataFrame with headers
df = pd.DataFrame(data, columns=headers)

# Save DataFrame to CSV file
print(df)
# df.to_csv('premier_league_table.csv', index=False)

# print("Data saved to 'premier_league_table.csv'")
