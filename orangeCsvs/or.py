import time
from bs4 import BeautifulSoup
import requests
import urllib.request
from selenium import webdriver
import xlrd
import xlwt
import re
import pandas as pd

station_list = ['APALACHICOLA AP', 'ARCADIA', 'ARCHBOLD BIO STN', 'AVON PARK 2 W', 'BARTOW', 'BELLE GLADE', 'BRADENTON 5 ESE', 'BROOKSVILLE CHIN HILL', 'BUSHNELL 1 E', 'CANAL POINT USDA', 'CHIPLEY', 'CLERMONT 9 S', 'CRESCENT CITY', 'CRESTVIEW BOB SIKES AP', 'CROSS CITY 1 E', 'DAYTONA BEACH', 'DAYTONA BEACH INTL AP', 'DE FUNIAK SPRINGS 1 E', 'DELAND 1 SSE', 'DESOTO CITY 8 SW', 'DEVILS GARDEN', 'EVERGLADES', 'FEDERAL POINT', 'FERNANDINA BEACH', 'FLAMINGO RS', 'FORT DRUM', 'FT GREEN 12 WSW', 'FT LAUDERDALE', 'FT LAUDERDALE BEACH', 'FT MYERS PAGE FLD AP', 'FT PIERCE', 'GAINESVILLE RGNL AP', 'GLEN ST MARY 1 W', 'HASTINGS 4NE', 'HIALEAH', 'HIGH SPRINGS', 'HILLSBOROUGH RIVER SP', 'IMMOKALEE', 'INVERNESS 3 SE', 'JACKSONVILLE INTL AP', 'JACKSONVILLE BEACH', 'JASPER', 'KEY WEST INTL AP', 'KISSIMMEE 2', 'LA BELLE', 'LAKE CITY 2 E', 'LISBON', 'LIVE OAK', 'MADISON', 'MAYO', 'MELBOURNE INTL AP', 'MIAMI BEACH', 'MIAMI INTL AP', 'MONTICELLO 5 SE', 'MONTICELLO 10 SW', 'MOORE HAVEN LOCK 1', 'MTN LAKE', 'MYAKKA RIVER SP', 'NAPLES', 'NICEVILLE', 'OASIS RS', 'OCALA', 'OKEECHOBEE', 'ORLANDO INTL AP', 'PANAMA CITY 5N', 'PARRISH', 'PENSACOLA RGNL AP', 'PERRINE 4W', 'PERRY', 'PLANT CITY', 'PUNTA GORDA 4 ESE', 'QUINCY 3 SSW', 'ROYAL PALM RS', 'ST AUGUSTINE LH', 'SAINT LEO', 'ST PETERSBURG AP', 'SANFORD', 'STUART', 'TALLAHASSEE RGNL AP', 'TAMPA INTL AP', 'TARPON SPGS SEWAGE PL', 'TITUSVILLE', 'USHER TWR', 'VENICE', 'VERO BEACH INTL AP', 'VERO BEACH 4SE', 'WAUCHULA', 'WEEKI WACHEE', 'WEST PALM BEACH INTL AP', 'WEWAHITCHKA']

driver = webdriver.Chrome('/Users/liambo/Desktop/chromedriver')


for station in station_list:
    driver.get('https://climatecenter.fsu.edu/climate-data-access-tools/downloadable-data')
    time.sleep(2)
    

    box = driver.find_element_by_id("down_station")
    box.find_element_by_xpath("//select[@name='down_station']/option[text()='"  + station + "']").click()
    time.sleep(1)
    htmlsource = driver.page_source
    soup = BeautifulSoup(htmlsource)
    yrlist = soup.find_all("select", {"class": "years"})
    Years = yrlist[0].text#.split('\n')
    maxYear = Years[len(Years)-4:len(Years)]
    print(maxYear)

    #box.find_element_by_xpath("//select[@name='down_time']/option[text()='January']").click()
    #time.sleep(1)
    #box.find_element_by_xpath("//select[@name='down_day']/option[text()='1']").click()
    #time.sleep(1)
    #box.find_element_by_xpath("//select[@name='down_year']/option[text()='1978']").click()
    #time.sleep(1)
    box.find_element_by_xpath("//select[@name='down_time_end']/option[text()='December']").click()
    time.sleep(1)
    box.find_element_by_xpath("//select[@name='down_day_end']/option[text()='31']").click()
    time.sleep(1)
    box.find_element_by_xpath("//select[@name='down_year_end']/option[text()='" + maxYear + "']").click()
    time.sleep(1)
    box.find_element_by_xpath("//select[@name='down_variable']/option[text()='All']").click()
    time.sleep(1)
    box.find_element_by_xpath("//input[@type='submit' and @value='Download File']").click()
    time.sleep(3)
    htmlsource = driver.page_source
    #print(htmlsource)

    list = re.split(",|\n", htmlsource)
    print(htmlsource)
    id = []
    year = []
    month = []
    day = []
    precip = []
    maxTemp = []
    minTemp = []
    meanTemp = []

    counter = 0
    for item in list:
     if counter == 0 and item != '</pre></body></html>':
        id.append(item)
     if counter == 1:
        year.append(item)
     if counter == 2:
        month.append(item)
     if counter == 3:
        day.append(item)
     if counter == 4:
        precip.append(item)
     if counter == 5:
        maxTemp.append(item)
     if counter == 6:
        minTemp.append(item)
     if counter == 7:
        meanTemp.append(item)
        counter = 0
     else:
        counter+=1
    print(len(id))
    print(len(year))
    print(len(month))
    print(len(day))
    print(len(precip))
    print(len(maxTemp))
    print(len(minTemp))
    print(len(meanTemp))
    df = pd.DataFrame({'id': id[1:], 'year': year[1:], 'month': month[1:], 'day': day[1:], 'precipitation': precip[1:], 'maxTemp': maxTemp[1:], 'minTemp': minTemp[1:], 'meanTemp': meanTemp[1:]})
    df.to_csv(str(station)+'.csv')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
        
        
time.sleep(10)
driver.quit()





