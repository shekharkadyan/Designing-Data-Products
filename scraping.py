import sys
# import the library we use to open URLs
import urllib.request
import time
import requests
#website_url = requests.get("https://en.wikipedia.org/wiki/1991_World_Wrestling_Championships").text
#website_url = requests.get("https://en.wikipedia.org/wiki/1991_World_Championships_in_Athletics").text
website_url_old = requests.get("https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-athletics-championships-doha-2019-7125365/results/men/100-metres/final/result").text
website_urls_men = ["https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-athletics-championships-doha-2019-7125365/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-championships-london-2017-7093740/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/15th-iaaf-world-championships-7078726/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/14th-iaaf-world-championships-7003368/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/13th-iaaf-world-championships-in-athletics-7003367/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/12th-iaaf-world-championships-in-athletics-6998524/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/11th-iaaf-world-championships-in-athletics-6903480/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/10th-iaaf-world-championships-in-athletics-6937596/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/9th-iaaf-world-championships-in-athletics-6930156/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/8th-iaaf-world-championships-6947294/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/7th-iaaf-world-championships-in-athletics-6939522/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/6th-iaaf-world-championships-in-athletics-6913256/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/5th-iaaf-world-championships-in-athletics-6997728/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/4th-iaaf-world-championships-in-athletics-6993598/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/3rd-iaaf-world-championships-in-athletics-6987209/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/2nd-iaaf-world-championships-in-athletics-6986221/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/1st-iaaf-world-championships-in-athletics-6988504/results/men/"]
website_urls_women = ["https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-athletics-championships-doha-2019-7125365/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-championships-london-2017-7093740/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/15th-iaaf-world-championships-7078726/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/14th-iaaf-world-championships-7003368/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/13th-iaaf-world-championships-in-athletics-7003367/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/12th-iaaf-world-championships-in-athletics-6998524/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/11th-iaaf-world-championships-in-athletics-6903480/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/10th-iaaf-world-championships-in-athletics-6937596/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/9th-iaaf-world-championships-in-athletics-6930156/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/8th-iaaf-world-championships-6947294/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/7th-iaaf-world-championships-in-athletics-6939522/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/6th-iaaf-world-championships-in-athletics-6913256/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/5th-iaaf-world-championships-in-athletics-6997728/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/4th-iaaf-world-championships-in-athletics-6993598/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/3rd-iaaf-world-championships-in-athletics-6987209/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/2nd-iaaf-world-championships-in-athletics-6986221/results/women/","https://www.worldathletics.org/competitions/world-athletics-championships/1st-iaaf-world-championships-in-athletics-6988504/results/women/"]
#website_urls = ["https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-athletics-championships-doha-2019-7125365/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/iaaf-world-championships-london-2017-7093740/results/men/","https://www.worldathletics.org/competitions/world-athletics-championships/15th-iaaf-world-championships-7078726/results/men/"]
years = list(range(2019,1989,-2))
years.append(1987)
years.append(1983)
events_men = ["100-metres","200-metres","400-metres","800-metres","1500-metres","5000-metres","10000-metres","marathon","3000-metres-steeplechase","110-metres-hurdles","400-metres-hurdles","high-jump","pole-vault","long-jump","triple-jump","shot-put","discus-throw","hammer-throw","javelin-throw","20-kilometres-race-walk","50-kilometres-race-walk","4x100-metres-relay","4x400-metres-relay"]
events_women = ["100-metres","200-metres","400-metres","800-metres","1500-metres","5000-metres","10000-metres","marathon","3000-metres-steeplechase","100-metres-hurdles","400-metres-hurdles","high-jump","pole-vault","long-jump","triple-jump","shot-put","discus-throw","hammer-throw","javelin-throw","20-kilometres-race-walk","50-kilometres-race-walk","4x100-metres-relay","4x400-metres-relay"]

# import the BeautifulSoup library so we can parse HTML and XML documents
from bs4 import BeautifulSoup

YE=[]
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

tbegin = time.time()
failedCount =0
failedData=[]
for url, year in zip(website_urls_women,years):
    for event in events_women:
        website_url = url+event+"/final/result"
        website_url_request = requests.get(website_url).text
        print ("year is "+ str(year))#+ " my website url is "+ website_url)
        soup = BeautifulSoup(website_url_request,'lxml')
        all_tables=soup.find_all("table")

        right_table=soup.find('table', class_='records-table clickable')

        
        #E=[]
        try:
            for tr in right_table.findAll('tr'):
                #td = tr.find_all('td')
                cells=tr.findAll('td')
                if len(cells)==6 and year >1997:
                    #print ("celllllsss", cells)
                    YE.append(str(year)+"|"+str(event))
                    A.append(cells[0].text)
                    #B.append(cells[1].text)
                    B.append(cells[2].text)
                    C.append(cells[3].text)
                    D.append(cells[4].text)
                    E.append(cells[5].text)
                elif len(cells)==5 and year <= 1997:
                    YE.append(str(year)+"|"+str(event))
                    A.append(cells[0].text)
                    B.append(cells[1].text)
                    C.append(cells[2].text)
                    D.append(cells[3].text)
                    E.append(cells[4].text)
        except:
            print ("--------------------------------Data collection failed " + str(year)+ " event " + event + "-------------------")
            failedCount+=1
            failedData.append((year,event, website_url))


import pandas as pd
df=pd.DataFrame(YE,columns=['Year Event'])
#df['Order/Lane']=A
df['Pos']=A
df['Athlete']=B
df['Country']=C
df['Mark']=D
df['Reaction time']=E

print ("--------")
print(df)
print (failedCount)
print (failedData)
df.to_csv(r'D:\mba\cornell course\designing data products\WAC result women.csv')
tend = time.time()
print ((tend-tbegin)/60)
