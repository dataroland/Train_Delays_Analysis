# Power BI Presentation:

For visualizing train delay data, I opted for [Microsoft Power BI](https://powerbi.microsoft.com/), an interactive data visualization software developed by Microsoft, primarily designed for business intelligence. Power BI comprises a suite of software services, apps, and connectors that collaborate seamlessly to transform diverse data sources into both static and interactive visualizations. Data can be sourced from databases, web pages, PDFs, or structured files such as spreadsheets, CSV, XML, JSON, XLSX, and SharePoint.

## 1) Data Discovery / Data Shaping:

I integrated Power BI with my PostgreSQL database on my Ubuntu server using SQL scripts. Daily, the SQL table receives new data, representing the previous day's delay information, automatically reflecting in the reports after refreshing. Several transformations were applied to the data:

- Changing column types
- Excluding duplicated columns
- Renaming columns
- Extracting the hour from date time
- Calculating train speeds from different columns
- Adding columns like day of the week and different delay categories

## 2) Data Modeling:

While the primary focus is on one table (train delays), I established connections to a weather data table through date columns (many-to-one relationship). I incorporated simple Data Analysis Expressions (DAX) for metrics such as average delay per day, median, variance, and standard deviation. Although not imperative due to SQL table capabilities, these DAX expressions provide additional analytical depth. As the database grows, future optimization plans include applying a star schema and creating separate databases for station-related and date-related information.

## 3) Data Visualization:

Diverse charts were crafted to represent train delay data, including bar and line charts, waterfall charts, histograms, funnels, simple tables, and a map visualization of train delays using circles for each station. A toolkit for train stations enhances interactivity, revealing information when hovering over a station. The report encompasses the following slides:

- Download statistics, displaying daily data received, with a funnel analysis for row vs. used data in the reports
- Daily breakdown of all delays, offering train-by-train analysis if necessary
- A histogram illustrating the distribution of train delays
- Train line information, including line distance, travel time, train speeds, and station count
- Average delays of train lines, showcasing delay proportions concerning total train time with daily, weekly, and monthly slicers
- Delay categories, providing a comprehensive breakdown
- Delay visualization by Intercity name, weekday, and departure time
- Delays by train stations, featuring waterfall charts and stop/running delay visualization

## 4) Data Sharing:

This report serves a personal purpose, designed exclusively for my use without publication or sharing with others.
