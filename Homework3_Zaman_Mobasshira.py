# Homework 3
# Mobasshira Zaman
# 11/ 16/ 2022
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import seaborn as sb
from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import LinearRegression
import random
from sklearn.metrics import mean_squared_error,r2_score
# Answer 3
rwine= pd.read_csv(r'Data/winequality-red.csv',sep= ';')
rwine_corr= rwine.corr(method= 'pearson')['quality']
print('Red Wine Correlation:')
print(rwine_corr)
print('3a. Variables that appear to have posotive correlation with quality column:\n'
      'fixed acidity ,citric acid , residual sugar ,'
      'sulphates    ,alcohol . '
      '\nMoreover, the obvious positive correlation of 1 is present for quality column with quality column.')
print('3b. Variables that appear to have negative correlation with quality column:\n'
      'volatile acidity ,chlorides ,free sulfur dioxide  ,total sulfur dioxide ,density ,pH')
print('3c. I was able to determine correlation value with quality column with all other columns/ variables.')

#Answer 4
# User defined function
def corr_pvalues(df):
    # df: a daatfreame of data to calculate correlation values and pvalues for
    # assumes pearson correlation
    p_values = np.zeros((df.shape[1], df.shape[1]))
    for col in df.columns:
        for col2 in df.drop(col, axis=1).columns:
            _, p= stats.pearsonr(df[col], df[col2])
            p_values[df.columns.to_list().index(col),df.columns.to_list().index(col2)]= p
    return  p_values
rwine_pvalues= corr_pvalues(rwine)
print('p_values:')
print(rwine_pvalues)
rwine_all_corr= rwine.corr(method= 'pearson')
print('All correlations:',rwine_all_corr)
# Makes a lower triangle matrix
mask= np.invert(np. tril(rwine_pvalues< 0.05))
mask[np.diag_indices(12)]= True
sb.heatmap(rwine_all_corr, mask=mask, annot= rwine_all_corr, cmap= "RdBu", linewidths=0.5, center=0)
plt.title("Correlation with p-values < 0.05")
plt.show()


# Answer 5
#split data into test set and for cv
#radomly gereratre zeros and ones to split
# 0 will be for test set (15%)
# 1 will be for cv (85%)
#np.random.seed(31) # for debugging purposes #TODO co
# mmand out later
split_indices= np.random.choice(2, size= len(rwine),  p=[0.15,0.85])
test_set= rwine.loc[split_indices==0]
for_cv= rwine.loc[split_indices==1]

#houdout set approach (validation set approach)
max_iteration= 100
metrics_list=[]
for i in range(1, max_iteration+1):
    #print('Iteration', i)
    # split data again for 1) to train the model/ training dataset 2) validation dataset
    split_data= np.random.choice(2, size= len(for_cv), p=[0.75,0.25])
    train_set=  for_cv.loc[split_data==0 ]
    validation_set = for_cv.loc[split_data==1]
    train_set_x = train_set.drop(columns=['quality'])
    train_set_y = train_set['quality']
    validation_set_x = validation_set.drop(columns=['quality'])
    validation_set_y = validation_set['quality']
    # set up regression model
    lr_model = LinearRegression().fit(X=train_set_x, y=train_set_y)
    # evaluate the model validation set
    predictions = lr_model.predict(validation_set_x)
    this_mse = mean_squared_error(y_true=validation_set_y, y_pred=predictions)
    this_r2 = r2_score(y_true=validation_set_y, y_pred=predictions)
    #print('mse', this_mse)
    #print('r2_score', this_r2)
    temp_dict = {'iteration': i,
                 'MSE': this_mse,
                 'r2': this_r2}
    metrics_list.append(temp_dict)
metrics_df = pd.DataFrame(metrics_list)
print(metrics_df)
print('=======cross validation results=====')
print('5.1 b. Average MSE and R^2 over overall iteration:',metrics_df.drop(columns=['iteration']).mean())
print('5.1 c. Standard deviation of the MSE and R^2 over overall iteration:', metrics_df.drop(columns=['iteration']).std())

# predict the set for 5.2
print('5.2 ')
to_fit_x = for_cv.drop(columns=['quality'])
to_fit_y = for_cv['quality']
final_lr_model = LinearRegression().fit(X=to_fit_x, y=to_fit_y)
test_predict = final_lr_model.predict(test_set.drop(columns=['quality']))
test_mse = mean_squared_error(y_true=test_set['quality'], y_pred=test_predict)
test_r2 = r2_score(y_true=test_set['quality'], y_pred=test_predict)
print('test set mse', test_mse)
print('test set r2', test_r2)
print('Here average set MSE is lower than test MSE. Which is typical for this type of modeling. So, we can conclude this model'
      'is good.')
# graphing result for 5.1 c
metrics_df.plot(kind='line', x='iteration', y=['MSE'])
plt.hlines(y=test_mse, label='Test MSE', xmin=1, xmax=max_iteration, colors='r')
plt.title('5.1 a. MSE for each iteration')
plt.ylim(bottom=0)
plt.show()
metrics_df.plot(kind='line', x='iteration', y=['r2'])
plt.hlines(y=test_r2, label='Test R2', xmin=1, xmax=max_iteration, colors='r')
plt.title('r2 per iteration')
plt.xlabel('Iteration #')
plt.ylabel('r2 value')
plt.ylim(bottom=0, top=1)
plt.show()




