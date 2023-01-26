# Module 12
# Mobasshira Zaman
# import Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
# Import data
raw_data = pd.read_csv(r"data/play_tennis.csv")
print(raw_data.info())
play_tennis = raw_data.drop(columns=['day'])

# Create the classifier obejct
# Define the parameters for the model
dt_classifier= tree.DecisionTreeClassifier(criterion='entropy')

# Create training and test data
X = OrdinalEncoder().fit_transform(play_tennis.drop(columns=['play']))

# label encoder only on target variable
le= LabelEncoder()
y= le.fit_transform(play_tennis['play'])
class_names= le.classes_
X_train, X_test, y_train, y_test =  train_test_split(X,y, test_size= 0.25, random_state= 30, stratify=y)

# Fit the model to data
dt_classifier= dt_classifier.fit(X_train,y_train)

# Predict the test set
predictions= dt_classifier.predict(X_test)
number_accurate = sum(predictions== y_test)
print('Number accurate', number_accurate)
print('Percent accurate', number_accurate/len(predictions))
# Output result
# plot
tree.plot_tree(dt_classifier,feature_names=play_tennis.drop(columns='play').columns, class_names= class_names,
               filled=True)
plt.show()













