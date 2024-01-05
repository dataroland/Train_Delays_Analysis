# Training data preparation for the model
```python


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

basic_table = pd.read_csv('path to the csv file', delimiter = ',')

agg_weather_data = pd.read_csv('path to the csv file', delimiter = ',')
basic_table = basic_table.merge(agg_weather_data, how = 'left', left_on = 'report_date', right_on = 'actual_date')

basic_table['start_hour'] = basic_table['train_start_time'].str.split(':').str[0]
basic_table['start_hour'] = pd.to_numeric(basic_table['start_hour'], errors='coerce')

analyzed_line = ['Budapest-Keleti-Békéscsaba', 'Békéscsaba-Budapest-Keleti', 'Budapest-Nyugati-Szeged', 'Szeged-Budapest-Nyugati', 'Budapest-Déli-Keszthely', 'Keszthely-Budapest-Déli', 'Budapest-Keleti-Pécs', 'Pécs-Budapest-Keleti', 'Budapest-Nyugati-Debrecen', 'Debrecen-Budapest-Nyugati', 'Keszthely-Győr', 'Győr-Keszthely']

basic_table = basic_table[basic_table.analyzed_line == analyzed_line[0]][['train_station', 'report_date', 'train_number', 'arrtime_diff', 'deptime_diff', 'running_delay', 'stop_delay', 'station_delay', 'start_hour', 'train_name',  'day_of_week', 'station_km', 'max_temp','sum_rain_mm', 'distance_km', 'station_index']].reset_index(drop=True)
short_table1 = basic_table[basic_table.arrtime_diff < 3000].reset_index(drop=True)
short_table1['day_of_week'] = short_table1['day_of_week'].str.strip()

short_table1['key'] = short_table1['report_date'] + short_table1['train_number'].astype(str) + short_table1['train_name']

# Find trains with end station delay greater than 30 minutes
stations = short_table1.groupby(['station_index']).count().reset_index(drop=False)['station_index'].tolist()
stations = sorted(stations, key=lambda x: int(x.split('_')[0]))
problem_trains = short_table1[short_table1['station_index'] == stations[len(stations)-1]]
problem_trains = problem_trains[problem_trains['arrtime_diff'] > 30]['key'].unique()

# Function to determine the value for the new column
def calculate_station_status(row):
    if row['key'] in problem_trains:
        return 0
    else:
        return 1

# Apply the function to create a new column 'station_status'
short_table1['filter1'] = short_table1.apply(calculate_station_status, axis=1)
short_table1 = short_table1[short_table1.filter1 == 1]


short_table1_adj = short_table1[['key', 'train_name', 'start_hour', 'day_of_week']]
pivoted_table_arr = short_table1.pivot(index='key', columns='station_index', values=['arrtime_diff'])

pivoted_table_dep = short_table1.pivot(index='key', columns='station_index', values=['deptime_diff'])

pivoted_table = pivoted_table_arr.merge(pivoted_table_dep, on='key', how='left')

stations_column = [('deptime_diff', '1_station')]
stations_column += [('arrtime_diff', f'{i}_station') for i in range(2, len(stations) + 1)]
data = pivoted_table.loc[:, stations_column]
```

# Validation data preparation for the model

```python
basic_table_test = pd.read_csv('path to the csv file', delimiter = ',')

basic_table_test['start_hour'] = basic_table_test['train_start_time'].str.split(':').str[0]
basic_table_test['start_hour'] = pd.to_numeric(basic_table_test['start_hour'], errors='coerce')

analyzed_line_test = ['Budapest-Keleti-Békéscsaba', 'Békéscsaba-Budapest-Keleti', 'Budapest-Nyugati-Szeged', 'Szeged-Budapest-Nyugati', 'Budapest-Déli-Keszthely', 'Keszthely-Budapest-Déli', 'Budapest-Keleti-Pécs', 'Pécs-Budapest-Keleti', 'Budapest-Nyugati-Debrecen', 'Debrecen-Budapest-Nyugati', 'Keszthely-Győr', 'Győr-Keszthely']

basic_table_test = basic_table_test[basic_table_test.analyzed_line == analyzed_line_test[0]][['train_station', 'report_date', 'train_number', 'arrtime_diff', 'deptime_diff', 'running_delay', 'stop_delay', 'station_delay', 'start_hour', 'train_name',  'day_of_week', 'station_km', 'distance_km', 'station_index']].reset_index(drop=True)
short_table1_test = basic_table_test[basic_table_test.arrtime_diff < 3000].reset_index(drop=True)
short_table1_test['day_of_week'] = short_table1_test['day_of_week'].str.strip()

short_table1_test['key'] = short_table1_test['report_date'] + short_table1_test['train_number'].astype(str) + short_table1_test['train_name']

# Find trains with end station delay greater than 30 minutes
stations_test = short_table1_test.groupby(['station_index']).count().reset_index(drop=False)['station_index'].tolist()
stations_test = sorted(stations_test, key=lambda x: int(x.split('_')[0]))
problem_trains_test = short_table1_test[short_table1_test['station_index'] == stations_test[len(stations_test)-1]]
problem_trains_test = problem_trains_test[problem_trains_test['arrtime_diff'] > 30]['key'].unique()

# Function to determine the value for the new column
def calculate_station_status_test(row):
    if row['key'] in problem_trains_test:
        return 0
    else:
        return 1

# Apply the function to create a new column 'station_status'
short_table1_test['filter1'] = short_table1_test.apply(calculate_station_status_test, axis=1)
short_table1_test = short_table1_test[short_table1_test.filter1 == 1]


short_table1_adj_test = short_table1_test[['key', 'train_name', 'start_hour', 'day_of_week']]
pivoted_table_arr_test = short_table1_test.pivot(index='key', columns='station_index', values=['arrtime_diff'])

pivoted_table_dep_test = short_table1_test.pivot(index='key', columns='station_index', values=['deptime_diff'])


pivoted_table_test = pivoted_table_arr_test.merge(pivoted_table_dep_test, on='key', how='left')
stations_column_test = [('deptime_diff', '1_station')]
stations_column_test += [('arrtime_diff', f'{i}_station') for i in range(2, len(stations_test) + 1)]
data_test = pivoted_table_test.loc[:, stations_column_test]
data_test = data_test.values.tolist()
data_test_float = [[float(x) for x in inner_list] for inner_list in data_test]
```

# Train the data on the model

```python
stations = short_table1.groupby(['station_index']).count().reset_index(drop=False)['station_index'].tolist()
stations = sorted(stations, key=lambda x: int(x.split('_')[0]))

e = 0
i = 1
delays = []
accuracy_test = []
for station in range(0, len(stations)-1):
    #model
    # Define the features and target variable
    choosed_station = stations[0:i]
    input_stations = stations_column[0:i]
    target_station = stations_column[(e+1):len(stations)]
    stations_full = input_stations + target_station
    
    X = data[input_stations]
    y = data[target_station]
    
    # Encode categorical variables using one-hot encoding
    #X = pd.get_dummies(X, columns=['key', 'station_number', 'day_of_week'], drop_first=False)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create an XGBoost model
    model = XGBRegressor()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Metrics calculation:
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    metrics = ['mae', 'mse', 'rmse', 'r2_score']
            
    predicted_data = y_pred
    actual_data = y_test
    
    mae = mean_absolute_error(y_pred, y_test)
    mse = mean_squared_error(y_pred, y_test)
    rmse = np.sqrt(mse)
    r2_value = r2_score(y_pred, y_test)
    accuracy_test.append(mae)
    accuracy_test.append(mse)
    accuracy_test.append(rmse)
    accuracy_test.append(r2_value)

    # Validation with external data:
    s = 0
    for test in range(0, len(data_test)):
        t = 0
        #input
        delay_at_input_stations = data_test[s][0:(e+1)]
        #delay_at_input2_station = 12
        dictionary = {}
        
        for dic in range(0, len(delay_at_input_stations)):
            dictionary[stations_full[t]]= [delay_at_input_stations[t]]
            t = t + 1
        input_data = pd.DataFrame(dictionary)
        
        end_station_delay = model.predict(input_data)
        try: 
            delay = delay_at_input_stations + end_station_delay[0].tolist()
        except:
            delay = delay_at_input_stations + end_station_delay.tolist()
        
        delays.append(delay)
        
        s = s + 1
        
    i = i + 1
    e = e + 1
```

# Validation with external data

```python
# Validation with external data (continue):
result = []
a = 0
c = 0
d = 0
e = 0
f = 0
t = 0

for data in range(0,len(stations) * len(data_test_float)):
    dictionary_res = {}
    dictionary_res['station'] = stations[c]    
    t = f
    for fore in range(0, len(stations)-1):
        dictionary_res[stations[fore]] = delays[t][a]        
        t = t + len(data_test) 
    dictionary_res[stations[len(stations)-1]] = data_test_float[d][e]
    c = c + 1
    a = a + 1
    e = e + 1

    if c != len(stations):
        t = f
    if c == len(stations):
        c = 0      
        f = f + 1      
    if a == len(stations):
        a = 0 
    if e == len(stations):
        e = 0
        d = d + 1
    
    result.append(dictionary_res)

result_df = pd.DataFrame(result)
result_df_fin = result_df[result_df.station == stations[len(stations)-1]]
```

# Calculation of metrics for the validation part

```python
# Calculation of metrics for the validation part:
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
accuracy = []
# Assuming df is your DataFrame with 'predicted_data' and 'actual_data' columns
metrics = ['mae', 'mse', 'rmse', 'r2_score']
for m in range(0, len(stations)-1):
    
    predicted_data = result_df_fin[stations[m]]
    actual_data = result_df_fin[stations[len(stations)-1]]
    
    mae = mean_absolute_error(actual_data, predicted_data)
    mse = mean_squared_error(actual_data, predicted_data)
    rmse = np.sqrt(mse)
    r2_value = r2_score(actual_data, predicted_data)
    accuracy.append(mae)
    accuracy.append(mse)
    accuracy.append(rmse)
    accuracy.append(r2_value)
metrics_test_valid = []
n = 0

for metric in metrics:
    dictionary_metrics = {}
    dictionary_metrics['metric_valid'] = metrics[n]
    m = n
    l = 0
    for station in range(0, len(stations)-1):
        dictionary_metrics[stations[l]] = accuracy[m]
        l = l + 1
        m = m + 4
    metrics_test_valid.append(dictionary_metrics)
    n = n + 1
    
metrics_test_valid_df = pd.DataFrame(metrics_test_valid)
```

# Calculation of metrics for the test part

```python
metrics_test = []
n = 0
for metric in metrics:
    dictionary_metrics = {}
    dictionary_metrics['metric_test'] = metrics[n]
    m = n
    l = 0
    for station in range(0, len(stations)-1):
        dictionary_metrics[stations[l]] = accuracy_test[m]
        l = l + 1
        m = m + 4
    metrics_test.append(dictionary_metrics)
    n = n + 1
metrics_test_df = pd.DataFrame(metrics_test)
```



