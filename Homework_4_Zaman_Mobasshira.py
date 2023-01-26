# Homework 4
# Mobasshira Zaman

import pandas as pd
from scipy import stats
import seaborn as sb
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder



raw_data= pd.read_csv('data/secondary_data.csv', sep= ';')
to_drop = ['cap-surface', 'gill-attachment', 'gill-spacing', 'stem-root', 'stem-surface', 'veil-type', 'veil-color',
           'ring-type', 'spore-print-color']
raw_data.drop(columns=to_drop, inplace=True)

cap_diam_bins = [0, 3.48, 5.86, 8.54, 62.34]
cap_diam_labels = ['small', 'medium', 'large', 'extra large']
raw_data['cap-diameter'] = pd.cut(raw_data['cap-diameter'], bins=cap_diam_bins, labels=cap_diam_labels)

stem_height_bins = [0, 4.64, 5.95, 7.74, 33.92]
stem_height_labels = ['small', 'medium', 'large', 'extra large']
raw_data['stem-height'] = pd.cut(raw_data['stem-height'], bins=stem_height_bins, labels=stem_height_labels)

stem_width_bins = [0, 5.21, 10.19, 10.57, 103.91]
stem_width_labels = ['small', 'medium', 'large', 'extra large']
raw_data['stem-width'] = pd.cut(raw_data['stem-width'], bins=stem_width_bins, labels=stem_width_labels)

raw_data.dropna(inplace=True)

print(raw_data.head())
encoder1= LabelEncoder()
encoder2= LabelEncoder()
encoder3= LabelEncoder()
encoder4= LabelEncoder()
encoder5= LabelEncoder()
encoder6= LabelEncoder()
encoder7= LabelEncoder()
encoder8= LabelEncoder()
encoder9= LabelEncoder()
encoder10= LabelEncoder()
encoder11= LabelEncoder()
raw_data['cap-diameter']= encoder1.fit_transform(raw_data['cap-diameter'])
raw_data['cap-shape']= encoder2.fit_transform(raw_data['cap-shape'])
raw_data['cap-color']= encoder3.fit_transform(raw_data['cap-color'])
raw_data['does-bruise-or-bleed']= encoder4.fit_transform(raw_data['does-bruise-or-bleed'])
raw_data['gill-color']= encoder5.fit_transform(raw_data['gill-color'])
raw_data['stem-height']= encoder6.fit_transform(raw_data['stem-height'])
raw_data['stem-width']= encoder7.fit_transform(raw_data['stem-width'])
raw_data['stem-color']= encoder8.fit_transform(raw_data['stem-color'])
raw_data['has-ring']= encoder9.fit_transform(raw_data['has-ring'])
raw_data['habitat']= encoder10.fit_transform(raw_data['habitat'])
raw_data['season']= encoder11.fit_transform(raw_data['season'])
print(raw_data.head())
# 1
raw_for_kendall= raw_data.__deepcopy__()
encoder12= LabelEncoder()
raw_for_kendall['class']= encoder12.fit_transform(raw_for_kendall['class'])
raw_data_kendall= raw_for_kendall.corr(method= 'kendall')
print(raw_data_kendall['class'][1:])
#alternative
cols_picked= ['cap-diameter', 'cap-shape','cap-color', 'does-bruise-or-bleed', 'gill-color','stem-height', 'stem-width', 'stem-color', 'has-ring', 'habitat', 'season']
corr_list = []
list=[]
l = len(cols_picked)
for j in range(0, l):
        print(j+1,":")
        print('variable 1 is: class')
        print('variable 2 is: ', cols_picked[j])
        tau,p =stats.kendalltau(raw_for_kendall['class'], raw_for_kendall[cols_picked[j]], nan_policy='omit')
        print("Tau is:", tau)
        print("p value is: ", p)
        if p< 0.05:
            list.append(cols_picked[j])
        temp_dict = {
            "variable 1": 'class',
            'variable 2': cols_picked[j],
            'Kendall correlation value': tau,
            'p value': p
        }
        corr_list.append(temp_dict)
print(list)
temp_df= pd.DataFrame(corr_list)
print(temp_df.head())
temp_df= temp_df.sort_values('p value')
print(temp_df.head())


# 2
X_train = OrdinalEncoder().fit_transform(raw_data.drop(columns=['class']))
def cv_model(X_train, y_train, num_splits= 5, num_repeats= 20, rand_state= 368):
    results= []
    iter= 1
    fold=1
    rkf= RepeatedStratifiedKFold(n_splits= num_splits,n_repeats= num_repeats, random_state= rand_state)
    for train_index, valid_index in rkf.split(X_train,y_train):
        train_X, validate_X= X_train.iloc[train_index], X_train.iloc[valid_index]
        train_y, validate_y= y_train.iloc[train_index], y_train.iloc[valid_index]
        nb_model= CategoricalNB()
        nb_model.fit(X= train_X, y= train_y)

        # evaluate
        predictions= nb_model.predict(validate_X)
        accuracy = sum(predictions == validate_y) / len(validate_y)
        results.append({'iteration': iter,
                        'fold': fold,
                        'accuracy': accuracy})
        if fold == num_splits:
            fold = 1
            iter = iter + 1
        else:
            fold = fold + 1
    results_df = pd.DataFrame(results)
    return results_df


#split the dataset into training and test data
X_train, X_test, y_train, y_test= train_test_split(raw_data.drop(columns= ['class']), raw_data['class'], test_size= 0.25, random_state =368)

# Build model A:
# perform repeated k-fold cv
X_trainA= X_train
X_testA= X_test
y_trainA= y_train
resultsA= cv_model(X_trainA, y_train, num_splits=2, num_repeats=20, rand_state=368)
# Build model B:
temp_df_not_best_5= temp_df['variable 2'][5:]
columns_to_drop_B= ['has-ring','cap-color','gill-color','stem-color','habitat','does-bruise-or-bleed']
X_trainB= X_train.drop(columns= columns_to_drop_B)
X_testB= X_test.drop(columns= columns_to_drop_B)
# perform repeated k-fold cv
resultsB= cv_model(X_trainB, y_train, num_splits=2, num_repeats=20, rand_state=368)

# 4. test set analysis
# final model A
nb_modelA= CategoricalNB()
nb_modelA.fit(X= X_trainA, y= y_train)
predictions= nb_modelA.predict(X_testA)
accuracyA = sum(predictions == y_test) / len(y_test)
print('Test data performance: Model A')
print('Accuracy:', accuracyA)
# final model B
nb_modelB= CategoricalNB()
nb_modelB.fit(X= X_trainB, y= y_train)
predictions= nb_modelB.predict(X_testB)
accuracyB = sum(predictions == y_test) / len(y_test)
print('Test data performance: Model B')
print('Accuracy:', accuracyB)

# 3. plot results
print(resultsA.groupby(by=['iteration']).mean(),resultsB.groupby(['iteration']).mean())
resultsA.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'accuracy')
plt.hlines(y=accuracyA, label= 'TestSet Accuracy', xmin= 1, xmax=20, colors= 'r')
plt.ylim(bottom=0.6,top=0.7)
plt.title('Model A: Accuracy')
plt.show()

resultsB.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'accuracy')
plt.hlines(y=accuracyB, label= 'TestSet Accuracy', xmin= 1, xmax=20, colors= 'r')
plt.ylim(bottom=0.6,top=0.7)
plt.title('Model B: Accuracy')
plt.show()

ax= resultsA.groupby(['iteration']).mean().reset_index().plot(kind= 'line', x= 'iteration', y= 'accuracy', label= 'Model A')
resultsB.groupby(['iteration']).mean().reset_index().plot(ax= ax, kind= 'line', x= 'iteration', y= 'accuracy', label= 'Model B')
plt.ylim(bottom=0, top=1)
plt.legend()
plt.title('Model A and B: Accuracy for training data')
plt.show()
