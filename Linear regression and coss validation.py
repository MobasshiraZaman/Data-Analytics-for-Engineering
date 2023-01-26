# Module 10 Lecture
# Linear regression and coss validation
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import random
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score



# dataset
this_data = sb.load_dataset("mpg")
this_data.drop(columns= ['model_year', 'origin', 'name'], inplace= True)
# drop NA
this_data.dropna(inplace= True)

#split data into test set and for cv
#radomly gereratre zeros and ones to split
# 0 will be for test set (20%)
# 1 will be for cv (80%)
#np.random.seed(31) # for debugging purposes #TODO co
# mmand out later
split_indices= np.random.choice(2, size= len(this_data),  p=[0.2,0.8])
test_set= this_data.loc[split_indices==0]
for_cv= this_data.loc[split_indices==1]

#houdout set approach (validation set approach)
max_iteration= 100
metrics_list=[]
for i in range(1, max_iteration+1):
    print('Iteration', i)
    # split data again for 1) to train the model/ training dataset 2) validation dataset
    split_data= np.random.choice(2, size= len(for_cv), p=[0.5,0.5])
    train_set=  for_cv.loc[split_data==0 ]
    validation_set = for_cv.loc[split_data==1]
    train_set_x= train_set.drop(columns=['mpg'])
    train_set_y = train_set['mpg']
    validation_set_x = validation_set.drop( columns= ['mpg'])
    validation_set_y = validation_set['mpg']
    # set up regression model
    lr_model = LinearRegression().fit(X= train_set_x, y= train_set_y)
    # evaluate the model validation set
    predictions = lr_model.predict(validation_set_x)
    this_mse= mean_squared_error(y_true=validation_set_y, y_pred=predictions)
    this_r2 = r2_score(y_true=validation_set_y, y_pred=predictions)
    print('mse', this_mse)
    print('r2_score', this_r2)
    temp_dict= {'iteration':i,
                'MSE': this_mse,
                'r2': this_r2}
    metrics_list.append(temp_dict)
metrics_df = pd.DataFrame(metrics_list)
print(metrics_df)
print('=======cross validation results=====')
print(metrics_df.drop(columns= ['iteration']).mean())

# predict the set
to_fit_x= for_cv.drop(columns= ['mpg'])
to_fit_y= for_cv['mpg']
final_lr_model= LinearRegression().fit(X=to_fit_x, y= to_fit_y)
test_predict= final_lr_model.predict(test_set.drop(columns= ['mpg']))
test_mse= mean_squared_error(y_true=test_set['mpg'], y_pred=test_predict)
test_r2= r2_score(y_true=test_set['mpg'], y_pred=test_predict)
print('test set mse', test_mse)
print('test set r2', test_r2)


#graphing result
metrics_df.plot(kind='line',x='iteration',y=['MSE'])
plt.hlines(y=test_mse, label= 'Test MSE', xmin= 1, xmax=max_iteration, colors= 'r')
plt.title('MSE per iteration')
plt.ylim(bottom=0)
plt.show()
metrics_df.plot(kind='line',x='iteration',y=['r2'])
plt.hlines(y=test_r2, label= 'Test R2', xmin= 1, xmax=max_iteration, colors= 'r')
plt.title('r2 per iteration')
plt.xlabel('Iteration #')
plt.ylabel('r2 value')
plt.ylim(bottom=0, top=1)
plt.show()


