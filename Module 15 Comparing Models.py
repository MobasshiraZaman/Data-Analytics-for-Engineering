# Module 15
# Mobasshira Zaman
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, RepeatedKFold

def cv_model(X_train, y_train, num_splits= 5, num_repeats= 10, rand_state_kf= None):
    results= []
    iter= 1
    fold=1
    rkf= RepeatedKFold(n_splits= num_splits,n_repeats= num_repeats, random_state= rand_state_kf)
    for train_index, valid_index in rkf.split(X_train):
        train_X, validate_X= X_train.iloc[train_index], X_train.iloc[valid_index]
        train_y, validate_y= y_train.iloc[train_index], y_train.iloc[valid_index]
        lr_model= LinearRegression(fit_intercept=True).fit(X= train_X, y= train_y)

        # evaluate MSE and r2 and collect data
        y_pred= lr_model.predict(validate_X)
        mse= mean_squared_error(validate_y, y_pred)
        r2= r2_score(validate_y, y_pred)
        print(iter,fold)
        results.append({'iteration': iter,
                        'fold':fold,
                        'mse': mse,
                        'r2': r2})
        if fold== num_splits:
            fold=1
            iter= iter+1
        else:
            fold=fold+1
    results_df= pd.DataFrame(results)
    return results_df

# get dataset
rawdata= sb.load_dataset('mpg')
rawdata= rawdata.drop(columns= ['model_year', 'name', 'origin'])
rawdata= rawdata.dropna()

# split the dataset into training and test data
X_train, X_test, y_train, y_test= train_test_split(rawdata.drop(columns= ['mpg']), rawdata['mpg'], test_size= 0.10, random_state =7412)

# Build model A: only horsepower
columns_to_drop_A= ['cylinders', 'displacement', 'weight', 'acceleration']
X_trainA= X_train.drop(columns= columns_to_drop_A)
X_testA= X_test.drop(columns= columns_to_drop_A)

# perform repeated k-fold cv
resultsA= cv_model(X_trainA, y_train, num_splits=2, num_repeats=10, rand_state_kf=249)
# collect result of mse and r2


# Build model B: horsepower, acceleration, weight
columns_to_drop_B= ['cylinders', 'displacement']
X_trainB= X_train.drop(columns= columns_to_drop_B)
X_testB= X_test.drop(columns= columns_to_drop_B)
# perform repeated k-fold cv
resultsB= cv_model(X_trainB, y_train, num_splits=2, num_repeats=10, rand_state_kf=143)
# collect result of mse and r2


# plot results
print(resultsA.groupby(by=['iteration']).mean())
resultsA.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'mse')
plt.ylim(bottom=0)
plt.title('Model A: MSE')
plt.show()

resultsB.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'mse')
plt.ylim(bottom=0)
plt.title('Model B: MSE')
plt.show()

ax= resultsA.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'mse', label= 'Model A')
resultsB.groupby(['iteration']).mean().reset_index().plot(ax= ax, kind= 'line', x= 'iteration', y= 'mse', label= 'Model B')
plt.ylim(bottom=0)
plt.legend()
plt.title('Model A and B: MSE for training data')
plt.show()

ax= resultsA.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'r2', label= 'Model A')
resultsB.groupby(['iteration']).mean().reset_index().plot(ax= ax, kind= 'line', x= 'iteration', y= 'r2', label= 'Model B')
plt.ylim(bottom=0, top=1)
plt.legend()
plt.title('Model A and B: r2 for training data')
plt.show()

# test set analysis


# final model A
lr_modelA= LinearRegression(fit_intercept=True).fit(X= X_trainA, y= y_train)
y_predA= lr_modelA.predict(X_testA)
mseA= mean_squared_error(y_test, y_predA)
r2A= r2_score(y_test, y_predA)
print('Test data performance: Model A')
print('MSE:', mseA)
print('r2:', r2A)

# final model B
lr_modelB= LinearRegression(fit_intercept=True).fit(X= X_trainB, y= y_train)
y_predB= lr_modelB.predict(X_testB)
mseB= mean_squared_error(y_test, y_predB)
r2B= r2_score(y_test, y_predB)
print('Test data performance: Model B')
print('MSE:', mseB)
print('r2:', r2B)

