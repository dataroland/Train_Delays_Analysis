<h1>Train Delays Analysis</h1>

 

<h2>Description</h2>
In this project, I conducted a comprehensive analysis of delays on selected passenger railway routes in Hungary. The delays were meticulously derived by comparing the official timetables with real-time train information provided by the Hungarian Railways (MÁV). Specifically, I focused on six key passenger train routes, namely: Budapest-Szeged, Budapest-Pécs, Budapest-Debrecen, Budapest-Békéscsaba, Budapest-Keszthely, Keszthely-Győr, including their return journeys. My analysis primarily revolved around InterCity trains operating between 6:00 am and 9:00 pm. It's worth noting that the start and end stations of these routes don't always align with the cities mentioned above. For example, in the case of Budapest-Békéscsaba, the Békéscsaba train station isn't necessarily the final destination, and for Debrecen-Budapest, the initial departure station differs from Debrecen.

To gather data for this project, I employed an automated daily data retrieval process, utilizing Selenium and BeautifulSoup, from the official Hungarian Railways website (https://elvira.mav-start.hu/). This data was then stored in CSV files on my dedicated server and subsequently uploaded into SQL tables using PostgreSQL. I used this data to create various informative dashboards in POWER BI.

The dataset consisted of approximately 1,200 to 1,300 daily records, encompassing essential information such as planned and actual departure and arrival times, the names of train stations, the specific train line names, distances between stations, and route distances, among other details. Furthermore, I went a step further and generated predictive models for future delays, considering historical data and forecasted weather conditions.

It's important to note that the primary objective of this project was not to directly address the train delay issues faced by the Hungarian Railways (MÁV). Instead, the goal was to enhance my skills in data analytics and provide valuable information to passengers, enabling them to plan their journeys more efficiently and minimize travel time.
<br />


<h2>Languages Used</h2>

- <b>Python, Selenium, BeautifulSoup, Pandas</b>
- <b>Bash</b>
- <b>PostgreSQL</b>


<h2>Environments Used </h2>

- <b>Remote data server (Ubuntu), mcedit, crontab</b>
- <b>Jupyter Notebooks, SQLWorkbench</b>
- <b>POWER BI Desktop</b>

<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>