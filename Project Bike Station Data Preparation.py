
# ISYE 570 Project 1.
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sb
from matplotlib import pyplot as plt

# Merging the 8 csv files
y20_q1= pd.read_csv('Project data/metro-trips-2020-q1.csv')
y20_q2= pd.read_csv('Project data/metro-trips-2020-q2.csv')
y20_q3= pd.read_csv('Project data/metro-trips-2020-q3.csv')
y20_q4= pd.read_csv('Project data/metro-trips-2020-q4.csv')
y21_q1= pd.read_csv('Project data/metro-trips-2021-q1.csv')
y21_q2= pd.read_csv('Project data/metro-trips-2021-q2.csv')
y21_q3= pd.read_csv('Project data/metro-trips-2021-q3.csv')
y21_q4= pd.read_csv('Project data/metro-trips-2021-q4.csv')
quarter_data = [y20_q1, y20_q2, y20_q3, y20_q4, y21_q1, y21_q2, y21_q3, y21_q4]
trip = pd.concat(quarter_data)


# Observation of merged dataframe
print('Primary data info:',trip.info())
print("Columns:",trip.columns)
print("Null values:",trip.isna().sum())

#split date and time into seperate columns
trip['Start_Dates'] = pd.to_datetime(trip['start_time']).dt.date
trip['Start_Time'] = pd.to_datetime(trip['start_time']).dt.time
trip['End_Dates'] = pd.to_datetime(trip['end_time']).dt.date
trip['End_Time'] = pd.to_datetime(trip['end_time']).dt.time
trip['start_month'] = pd.DatetimeIndex(trip['Start_Dates']).month
trip['end_month'] = pd.DatetimeIndex(trip['End_Dates']).month

# Bike ID Variable observation
bike_id_cardinality= trip['bike_id'].nunique()
print('cardinality:' ,trip['bike_id'].value_counts())
bike_id_str= ['16015a', '15111a', '15229a', '15241b', '_Test_RFID', 'TBlocker_Slash', '15902a', '16116a', '16257a']
print("========================================================================")

# Modify data for bike id column for ID errors (typo a,b, test RFID)
trip['bike_id']= trip['bike_id'].replace('_Test_RFID', np.nan)
trip['bike_id']= trip['bike_id'].replace('TBlocker_Slash', np.nan)
trip['bike_id']= trip['bike_id'].replace('16015a', '16015')
trip['bike_id']= trip['bike_id'].replace('15111a', '15111')
trip['bike_id']= trip['bike_id'].replace('15229a', '15229')
trip['bike_id']= trip['bike_id'].replace('15241b', '15241')
trip['bike_id']= trip['bike_id'].replace('15902a', '15902')
trip['bike_id']= trip['bike_id'].replace('16116a', '16116')
trip['bike_id']= trip['bike_id'].replace('16257a', '16257')

# Drop old start and end columns
trip=trip.drop(columns=['start_time', 'end_time'])

# Drop start and end station names
trip=trip.drop(columns=['start station name', 'end station name'])

# Remove rows with test Bike ID
trip= trip.dropna(subset=['bike_id'])

# Correcting datatypes for tableau

convert_dict = {'trip_id': int,
                'duration': int,
                'start_station': int,
                'start_lat': float,
                'start_lon': float,
                'end_station': int,
                'end_lat': float,
                'end_lon': float,
                'bike_id': int,
                'plan_duration': int,
                'trip_route_category': str,
                'passholder_type': str,
                'bike_type': str
                }
trip= trip.astype(convert_dict)
print(trip.dtypes)


# drop duplicates only for trip ID
trip= trip.drop_duplicates(subset='trip_id', keep='first')
print('Modified data info:',trip.info())
print("Modified data null:",trip.isna().sum())

# Check plan type cardinality values, drop rows with testing
# in column then drop pass type column
print(trip['passholder_type'].value_counts)
trip['passholder_type']= trip['passholder_type'].replace('Testing', np.nan)
trip= trip.dropna(subset=['passholder_type'])
trip = trip.drop(trip[(trip['passholder_type'] == 'Testing')].index)
# Generate
trip.to_csv('Merged1.csv')



