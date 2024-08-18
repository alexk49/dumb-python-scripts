"""

anorak.py

Used to get weather for day and advised if an anorak is needed
"""
import requests 
import bs4
import lxml 

res = requests.get("https://www.bbc.co.uk/weather/2648301")

soup = bs4.BeautifulSoup(res.text,"lxml")

weatherType = soup.select(".wr-weather-type__text")[0]
weatherType = weatherType.text.lower()

def weather_check(weatherType):
	if "rain" in weatherType:
	    return ("Bring a waterproof")
	elif "drizzle" in weatherType:
	    return ("Bring a waterproof, just to be sure")
	elif "sunny" in weatherType:
	    return ("Bring a hat")

todaysTemp = soup.select(".wr-value--temperature--c")[0]

todaysTemp = int(todaysTemp.text[:-1])

def temp_check(todaysTemp):
	if todaysTemp < 10:
	    return ("and bring a coat")
	elif todaysTemp < 15:
	    return ("and bring a jacket")
	elif todaysTemp <= 20:
	    return ("and bring a light jumper")
	elif todaysTemp <= 25:
		return ("and consider wearing shorts and don't forget sun screen")
	elif todaysTemp > 25:
	    return ("and it's going to be hot hot hot, and don't forget sun screen")

waterproof = weather_check(weatherType) 
layers = temp_check(todaysTemp)

print(waterproof + ' ' + layers)
