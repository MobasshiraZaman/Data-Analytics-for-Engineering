# Module 12 Part 2
# Mobasshira Zaman
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE, RFECV
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

# Import data
raw_data= sb.load_dataset('mpg')
mpg_data= raw_data.drop(columns=['model_year', 'origin', 'name'])
mpg_data= mpg_data.dropna()
print('Columns are: ', mpg_data.columns)
# RFE - recursive feature elimination
LR= LinearRegression()
selector= RFE(estimator= LR, n_features_to_select= 2, step= 1)
selector.fit(X= mpg_data.drop(columns= ['mpg']), y= mpg_data['mpg'])
print(selector.ranking_)

rfecv_selector = RFECV(estimator= LR, step=1, cv= KFold(5), scoring= 'neg_mean_squared_error')
rfecv_selector.fit(X= mpg_data.drop(columns= ['mpg']), y= mpg_data['mpg'])

# plot
#plt.plot(range(1, len(rfecv_selector.cv_results_['mean_test_score'])+1), rfecv_selector.cv_results_['mean_test_score'])
plt.bar(range(1, len(rfecv_selector.cv_results_['mean_test_score'])+1), -rfecv_selector.cv_results_['mean_test_score'])
#plt.title('Neg MSE by # features')
#plt.xlabel('# features in model')
#plt.ylabel('Neg MSE')
#plt.show()
plt.title('MSE by # features')
plt.xlabel('# features in model')
plt.ylabel('MSE')
plt.show()

rfecv_selector = RFECV(estimator= LR, step=1, cv= KFold(5), scoring= 'r2')
rfecv_selector.fit(X= mpg_data.drop(columns= ['mpg']), y= mpg_data['mpg'])
plt.bar(range(1, len(rfecv_selector.cv_results_['mean_test_score'])+1), rfecv_selector.cv_results_['mean_test_score'])
plt.ylim(top=1)
plt.title('R2 by # features')
plt.xlabel('# features in model')
plt.ylabel('R2')
plt.show()