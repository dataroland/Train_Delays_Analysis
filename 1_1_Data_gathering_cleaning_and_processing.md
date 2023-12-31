# Data Gathering, Cleaning, and Processing

## 1) Data Collection:

Initiating the process, I systematically retrieve train delay data from the [MAV-START Elvira website](https://elvira.mav-start.hu/) from my Ubuntu server, focusing specifically on chosen train routes:

- Budapest-Keszthely
- Budapest-Pécs
- Budapest-Debrecen
- Budapest-Békéscsaba
- Budapest-Szeged
- Keszthely-Győr

...and their corresponding return routes. The selection criteria include direct connections and InterCity trains (excluding the Keszthely-Győr route). Employing Selenium and BeautifulSoup for web scraping, the following data is captured:

**Basic Train Information:**
- Report Datetime: The timestamp when the data is downloaded.
- Train Number: A unique identifier assigned to each train.
- Train Name (InterCity): The specific name of the InterCity train.
- Train Date: The scheduled date when the train is due.
- Train Start Time: The departure time from the first station according to the timetable.
- Train End Time: The arrival time at the last station according to the timetable.
- Train Duration: The total duration of the train journey in hours and minutes.
- Distance of the Line: The total distance covered by the train route.
- Train Start Place: The name of the first station, which may differ from the route name.
- Train End Place: The name of the end station, which may differ from the route name.

**Station-Specific Information:**
- Station Name: The name of the station where the train stops.
- Train Arrival Time (Timetabled): The scheduled time when the train should arrive at the station.
- Train Arrival Time (Actual): The actual time when the train arrived at the station.
- Train Departure Time (Timetabled): The scheduled time when the train should depart from the station.
- Train Departure Time (Actual): The actual time when the train departed from the station.
- Station Distance from the First Station: The distance of the station from the starting point.
- Analyzed Train Line: The name of the train line being analyzed.
- Station Distance from the First Station: The distance of the station from the first station in kilometers.

Each night, between 22:00 and 00:00, this data is automatically collected on an Ubuntu server, stored in a CSV file, and uploaded to a PostgreSQL table.

## 2) Data Cleaning:

The subsequent step involves refining the data through a SQL script to ensure a focus on pertinent information for analysis. Exclusions encompass:

- **Train Stations:** exclusion of local or foreign stations out of the analyzed line (approximately 27% of all data).
- **Intermediate and Technical Stations:** exclusion of stations within the train line that are not universally served by all trains, along with technical stations (approximately 5% of all data).
- **Incomplete Train Journeys and Excessive Delays:** exclusion of trains unable to complete the line, those missing actual arrival or departure times at any of the stations, or experiencing delays longer than 150 minutes (approximately 4% of all data).

Additionally, a station mapping table is prepared to facilitate operations, mapping train lines with analyzed stations and marking start, end, middle, and out-of-scope stations.

## 3) Data Calculation:

Within the script, crucial features are calculated from the collected data:

- **Delay calculation:**
  - Arrival time difference (in minutes) between actual and timetabled.
  - Departure time difference (in minutes) between actual and timetabled.
- **Delay Components:**
  - Running delay (delay between two stations or faster travel).
  - Stop delay (waiting longer than timetabled).
  - Station delay (combination of running delay and stop delay).
- **Additional Features:**
  - Week number.
  - Month number.
  - Distance in kilometers (excluding 'km').
  - Day of the week.

This comprehensive script serves as the foundation for the Power BI presentation, prediction models, and website functionalities, ensuring detailed insights for each of the specified train routes. The dataset is refreshed on a daily basis with the previous day's delay data.
