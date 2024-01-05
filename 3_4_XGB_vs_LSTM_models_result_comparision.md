# Comparison of Predictive Model Results

In the following analysis, I present a comparison of the outcomes obtained from the XGB and LSTM models, utilizing mean absolute error (MAE) as the metric. The MAE was computed for predicting end station delays, leveraging the actual delays at preceding stations.

To facilitate comprehension, let's delve into the specifics of the Budapest-Békéscsaba line. The initial chart illustrates the predicted delays by both models during the test and validation phases at the terminal station. For instance, when considering the actual delay at the first station, the models forecast the delay at the end station (Békéscsaba). Similarly, for the second station, the model predicts the delay at Békéscsaba based on the actual delays at the first and second stations, and so forth.

The second chart plays a crucial role in elucidating the average delays experienced at each station throughout the analyzed period. Notably, both models exhibited enhanced prediction accuracy as the forecasting approached the end stations. Noteworthy, the LSTM model consistently outperformed XGBoost across various lines in both the test and validation phases.

# Budapest-Békéscsaba
![Képernyőkép 2024-01-05 222524](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/6f2b809a-f476-4ee2-8e06-c66c0ff74656)


![Képernyőkép 2024-01-05 222541](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/431a99ae-9ed4-40c3-a90d-e9f173756522)


![Képernyőkép 2024-01-05 222905](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/98a27f91-31e5-48c0-a303-cd70d2dc8076)


![Képernyőkép 2024-01-05 222959](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/b595f0a2-1f20-4ea0-a73f-6d7c2c530de0)


![Képernyőkép 2024-01-05 223212](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/b415f684-04e9-4cff-9d4a-acab30d21ff3)


![Képernyőkép 2024-01-05 223354](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/87921c09-f8bb-4b2e-a2ed-f7b2471fce39)


![Képernyőkép 2024-01-05 223419](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/dcb27004-b2b7-4c7a-8328-8f3852e47221)


![Képernyőkép 2024-01-05 223450](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/6acd09e8-563e-4ab0-a8ea-8de28d2f4a29)


![Képernyőkép 2024-01-05 223505](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/248b4673-d6b5-4688-a87a-77cc54144d68)


![Képernyőkép 2024-01-05 223518](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/8913c731-0de6-4278-b8be-4db391353733)


![Képernyőkép 2024-01-05 223552](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/cb41d869-2e3f-48e8-8135-5d02fd44d805)
![Képernyőkép 2024-01-05 223605](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/1626ff58-0546-4e57-b0ad-03cdd9919365)


![Képernyőkép 2024-01-05 223617](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/25e8faf7-f6c3-4e83-87dc-faeff8bb3d55)
![Képernyőkép 2024-01-05 223631](https://github.com/dataroland/Train_Delays_Analysis/assets/145594847/6dbe61e0-310b-42b3-aa10-57239a3eaf33)
