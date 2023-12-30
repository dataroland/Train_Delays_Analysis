# Predictive Models

The predictive models in this project are designed to forecast train delays, providing valuable insights for both travelers and train companies. The project distinguishes between two types of predictions based on the time horizon: long-term prediction and short-term prediction.

## Long-term Prediction:

The long-term prediction model utilizes historical train operation data to understand the impact of various factors on railway system performance. By analyzing aggregated historical data, the model predicts delays several days in advance. Factors such as InterCity name, traveling time, and weather-related data were taken into account to assess their impact on train events.

### Assumptions and Results:

- **Objective:** Predict delays at the end station of the line for the next 1-2 weeks.
- **Dataset:** Train-related info for the twelve routes between 22-June 2023 and 23-Sept 2023.
- **Exclusions:** Extreme long delays (above 30 min) were excluded.
- **Features Used:** InterCity name, day of the week, departure hour, train line, and weather-related data.
- **Model Types:** Linear regression, Gradient boosting, and Random forest were employed using both raw and aggregated (average) data.
- **Outcome:** The best-performing model used aggregated data (average), achieving an R2-score above 0.7 and a mean absolute error close to 1 min.
- **Future Improvements:** Model building is temporarily suspended to collect more data (at least 1 year) to capture seasonality and enhance prediction accuracy. In the meantime, a simple web application has been created for travelers to check average expected delays based on historical data.

## Short-term Prediction:

The short-term prediction model focuses on real-time data, allowing travelers to predict delays for the next stations based on their current location. Two types of calculations were performed: one for training and validation databases to assess prediction accuracy and another as a delay forecast for immediate use.

### Assumptions and Results:

- **Databases:** Training/test (22-Jun 2023 to 29-Oct 2023) and validation (30-Oct to 14-November) databases were created, excluding trains above 30 min delay.
- **Line-Specific Models:** Twelve different databases were created based on train routes, aiming to find patterns in sequential delays from station to station.
- **Model Types:** XGBoost and LSTM models were chosen for their ability to capture sequential dependencies.
- **Outcome:** Both models showed improved prediction accuracy as the prediction moved closer to the end stations. LSTM outperformed XGBoost in most lines in both test and validation phases.
- **Web Application:** XGBoost was selected for the web application due to its fast computation and acceptable prediction results.

In summary, the project combines both long-term and short-term predictive models, leveraging historical and real-time data to enhance the efficiency of train travel for both passengers and train companies.

*Source: [A review of data-driven approaches to predict train delays](https://www.sciencedirect.com/science/article/pii/S0968090X23000165)*
