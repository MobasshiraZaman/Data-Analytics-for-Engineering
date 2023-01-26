# Module 7 Practice Exercise
# Mobasshira Zaman
# import packages
from rdatasets import data
import pandas as pd
from scipy import stats
# import data
com = data(package='Ecdat', item= 'Computers')
print(com.head())
print(com.info())
print('========1=======')
# 1
# (a) The dataset contains information about prices of personal computers from year 1993 to 1995 in the United States
# (b) There should be 6259 observations.
print('(a) The dataset contains information about prices of personal computers from year 1993 to 1995 in the United States.\n(b) There should be 6259 observations. \n(c) The variables that are categorical are: speed, hd, ram, screen,cd, hd, multi, ads, trend.\n Price can be considered under categorical variable, but we can also consider price as discrete variable or quantitive variable. Quantative data (discrete data) can sometimes take categorical form')
# 2
print('========2=======')
print("Number of total empty records: ", com.isna().sum().sum())
# 3
print('========3=======')
int_col= com.dtypes[com.dtypes == 'int64'].index.values.tolist()
print('3(a) Number of columns with integer datatype are', len(int_col), 'and they are: ', ', '.join(int_col))
str_col= com.dtypes[com.dtypes == 'object'].index.values.tolist()
print('3(b) Number of columns with integer datatype are', len(str_col), 'and they are: ', ', '.join(str_col))
# 4
print('========4=======')
print('4(a)')
print("Cardinality for each columns: \n",com.nunique())
print("4(b) cd, multi and premium has entry as yes and no for relevant questions which could had been given entry as boolean (True and False) instead, which made the columns' data type string rather than boolean.")
# 5
# 5(a) ordinal categorical variable: trend. We can consider it orderly in a temporal manner.
# 5(b) nominal categorical variable:  speed, hd, ram, screen, ads. Although these variables has certain value higher and lower but we can not consider them ordinal if those higher to lower values does not give us any orderly information. Price can be considered as nominal or discrete variable. Becasue over 6000 price data can be grouped into 808 types. However, the data is not completely describing any category but certain pc. Moreover, cd, multi and premium although indicating yes no answers these are categorizing the observation into having or not having a certain attribute, which is more like binary variable.
# 5(c) There are no columns with continuous data. However, price can be considered as discrete values or interval continuos variable.
print('========5=======')
print('5(a) ordinal categorical variable: trend. We can consider it orderly in a temporal manner. ')
print('5(b) nominal categorical variable:  speed, hd, ram, screen, ads. Although these variables has certain value higher and lower but we can not consider them ordinal if those higher to lower values does not give us any orderly information. Price can be considered as nominal or discrete variable. Becasue over 6000 price data can be grouped into 808 types. However, the data is not completely describing any category but certain pc. Moreover, cd, multi and premium although indicating yes no answers these are categorizing the observation into having or not having a certain attribute, which is more like binary variable ')
print('5(c) There are no columns with continuous data. However, price can be considered as discrete values or interspaced continuos variable.')
# 6
print('========6=======')
col = com.columns.values.tolist()
temp_list=[]
for i in (com.nunique() < 10):
    temp_list.append(str(i))
    if (str(i)) == 'True':
        print('"',str(col[len(temp_list)-1]),'"','column has cardinality less than 10 and number of observations for each unique value of column','"',str(col[len(temp_list)-1]), '"','is:\n',com[str(col[len(temp_list)-1])].value_counts().to_string())
# 7
print("======7=====")
print('7(a)')
corr_list = []
l = len(int_col)
for i in range(0,(l-1)):
    for j in range((i+1), l):
        r,p =stats.pearsonr(com[int_col[i]], com[int_col[j]])
        temp_dict={
            "variable 1": int_col[i],
            'variable 2': int_col[j],
            'Correlation value/Pearson r': r,
            'p-value': p
        }
        corr_list.append(temp_dict)
corr_p = pd.DataFrame(corr_list)
print('DataFrame: corr_p\n',corr_p,"\n")
corr_p.to_csv('Pearson_Correlation_results(Mobasshira_Zaman).csv')
print('7 (b)')
ind= 0
for i in corr_p['p-value']:
    if i < 0.05:
        print('DataFrame "corr_p" index', ind,': Variable',corr_p['variable 1'][ind],'and variable' ,corr_p['variable 2'][ind], 'pair has statistically significant value as p value is',corr_p['p-value'][ind])
    ind=ind+1
# 8
print("\n========================8=============================")
print('\n8(a)')
cont_table1= pd.crosstab(com['cd'], com["premium"], margins= False)
chi1, p1, dof1, expected1 = stats.chi2_contingency(cont_table1)
print('Chi square value: ', chi1)
print('p-value:', p1)
print('As for cd and premium variable pair p-value is less than 0.05 and Chi square value is high we can reject the null hypothesis in favor of alternative hypothesis. Which means these variables are not independent.')

print('\n8(b)')
cont_table2= pd.crosstab(com['speed'], com["premium"], margins= False)
chi2, p2, dof2, expected2 = stats.chi2_contingency(cont_table2)
print('Chi square value: ', chi2)
print('p-value:', p2)
print('As for speed and premium variable pair p-value is less than 0.05 and Chi square value is high we can reject the null hypothesis in favor of alternative hypothesis. Which means these variables are not independent.')
print('\n8(c)')
cont_table3= pd.crosstab(com['speed'], com["multi"], margins= False)
chi3, p3, dof3, expected3 = stats.chi2_contingency(cont_table3)
print('Chi square value: ', chi3)
print('p-value:', p3)
print('As for speed and multi variable pair p-value is less than 0.05 and Chi square value is high we can reject the null hypothesis in favor of alternative hypothesis. Which means these variables are not independent.')








