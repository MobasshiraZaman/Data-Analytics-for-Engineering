# Module 6
# Mobasshira
# Import packages
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
# read in iris data
iris= pd.read_csv(r"/Users/mobasshirazaman/Library/CloudStorage/OneDrive-NorthernIllinoisUniversity/Semester 4/ISYE 570/Python Project/data/iris.csv")
print(iris.head())
print(iris.info())
# drop unnamed column
# axis 1 for column and 0 for rows
print('=====After droping column======')
iris = iris.drop(columns=['Unnamed: 0'])
print(iris.head())

# pearson correlation
iris_pearson= iris.corr(method= 'pearson')
print(iris_pearson)
# plotting a heatmap for pearson correlation
ax = sb.heatmap(iris_pearson, cmap= 'RdBu', linewidths=0.5, annot= True, vmin= -1, vmax=1)
plt.title('Heatmap')
plt.show()

# colab
#plt.savefig('pearson heatmap iris save.png')
# from google.colab import files
# files.download('pearson heatmap iris save.png')

# read in titanic
titanic= pd.read_csv(r'data/titanic.csv')
print(titanic.head())
print(titanic.info())
print(titanic.isna().sum())
titanic_subset= titanic.filter(items= ["alone", 'deck', 'parch', 'sibsp', 'embarked'])
titanic_kendall= titanic_subset.corr(method= 'kendall')
print(titanic_kendall)
ax = sb.heatmap(titanic_kendall, cmap= 'PuOr', linewidths=0.5, annot= True, vmin= -1, vmax=1)
plt.title('Heatmap Kendall')
plt.show()

plt.figure(3)
t_s_spear= titanic.filter(items= ["alone", 'adult_male'])
titanic_spearman= t_s_spear.corr(method= 'spearman')
ax1 = sb.heatmap(titanic_spearman, cmap= 'Oranges', linewidths=0.5, annot= True, vmin= -1, vmax=1)
plt.title('Heatmap Spearman')
plt.show()








