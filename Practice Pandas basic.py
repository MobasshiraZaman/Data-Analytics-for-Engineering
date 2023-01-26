# Module 4 Practice Exercise
# Mobasshira Zaman
# 9/15/2022
from rdatasets import data
DocCont = data(package="Ecdat", item="DoctorContacts")
print(DocCont.info())
# print(DocCont.describe())
# Answers for Question 1
# 1 (a) : The dataset contains information of contact with medical doctors or demand for medical care.
# 1 (b) : There should be 20186 observations.
# 1 (c) : There are 15 columns.
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answers for Question 1:')
print('1 (a) : The dataset contains information of contact with medical doctors or demand for medical care.')
print('1 (b) : There should be 20186 observations.')
print('1 (c) : There are 15 columns.')
# Answers for Question 2
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answers for Question 2:')
DocCont_Original_Col_Name = DocCont.columns
print('The given column names of the dataset is: ', DocCont_Original_Col_Name)
# Alternative Way
DocCont_Original_Col_Name_Alt = list(DocCont.columns)
print('The given column manes of the dataset in a list form is: ', DocCont_Original_Col_Name_Alt)
# Replace with new column names
New_Columns =['#OutpatientVisit', 'CoinsuranceRate' , 'IndividualDeductPlan' , 'LogAnnualIncentivePay', 'LogMaxDeductExpend', 'PhysicalLimit' ,'#ChronicDiseases' , 'SelfRateHealth' , 'LogAnnualFamilyIncome' , 'LogFamilySize' ,'YearsOfSchoolingOfHouseholdHead' ,'ExactAge' , 'Sex' , 'AgeLessThan18' ,'HouseholdHeadBlack']
DocCont.columns = New_Columns
print(DocCont.columns)
# Answer for Question 3
# 3 (a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(a): ')
print(DocCont.info())
# From the console the following information was found:
# RangeIndex: 20186 entries, 0 to 20185
# Data columns (total 15 columns):
# Which means there are 20186 rows and 15 columns.
print('Number of Columns of the dataset: ', len(DocCont.columns))
print('Number of Columns of the dataset: ', len(DocCont))
DataTypeFromInfo = DocCont.dtypes
print('List of datatypes of all columns:', DataTypeFromInfo)
#  3 (b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(b): ')
int_col = DocCont.dtypes[DocCont.dtypes == 'int64'].index.values.tolist()
print('Columns that have an integer datatype: ', int_col)
print('Number of columns that have integer datatype: ', len(int_col))
# 3 (c)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(c): ')
flt_col= DocCont.dtypes[DocCont.dtypes == 'float64'].index.values.tolist()
print('Columns that have float datatype: ', flt_col)
print('Number of columns that have float datatype: ', len(flt_col))
# 3 (d)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(d): ')
str_col= DocCont.dtypes[DocCont.dtypes == 'object'].index.values.tolist()
print('Columns that might have string datatype: ', str_col)
print('Number of columns that might have string datatype: ', len(str_col))
# 3 (e)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(e): ')
bool_col= DocCont.dtypes[DocCont.dtypes == 'bool'].index.values.tolist()
print('Columns that have boolean datatype: ', bool_col)
print('Number of columns that have boolean datatype: ', len(bool_col))
# 3 (f)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(f): ')
print('The data type for health or self rate health is: ',DocCont['SelfRateHealth'].dtypes)
# 3 (g)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 3(g): ')
isNA_Vals = DocCont.isna()
tot_num_NAs_Per_Col = isNA_Vals.sum()
print('Number of total NA values per columns:\n',tot_num_NAs_Per_Col)
Name_Col_With_Null = tot_num_NAs_Per_Col[tot_num_NAs_Per_Col > 0].index.values.tolist()
if len(Name_Col_With_Null) > 0:
    print('Name of columns which have null or missing value: ', Name_Col_With_Null)
else:
    print('There is no columns which has null or missing value')
# 4 (a)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 4(a): ')
print('Descriptive Statistics of number of outpatient visits to a medical doctor:\n',DocCont['#OutpatientVisit'].describe())
Descrip_OutpatientVisit = DocCont['#OutpatientVisit'].describe()
print('Mean and standard deviation for the column representing the number of outpatient visit to a medical doctor:','\nMean:' , Descrip_OutpatientVisit['mean'], '\nStandard Deviation:',Descrip_OutpatientVisit['std'])
# 4 (b)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 4(b): ')
print('Descriptive Statistics of exact age column:\n', DocCont['ExactAge'].describe())
Descrip_Age = DocCont['ExactAge'].describe()
print('Percentile values for the age column:','\n25th percentile:' , Descrip_Age['25%'], '\n50th percentile:' , Descrip_Age['50%'],'\n75th percentile:' , Descrip_Age['75%'])
#i=0
#Cardinality_for_Each_Col = []
#if i < 15:
 #   ind = New_Columns[i]
  #  Cardinality_for_Each_Col_add = DocCont[ind].nunique()
   # Cardinality_for_Each_Col.append(Cardinality_for_Each_Col_add)
    #i=i+1
#print(Cardinality_for_Each_Col_add)
#5
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 5: ')
i=0
temp_list_for_ind= list(range(0,15))
Dict_for_Cardinality_each_col = dict()
Cardinality_for_Each_Col= []
for i in temp_list_for_ind:
    Cardinality_for_Each_Col.append(DocCont[New_Columns[i]].nunique())
    i=i+1
print("Cardinality of each column list: ",Cardinality_for_Each_Col)
Dict_for_Cardinality_each_col = dict(zip(New_Columns, Cardinality_for_Each_Col))
print('Cardinality for every column in data frame:', '\n',Dict_for_Cardinality_each_col)
print('5 (a)')
Max_Cardinality = max(Cardinality_for_Each_Col)
Max_Cardinality_Col = list(Dict_for_Cardinality_each_col.keys())[list(Dict_for_Cardinality_each_col.values()).index(Max_Cardinality)]
print('The column which has the largest cardinality is', Max_Cardinality_Col, 'with', Max_Cardinality, 'unique components.')
print('5 (b)')
Min_Cardinality = min(Cardinality_for_Each_Col)
list_Min_Cardinality= [k for k, v in Dict_for_Cardinality_each_col.items() if v== Min_Cardinality]
print('The columns which have the lowest cardinality are:', list_Min_Cardinality, '; with', Min_Cardinality, 'unique components.')
# 6
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 6: ')
print('Number of NA values for each column in given data frame:', '\n',DocCont.isna().sum())
# ALTERNATIVE
i=0
temp_list_for_ind= list(range(0,15))
Dict_for_NA_each_col = dict()
NA_for_Each_Col= []
for i in temp_list_for_ind:
    NA_for_Each_Col.append(DocCont[New_Columns[i]].isna().sum())
    i=i+1
print(NA_for_Each_Col)
Dict_for_NA_each_col = dict(zip(New_Columns, NA_for_Each_Col))
print('Number of NA values for each column in given data frame:', '\n',Dict_for_NA_each_col)
# 7
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 7: ')
print('Number of NA values for entire data frame:', '\n',DocCont.isna().sum().sum())
# 8
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 8: ')
Num_of_Values_For_Each_Sex = DocCont['Sex'].value_counts()
print('Number of values for each unique value for column Sex: \n', Num_of_Values_For_Each_Sex)
# 9
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 9: ')
Num_of_Values_For_Each_Health = DocCont['SelfRateHealth'].value_counts()
print('Number of values for each unique value for column Health: \n', Num_of_Values_For_Each_Health)
print('Number of patients said they are of good health: ', Num_of_Values_For_Each_Health['good'])
print('Number of patients said they are of excellent health: ', Num_of_Values_For_Each_Health['excellent'])
GoodorExcel= Num_of_Values_For_Each_Health['good']+Num_of_Values_For_Each_Health['excellent']
print('Number of patients said they are of good or excellent health: ', GoodorExcel)
#10
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Answer for Question 10: ')
AgeLessThan18= list(DocCont['AgeLessThan18'])
Condition_Count_AgeLessThan18 = AgeLessThan18.count(True)
print("Count of true false: \n",DocCont['AgeLessThan18'].value_counts())
print('Number of records for patients that are below 18 years old: ', Condition_Count_AgeLessThan18)





