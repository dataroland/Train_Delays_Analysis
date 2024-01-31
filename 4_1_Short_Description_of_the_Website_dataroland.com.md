# Short Description of the Website - dataroland.com

## Website Focus:

[Dataroland.com](https://dataroland.com) is dedicated to my hobby projects, prominently featuring the Train Delay Project and Weather Forecast Accuracy Project. Offering users a comprehensive experience, the site allows exploration of detailed train delay statistics, station-specific delays, access to a travel helper, and real-time delay forecasts. With a commitment to user engagement and data-driven insights, the website showcases the versatile capabilities of WordPress, Elementor, advanced charting libraries, and website - Ubuntu server communication. Regularly updated data ensures the accuracy and relevance of information presented on dataroland.com.

## Technical Details:

- **Domain:** [dataroland.com](https://dataroland.com)
- **Host:** [hostinger.com](https://www.hostinger.com/)
- **CMS:** WordPress serves as the content management system, boasting plugin architecture and a template system for flexible customization. The site adopts the Colobri WP appearance and integrates Elementor—a drag-and-drop page builder providing a visual editor for efficient and dynamic website creation.

## Website Menu:

- Home
- Hobby Projects
  - Train Delay Project
    - Train Delay Summary
      - Train Delay Statistics
    - Travel Helper
    - Delay Forecast
  - Weather Forecast Accuracy Project
- About Me

## Development and Visualization:

- **Development:** HTML and JavaScript codes are predominantly developed by ChatGPT3.5, ensuring a responsive and interactive user experience.
- **Charting Libraries:** The site leverages chart.js for bar and line charts, along with plotly for waterfall charts, enhancing data visualization capabilities.

## Data Management:

- **Data Source:** Primarily sourced from CSV files on the hostinger server, with regular updates being essential to maintain accuracy.
- **CSV Parsing:** Papa Parse, the fastest in-browser CSV parser for JavaScript, is employed for efficient data handling.

## Technical Challenges:

The most significant challenge in website creation was the implementation of the 'Delay Forecast' site. This involved sending input data to an Ubuntu server, housing the predictive model (Python code). The model's results, in the form of predicted delays, are then sent back to the website. This complex operation was facilitated using Flask and Flask Cors libraries, with NGinx (reverse proxy server) and Gunicorn (WSGI server) to serve Python web applications. Additionally, obtaining an SSL certificate from Let's Encrypt ensured secure communication with the server. The successful integration of these technical elements enhances the website's functionality and real-time prediction capabilities.
After two months, I changed the previously mentioned solution to a more stable one. I calculated all combinations of the possible results of the predictive model and uploaded them to a CSV file on the web server.
