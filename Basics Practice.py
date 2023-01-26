# Module 5 Homework 1
# Mobasshira Zaman
# 09/20/2022
import pandas as pd
# Importing local file and saving as a dataframe
college_distance_data = pd.read_csv(r'data/CollegeDistance.csv')
# 1 (a)
# One row/ record of the data represents 1 student's information.
# 1 (b)
# There are 14 columns in the given data.
# Each or the columns stores different attribute about students. The information each columns stores are described below:
# gender: The gender of the student.
# ethnicity: The ethnicity or cultual of the student is stored in this columns. The contents were either Hispanic (hispanic), African-American (afam) or other.
# score: The student's composite test score of base year is stored in this column.
# fcollege: The student's father educational background (whether the father of the student is college graduate or not)
# mcollege: The student's mother educational background (whether the mother of the student is college graduate or not)
# home: Stored yes or no answer for about whether family of the student owns a home or not.
# urban: Stored yes or no answer for about whether family of the student's affiliated school is in urban area or not.
# unemp: Unemployment rate of the country in 1980 from where the student is attending the educational institution.
# wage: The per hour wage rate of the state in 1980 from where the student is attending the educational institution.
# distance: The distance from the student's home to 4-year college and it's stored as ten miles unit. Meaning real distance is 10 times the stored values.
# tuition: The average college tuition of the 4-year college where the student is studying. the values are stored as 1000 in USD. Meaning real value is 1000 times the stored values.
# education: Number of years the student is admitted to educational institution.
# income: Answer as high or low taking income threshold as 25000 per year for the student's family.
# region: Answering is the student is from west region or other region.

# 2 (a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 2(a): ')
int_col = college_distance_data.dtypes[college_distance_data.dtypes == 'int64'].index.values.tolist()
print('Columns that have an integer datatype: ', int_col)
print('Number of columns that have integer datatype: ', len(int_col))
# 2 (b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 2(b): ')
str_col= college_distance_data.dtypes[college_distance_data.dtypes == 'object'].index.values.tolist()
print('Columns that might have string datatype: ', str_col)
print('Number of columns that might have string datatype: ', len(str_col))
#2 (c)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 2(c): ')
flt_col= college_distance_data.dtypes[college_distance_data.dtypes == 'float64'].index.values.tolist()
print('Columns that have float datatype: ', flt_col)
print('Number of columns that have float datatype: ', len(flt_col))
# 2 (d)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 2(d): ')
bool_col= college_distance_data.dtypes[college_distance_data.dtypes == 'bool'].index.values.tolist()
print('Columns that have boolean datatype: ', bool_col)
print('Number of columns that have boolean datatype: ', len(bool_col))

# 3 (a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(a): ')
Cardinality_for_Ethnicity_Col = college_distance_data['ethnicity'].nunique()
print('Cardinality for ethnicity column ', Cardinality_for_Ethnicity_Col)
# 3 (b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(b): ')
Cardinality_for_Score_Col = college_distance_data['score'].nunique()
print('Cardinality for score column ', Cardinality_for_Score_Col)
# 3 (c)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(c): ')
Cardinality_for_Education_Col = college_distance_data['education'].nunique()
print('Cardinality for education column ', Cardinality_for_Education_Col)
# 4
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 4: ')
# The column named as: fcollege, mcollege, home, urban should be formated as boolean type. Because these coulmn are giving yes no answer of a certain question which is string and if they wanted to store is as boolean data type they needed to store as True instead of yes and False instead of no.
print('The column named as: fcollege, mcollege, home, urban should be formated as boolean type. Because these coulmn are giving yes no answer of a certain question which is string and if they wanted to store is as boolean data type they needed to store as True instead of yes and False instead of no.')
# 5
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 5: ')
print('Number of NA values for each column in given data frame:', '\n',college_distance_data.isna().sum())
# 6 (a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 6(a): ')
Num_of_Values_For_Each_Gender = college_distance_data['gender'].value_counts()
print('Number of total values for each unique value of gender column: \n', Num_of_Values_For_Each_Gender)
# 6 (b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 6(b): ')
Num_of_Values_For_Each_Home = college_distance_data['home'].value_counts()
print('Number of total values for each unique value of home column: \n', Num_of_Values_For_Each_Home)
# 6 (c)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 6(c): ')
Num_of_Values_For_Each_fcollege = college_distance_data['fcollege'].value_counts()
print('Number of total values for each unique value of fcollege column: \n', Num_of_Values_For_Each_fcollege)
# 6 (d)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 6(d): ')
Num_of_Values_For_Each_mcollege = college_distance_data['mcollege'].value_counts()
print('Number of total values for each unique value of mcollege column: \n', Num_of_Values_For_Each_mcollege)
# 7(a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 7(a): ')
both_parents_c_grad= ((college_distance_data['fcollege']=='yes') & (college_distance_data['mcollege']=='yes'))
print('Both parents were college graduate: ', sum(both_parents_c_grad))
only_mother_c_grad= ((college_distance_data['fcollege']!='yes') & (college_distance_data['mcollege']=='yes'))
print('Only mother were college graduate: ', sum(only_mother_c_grad))
only_father_c_grad= ((college_distance_data['fcollege']=='yes') & (college_distance_data['mcollege']!='yes'))
print('Only father were college graduate: ', sum(only_father_c_grad))
neither_c_grad= ((college_distance_data['fcollege']!='yes') & (college_distance_data['mcollege']!='yes'))
print('Neither were college graduate: ', sum(neither_c_grad))
#Alternative:
grouped= college_distance_data.groupby(['fcollege', 'mcollege']).count()
#print(grouped.iloc[:,1])
print('Alternative: 7(a) with groupby function')
print('Both parents were college graduate: ',grouped.iloc[3,1], '\nOnly mother were college graduate: ', grouped.iloc[1,1],'\nOnly father were college graduate: ',grouped.iloc[2,1],'\nNeither were college graduate: ', grouped.iloc[0,1])
# 7(b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 7(b): ')
yes_home_filter= (college_distance_data['home']=='yes')
no_home_filter= (college_distance_data['home']=='no')
print('For home response yes average distance is: ', round(college_distance_data[yes_home_filter]['distance'].mean(), 3), '(in 10 miles) and for no average distance is: ', round(college_distance_data[no_home_filter]['distance'].mean(),3), '(in 10 miles)')
#Alternative:
grouped= college_distance_data.groupby(['home']).mean()
print('Alternative: 7(b) with groupby function average distance (in 10 miles):\n',round(grouped.loc[:,'distance'],3))
# 7 (c)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 7(c): ')
r_west_h_yes= ((college_distance_data['region']=='west')& (college_distance_data['home']=='yes'))
r_west_h_no= ((college_distance_data['region']=='west')& (college_distance_data['home']=='no'))
r_other_h_yes= ((college_distance_data['region']=='other')& (college_distance_data['home']=='yes'))
r_other_h_no= ((college_distance_data['region']=='other')& (college_distance_data['home']=='no'))
print('For region west and home yes combination tuition mean (in 1000 USD) is: ', round(college_distance_data[r_west_h_yes]['tuition'].mean(), 3))
print('For region west and home no combination tuition mean (in 1000 USD) is: ', round(college_distance_data[r_west_h_no]['tuition'].mean(), 3))
print('For region other and home yes combination tuition mean (in 1000 USD) is: ', round(college_distance_data[r_other_h_yes]['tuition'].mean(), 3))
print('For region other and home no combination tuition mean (in 1000 USD) is: ', round(college_distance_data[r_other_h_no]['tuition'].mean(), 3))
#Alternative:
grouped= college_distance_data.groupby(['region', 'home']).mean()
print('Alternative: \n7(c) with groupby function average tuition (in 1000 USD):\n', round(grouped.loc[:,'tuition'],3))

#print('For region west and home yes combination tuition mean is:', round(grouped.loc[3,'tuition'],3),'\nFor region west and home no combination tuition mean is:',round(grouped.loc[2,'tuition'],3),'\nFor region other and home yes combination tuition mean is:',round(grouped.loc[1,'tuition'],3),'\nFor region other and home no combination tuition mean is:',round(grouped.loc[0,'tuition'],3))
# 7(d)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 7(d): ')
high_income_filter= (college_distance_data['income']=='high')
low_income_filter= (college_distance_data['income']=='low')
print('For high income average wage is: ', round(college_distance_data[high_income_filter]['wage'].mean(), 3), 'and for low income average wage is: ', round(college_distance_data[low_income_filter]['wage'].mean(),3))
#Alternative:
grouped= college_distance_data.groupby(['income']).mean()
print('Alternative: 7(d) average wage with groupby function\n',round(grouped.loc[:,'wage'],3))
#8 (a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 8(a): ')
a_cond=[]
for x in college_distance_data['distance']:
 if x > 1:
    a_cond.append(x)
print('Number of students lived more_than_10 miles from 4-year college:', len(a_cond))
#8 (b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 8(b): ')
print('Number of students lived less than 10 miles from 4-year college and family had low income:', sum((college_distance_data['distance']<1) & (college_distance_data['income']=='low')))
#8 (c)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 8(c): ')
print('Number of students had both parents graduate from college and had high income levels', sum(((college_distance_data['fcollege']=='yes')&(college_distance_data['mcollege']=='yes')) & (college_distance_data['income']=='high')))




