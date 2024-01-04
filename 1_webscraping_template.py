#!/usr/bin/env python3

#the trains with the duration (h:mm), I would like to analyze:
bp_debrecen = ["2:28", "2:30", "2:33", "2:38", "2:35"]
bp_keszthely = ["2:36"]
keszthely_gyor = ["2:34", "2:36"]
bp_bekescsaba = ["2:29", "2:30"]
bp_pecs = ["2:50", "2:46", "2:47"]
bp_miskolc = ["2:00", "2:04", "2:05", "2:10", "2:11", "2:15"]
bp_hegyeshalom = ["1:49", "1:51", "1:52"]
bp_gyor = ["1:20", "1:22", "1:23", "1:24", "1:33", "1:39", "1:42", "1:44", "1:43"]
bp_zalaegerszeg = ["3:08", "3:12", "3:10"]
bp_nagykanizsa = ["3:09", "3:14", "3:10"]
bp_szombathely = ["3:17", "3:18", "3:29", "3:30", "3:27", "3:35", "3:21", "3:24"]
bp_k_szombathely = ["3:34", "3:31", "3:36"]
bp_sopron = ["2:23", "2:28", "2:27"]
cities = ["Budapest-Nyugati", "Budapest-Déli", "Budapest-Keleti", "Debrecen", "Keszthely", "Győr", "Szeged", "Pécs", "Békéscsaba", "Miskolc-Tiszai", "Hegyeshalom", "Zalaegerszeg", "Nagykanizsa", "Szombathely", "Győr", "Sopron"]

from_where = cities[1]
destination = cities[4]
needed_trains = bp_keszthely


# import libraries
import time
import signal
import datetime
import pytz
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# if the code receives an error message than repeat the execution max 5 times and one try cannot be longer than 150 sec
max_retries = 5
max_execution_time = 250

def timeout_handler(signum, frame):
    raise TimeoutError("Script execution timed out")

signal.signal(signal.SIGALRM, timeout_handler)

retry_count = 0



def parse_trains(j,a):
    """
    This function goes through the train variants by different time options during the day and collect data.
    """
    page_source = driver.page_source
    from bs4 import BeautifulSoup
    city_temp1 = BeautifulSoup(page_source, 'html.parser')
        
    timetable1 = city_temp1.find(class_="rtf").tbody.find_all("tr")
    timetable2 = city_temp1.find(class_="rtf").tbody.find_all('div', class_="morebutton")
        
    
    y = 0
        
    for div in timetable2:
    
        #if the duration of the train is not equal with the required duration than do not download the data:
        i = 1
        if timetable1[y].find_all("td")[4].get_text(strip=True) not in needed_trains:
            y = y + 5
            j = j + 2
            a = a + 2
            
            continue  
        #I would like to exclude the same trains in the same time:
        if timetable1[y].find_all("td")[1].get_text(strip=True) == timetable1[y-5].find_all("td")[1].get_text(strip=True):
            y = y + 5
            j = j + 2
            a = a + 2
            
            continue 
        
        # open the train variant by different times
        xpath1 = "/html/body/div[1]/div[4]/div[1]/div/div[1]/div[7]/div/table/tbody/tr["
        xpath2 = str(j)
        xpath3 = "]/td[1]/div/a/img"
        xpath4 = xpath1 + xpath2 + xpath3
        link2 = driver.find_element(By.XPATH, xpath4)
        try: 
            link2.click()
        except:
            j = j + 2
            a = a + 2
            i = i + 1
    
            continue
        time.sleep(2)
        
        # click on the train_number to receive the details (stations, arriving time, departure time etc)
        xpath5 = "/html/body/div[1]/div[4]/div[1]/div/div[1]/div[7]/div/table/tbody/tr["
        xpath6 = str(j+1)
        xpath7 = "]/td/div/table/tbody/tr[1]/td[6]/a"
        xpath8 = xpath5 + xpath6 + xpath7
        
        try: 
            link3 = driver.find_element(By.XPATH, xpath8)
            link3.click()
        except:
            xpath5 = "/html/body/div[1]/div[4]/div[1]/div/div[1]/div[7]/div/table/tbody/tr["
            xpath6 = str(j+1)
            xpath7 = "]/td/div/table/tbody/tr[1]/td[5]/a"
            xpath8 = xpath5 + xpath6 + xpath7
            link3 = driver.find_element(By.XPATH, xpath8)
            link3.click()
        time.sleep(2)

        # parse the page
        page_source = driver.page_source
        from bs4 import BeautifulSoup
        city = BeautifulSoup(page_source, 'html.parser')
    
        utc_datetime = datetime.datetime.now(pytz.utc)
        budapest_timezone = pytz.timezone('Europe/Budapest')
        converted_datetime = utc_datetime.astimezone(budapest_timezone)

        # additional help steps for creating dataset
        train_route_full = []
        allomas = city.find_all("div", id="menetrend")
        try: 
            allomas = allomas[0]
        except IndexError:
            j = j + 2
            a = a + 2
            i = i + 1
            driver.back()
            continue
        
        
        help = allomas.find_all("tr")[2:]
    

        date2 = city_temp1.find_all("td", class_="l")[a].get_text(strip=True)
        date3 = city_temp1.find_all("td", class_="l")[a+1].get_text(strip=True)
        help_time = timetable1[y].find_all("td")[4].get_text(strip=True)
        help_dist = timetable1[y].find_all("td")[5].get_text(strip=True)
    
    
        j = j + 2
        a = a + 2
        y = y + 5
        
        # receive the needed data by different starting times
        for tr in help:
            if help[i-1].a is None:
                i = i + 1
                continue
            dictionary = {}
            dictionary['report_datetime'] = converted_datetime.strftime("%Y-%m-%d %H:%M:%S")
            dictionary['report_date'] = converted_datetime.strftime("%Y-%m-%d")
            dictionary['report_hour'] = converted_datetime.strftime("%H")
            train_number = city.find_all('div', id="tul")[0].h2.get_text().split(' ')
            train_number = train_number[0]
            dictionary['train_number'] = train_number
            
            train_name = city.find_all('div', id="tul")[0].h2.get_text().split(" (")[0].split(" ")[1:]
            train_name = ' '.join(train_name)
            dictionary['train_name'] = train_name
            
            dictionary['train_date1'] = city_temp1.find("div", class_="rrtftop").get_text(strip=True).split(",")[0]
            dictionary['train_start_time'] = date2
            dictionary['train_end_time'] = date3
            dictionary['train_time'] = help_time
            dictionary['distance'] = help_dist
            
            train_start_place = city.find_all('div', id="tul")[0].h2.get_text(strip=True).split('(')[1].split(')')[0].split(' - ')[0]
            dictionary['train_start_place'] = train_start_place

            train_end_place = city.find_all('div', id="tul")[0].h2.get_text(strip=True).split('(')[1].split(')')[0].split(' - ')[1]
            dictionary['train_end_place'] = train_end_place
            
            dictionary['train_station'] = help[i-1].a.get_text(strip=True)
            if help[i-1].find_all('td')[2].get_text(strip=True) == '':
                dictionary['train_arrtime_t'] = '00:00'
            else:
                dictionary['train_arrtime_t'] = help[i-1].find_all('td')[2].get_text(strip=True)
    
            try:
                if help[i-1].find_all('td')[4].get_text(strip=True) == '':
                    if help[i-1].find_all('td')[6].get_text(strip=True) == '':
                        dictionary['train_arrtime_a'] = '00:00'
                    else:
                        dictionary['train_arrtime_a'] = help[i-1].find_all('td')[6].get_text(strip=True)
                else:
                    dictionary['train_arrtime_a'] = help[i-1].find_all('td')[4].get_text(strip=True)
            except:
                dictionary['train_arrtime_a'] = '00:00'
            
            if help[i-1].find_all('td')[3].get_text(strip=True) == '':
                dictionary['train_deptime_t'] = '00:00'
            else:
                dictionary['train_deptime_t'] = help[i-1].find_all('td')[3].get_text(strip=True)
    
            try:
                if help[i-1].find_all('td')[5].get_text(strip=True) == '':
                    if help[i-1].find_all('td')[7].get_text(strip=True) == '':
                        dictionary['train_deptime_a'] = '00:00'
                    else:
                        dictionary['train_deptime_a'] = help[i-1].find_all('td')[7].get_text(strip=True)   
                else:
                    dictionary['train_deptime_a'] = help[i-1].find_all('td')[5].get_text(strip=True)
            except:
                dictionary['train_deptime_a'] = '00:00'
            
            analyzed_line = (city_temp1.find("div", class_="lrtftop").get_text(strip=True).split(" "))
            analyzed_line = ''.join(analyzed_line)
            dictionary['analyzed_line'] = analyzed_line
            if help[i-1].find("td").get_text(strip=True) == '':
                dictionary['station_km'] = '1000'
            else:
                dictionary['station_km'] = help[i-1].find("td").get_text(strip=True)
            
            i = i + 1
            train_route_full.append(dictionary)

        train_route_full_full.extend(train_route_full)
        driver.back()
        
    return train_route_full_full

while retry_count < max_retries:
    try:
        signal.alarm(max_execution_time)
        
        #start the code
        
        service = Service(executable_path="path of the chromedriver")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://elvira.mav-start.hu/")
        time.sleep(3)
        
        # click on "without transfer" button
        
        link = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/form/div[3]/div[1]/div[2]/div[3]/div[3]/div[1]/input")
        link.click()
        time.sleep(1)
        # add from where
        search = driver.find_element(By.NAME, "i")
        search.send_keys(from_where)
        #search.send_keys(Keys.RETURN)
        time.sleep(1)
        # add to where
        search = driver.find_element(By.NAME, "e")
        search.send_keys(destination)
        #search.send_keys(Keys.RETURN)
        
        
        # click on the search button
        link1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/form/div[3]/div[2]/div/input")
        link1.click()
        time.sleep(1)
                
        train_route_full_full = []     
        
        # receive the list of the train options
        parse_trains(1,0)
        
        
        # return button
        link5 = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[1]/form/div[3]/div[2]/div/input[2]")
        link5.click()
        time.sleep(1)
        
        
        #return
        parse_trains(1,0)
        
        
        
        driver.quit()
        
        signal.alarm(0)
        
        break
        
    except TimeoutError:
        retry_count += 1
        print(f"Script execution time exceeded {max_execution_time} seconds. Restarting...") 
        
    except Exception as e:
        retry_count += 1
        print(f"Error: {e}")
        if retry_count < max_retries:
            print(f"Attempting to run the script again (Retry {retry_count}/{max_retries})...")
        else:
            print("Max retries reached. Exiting.")

train_route_full_full_df = pd.DataFrame(train_route_full_full)

utc_datetime = datetime.datetime.now(pytz.utc)
budapest_timezone = pytz.timezone('Europe/Budapest')
converted_datetime = utc_datetime.astimezone(budapest_timezone)

dictionary_path1 = 'path1 of the folder on the server'
date_hour_format = converted_datetime.strftime("%Y-%m-%d_%H")
file_path1 = dictionary_path1 + date_hour_format
train_route_full_full_df.to_csv(file_path1, index=False, header=False)

file_path2 = 'path2 of the folder on the server'
train_route_full_full_df.to_csv(file_path2, mode='a', index=False, header=False)
