#!env python3
# -*- coding: utf-8 -*-

#from: https://www.dataquest.io/blog/web-scraping-tutorial-python/
import requests

print('The requests library')
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print('Response status')
print(page.status_code)
print('')

print('Is that ok?')
print(page.ok)
print('')

print('Core content')
print(page.content)
print('')

print('Main goal: Extract the content of <p>')
print('Parsing a page with BeautifulSoup')
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print('')

print(list(soup.children))
print('')

print([type(item) for item in list(soup.children)])
print('')

html = list(soup.children)[2]
print(list(html.children))
print('')

body = list(html.children)[3]
print(list(body.children))
print('')

p = list(body.children)[1]
print(p.get_text())
print('')

print('Finding all instances of a tag at once')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))
print('')

print(soup.find_all('p')[0].get_text())
print('')

print([tag.get_text() for tag in soup.find_all('p')])
print('')

print(soup.find('p'))
print('')

print('Searching for tags by class and id')
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
print('')

print('Search for any p tag that has the class outer-text')
print(soup.find_all('p', class_='outer-text'))
print('')

print('Look for any tag that has the class outer-text')
print(soup.find_all(class_='outer-text'))
print('')

print('Search for elements by id')
print(soup.find_all(id='first'))
print('')


print('Using CSS Selectors')
print('')

print('''
- p a – finds all a tags inside of a p tag.
- body p a – finds all a tags inside of a p tag inside of a body tag.
- html body – finds all body tags inside of an html tag.
- p.outer-text – finds all p tags with a class of outer-text.
- p#first – finds all p tags with an id of first.
- body p.outer-text – finds any p tags with a class of outer-text inside of a body tag.
''')
print('')

print('find all the p tags in our page that are inside of a div:')
print(soup.select('div p'))
print('')

print('Downloading weather data')
print('''
- Download the web page containing the forecast.
- Create a BeautifulSoup class to parse the page.
- Find the div with id seven-day-forecast, and assign to seven_day
- Inside seven_day, find each individual forecast item.
- Extract and print the first forecast item.
''')
print('')

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())
print('')


print('Extracting all the information from the page')
print('''
- Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
- Use a list comprehension to call the get_text method on each BeautifulSoup object.
''')

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print('')
print(temps)
print('')
print(descs)
print('')

print('Combining our data into a Pandas Dataframe')
import pandas as pd
weather = pd.DataFrame({
            "period": periods, 
            "short_desc": short_descs, 
            "temp": temps, 
            "desc":descs
        })
print(weather)
print('')

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)
print(weather['temp_num'].mean())
print('')

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)
print(weather[is_night])
print('')
