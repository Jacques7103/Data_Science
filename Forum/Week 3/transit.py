from bs4 import BeautifulSoup
import requests
import pandas as pd

country_list = []
city_list = []
commutet_list = []
commutep_list = []
waitings_list = []
waitingp_list = []
distances_list = []
distancep_list = []
transito_list = []
transitm_list = []
walkd_list = []
walkf_list = []

t_url = 'https://moovitapp.com/insights/en/Moovit_Insights_Public_Transit_Index-commute-time'
w_url = 'https://moovitapp.com/insights/en/Moovit_Insights_Public_Transit_Index-waiting-time'
d_url = 'https://moovitapp.com/insights/en/Moovit_Insights_Public_Transit_Index-commute-distance'
tr_url = 'https://moovitapp.com/insights/en/Moovit_Insights_Public_Transit_Index-transfer-count'
wa_url = 'https://moovitapp.com/insights/en/Moovit_Insights_Public_Transit_Index-walking-distance'
transit_time = 'Howlongdopeopleusuallycommutebypublictransiteveryday?'
transit_people = 'Howmanypeoplehavealongcommuteeverydaywithpublictransit?'
wait_time = 'Howlongdopeopleusuallywaitatastationeveryday?'
wait_people = 'Howmanypeopleusuallywaitalongtimefortheirlineatatransitstationeveryday?'
distance_long = 'Howfardopeopleusuallycommuteeachwaywithpublictransit?'
distance_people = 'Howmanypeoplehavealongcommuteeveryday?'
transit_one = 'Howmanypeopletransferlinesatleastonceineverydayaroundtheworld?'
transit_more = 'Howmanypeopletransfertransitlinesmorethanonceduringasingletripindifferentcities?'
walking_distance = 'Howfardopeopleusuallywalkpertripindifferentcitiesaroundtheworld?'
walking_far = 'Howmanypeopleineachcitywalkformorethan1km?'

t_response = requests.get(t_url)
t_soup = BeautifulSoup(t_response.content)
c_time = t_soup.find_all('section', class_ = 'content-section stats')
for num, c in enumerate(c_time):
    check = c.find('div', class_ = 'query-title').get_text().strip().replace(' ', '')
    if (check == transit_time):
        country = c.find_all('div', class_ = 'bars-container')

        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                commute_time = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace(' min', '')
                # print(f"Average time travel by public transport :  {commute_time}")
                country_list.append(country_name)
                city_list.append(city_name)
                commutet_list.append(commute_time)
    
    elif (check == transit_people):
        # print("======================================================")
        country = c.find_all('div', class_ = 'bars-container')
        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                commute_people = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace('%', '')
                # print(f"Percentage of people that ride public transport more than 2 hour everyday :  {commute_people} of people")
                commutep_list.append(commute_people)

w_response = requests.get(w_url)
w_soup = BeautifulSoup(w_response.content)
w_time = w_soup.find_all('section', class_ = 'content-section stats')
for num, w in enumerate(w_time):
    check = w.find('div', class_ = 'query-title').get_text().strip().replace(' ', '')
    if (check == wait_time):
        country = w.find_all('div', class_ = 'bars-container')

        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                waiting_time = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace(' min', '')
                # print(f"Average waiting time at station :  {waiting_time}")
                waitings_list.append(waiting_time)
    
    elif (check == wait_people):
        # print("======================================================")
        country = w.find_all('div', class_ = 'bars-container')
        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                waiting_people = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace('%', '')
                # print(f"Percentage of people that wait longer than 20 mins :  {waiting_people} of people")
                waitingp_list.append(waiting_people)
                
d_response = requests.get(d_url)
d_soup = BeautifulSoup(d_response.content)
d_time = d_soup.find_all('section', class_ = 'content-section stats')
for num, d in enumerate(d_time):
    check = d.find('div', class_ = 'query-title').get_text().strip().replace(' ', '')
    if (check == distance_long):
        country = d.find_all('div', class_ = 'bars-container')

        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                distance = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace(' km', '')
                # print(f"Average travel distance for single trip :  {distance}")
                distances_list.append(distance)
    
    elif (check == distance_people):
        # print("======================================================")
        country = d.find_all('div', class_ = 'bars-container')
        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                long_distance = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace('%', '')
                # print(f"Percentage of people that travel over 12 km in single direction :  {long_distance} of people")
                distancep_list.append(long_distance)
                
tr_response = requests.get(tr_url)
tr_soup = BeautifulSoup(tr_response.content)
tr_time = tr_soup.find_all('section', class_ = 'content-section stats')
for num, tr in enumerate(tr_time):
    check = tr.find('div', class_ = 'query-title').get_text().strip().replace(' ', '')
    if (check == transit_one):
        country = tr.find_all('div', class_ = 'bars-container')

        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                num_to = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace('%', '')
                # print(f"Percentage of people who transfer transit lines at least once in a single trip  :  {num_to} of people")
                transito_list.append(num_to)
    
    elif (check == transit_more):
        # print("======================================================")
        country = tr.find_all('div', class_ = 'bars-container')
        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                num_tm = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace('%', '')
                # print(f"Percentage of people who transfer transit lines at least twice in a single trip :  {num_tm} of people")
                transitm_list.append(num_tm)
                
wa_response = requests.get(wa_url)
wa_soup = BeautifulSoup(wa_response.content)
wa_time = wa_soup.find_all('section', class_ = 'content-section stats')
for num, wa in enumerate(wa_time):
    check = wa.find('div', class_ = 'query-title').get_text().strip().replace(' ', '')
    if (check == walking_distance):
        country = wa.find_all('div', class_ = 'bars-container')

        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                walkingd = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace(' km', '')
                # print(f"Average distance people walk every day in one direction :  {walkingd} of people")
                walkd_list.append(walkingd)
    
    elif (check == walking_far):
        # print("======================================================")
        country = wa.find_all('div', class_ = 'bars-container')
        for num, x in enumerate(country):
            country_name = x.find('h2', class_ = 'country-title').get_text()
            # print(f"Country : {country_name}")
            city_time = x.find_all('div', class_ = 'bar-text-wrapper')
            for num, y in enumerate(city_time):
                city_name = y.find('span', class_ = 'bar-metro-text').get_text()
                # print(f"City :  {city_name}")
                walkingp = y.find('span', class_ = 'bar-metro-value').get_text().strip().replace('%', '')
                # print(f"Percentage of people who walk for over 1 km each day to reach a specific destination :  {walkingp}% of people")
                walkf_list.append(walkingp)

df = pd.DataFrame({'Country' : country_list, 
                   'City' : city_list, 
                   'Average time travel by public transport (Min)' : commutet_list, 
                   'Percentage of people that ride public transport more than 2 hour everyday (%)' : commutep_list,
                   'Average waiting time at station (Min)' : waitings_list,
                   'Percentage of people that wait longer than 20 mins (%)' : waitingp_list,
                   'Average travel distance for single trip (KM)' : distances_list,
                   'Percentage of people that travel over 12 km in single direction (%)' : distancep_list,
                   'Percentage of people who transfer transit lines at least once in a single trip (%)' : transito_list,
                   'Percentage of people who transfer transit lines at least twice in a single trip (%)' : transitm_list,
                   'Average distance people walk every day in one direction (KM)' : walkd_list,
                   'Percentage of people who walk for over 1 km each day to reach a specific destination (%)' : walkf_list})
# df.to_excel('moovit_before.xlsx', sheet_name= 'sheet1', index=False)
df.to_csv('moovit.csv', index=False)