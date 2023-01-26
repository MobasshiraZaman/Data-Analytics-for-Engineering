# Module 13
# Mobasshira Zaman
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split


raw_data= pd.read_csv(r"data/titanic.csv")
raw_data.drop(columns= ['deck', 'embark_town','fare', 'age', 'class', 'sex', 'alive', 'embarked'], inplace= True)

titanic= raw_data.__deepcopy__()
print(titanic.info())

encoder= OrdinalEncoder()
data_transfrom= encoder.fit_transform(titanic)
titanic= pd.DataFrame(data_transfrom, columns= raw_data.columns)

X_train, X_test, y_train, y_test = train_test_split(titanic.drop(columns=['survived']), titanic['survived'],
                                                    test_size= 0.15, stratify=titanic['survived'])

# Create the model
nb_model= CategoricalNB()


# Fit data to the model
nb_model.fit(X_train, y_train)


# Predict the test set
predictions= nb_model.predict(X_test)

accuracy= sum(predictions== y_test)/ len(y_test)
print('Accuracy: ', accuracy)

TP= np.logical_and(y_test== 1, predictions== 1).sum()
TN= np.logical_and(y_test== 0, predictions== 0).sum()
FP= np.logical_and(y_test== 0, predictions== 1).sum()
FN= np.logical_and(y_test== 1, predictions== 0).sum()
print('TP and TN: ', TP, "",TN)
print("FP and FN: ", FP, "",FN)









