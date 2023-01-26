# Fall 2022- ISYE 570: Module 4 Pandas Basics
# Mobasshira Zaman
# Z_ID: Z1934124
# This code was done in Mac.
# Only difference is in the line of importing data from device.
# 'r' was before the location of the file.
# in colab : !pip install rdatasets. Here line number 26.

from rdatasets import data
import pandas as pd

this_data = data(package="MASS", item="crabs")
print(this_data.info())
print(this_data.describe())
new_columns =['species', 'sex', 'index', 'frontal lobe', 'rear width', 'carapace length', 'carapace width', 'body depth']
this_data.columns = new_columns
print(this_data.columns)

# Get data in colab from device:
# Left side there is icon for files and then on top upload
# Can be done from drive by copying in drive and then using the drive icon

# Importing local file and saving as a dataframe
film_data = pd.read_csv(r'data/Film_Locations_in_San_Francisco.csv')
# For europe data
film_data_eu = pd.read_csv(r'data/Film_Locations_in_San_Francisco_eu.csv', sep = ';')
print(film_data.info())

# Identifying NA and missing values
# .isna() ask if the cell is null or not
# So .sum() is  needed to know the number of total NA values
isNA_Vals = film_data.isna()
tot_num_NAs_Per_Col = isNA_Vals.sum()
print('Number of total NA values per columns: ', tot_num_NAs_Per_Col)
tot_num_NAs= tot_num_NAs_Per_Col.sum()
print('Number of total NA values: ', tot_num_NAs)

# Doing this all-in-one line
print('Number of total NA values: ', film_data.isna().sum().sum())

# value in the 1000 index for Actor 1
print('Actor in the 1000th index: ', film_data['Actor 1'].iloc[1000])

# Number of unique values
print('Number of unique film titles: ', film_data['Title'].nunique())
print('List of unique film titles: ', film_data['Title'].unique())

# Drop duplicates

print('=================Drop Duplicates================')
film_data_drop_dup = film_data.drop_duplicates()
print(film_data_drop_dup.info())
print('===========Drop Duplicate (Title Column)===========')
film_data_title_drop_dup = film_data['Title'].drop_duplicates()
print(film_data_title_drop_dup)
print(film_data_title_drop_dup.info())

print("===========value counts per title========")
print(film_data_drop_dup['Title'].value_counts())
print("===========value counts per release year========")
print(film_data_drop_dup['Release Year'].value_counts())

print('==========Create a Subset dataframe for Only Ant-Man Film Locations=======')
ant_man_TF = film_data_drop_dup['Title'] == 'Ant-Man'
ant_man_data = film_data_drop_dup.loc[ant_man_TF, :]
print(ant_man_data.info())
print('====== number of rows for locations/actors/title combo for films in or before 2000=====')
before_2000_TF = film_data_drop_dup['Release Year'] <= 2000
before_2000_df = film_data_drop_dup.loc[before_2000_TF, :]
print(before_2000_df.info())

