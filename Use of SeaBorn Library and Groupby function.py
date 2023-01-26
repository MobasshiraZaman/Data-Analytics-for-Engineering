# Lecture 9
# Mobasshira Zaman
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
diamonds= pd.read_csv(r'data/diamonds.csv')
diamonds= diamonds.drop(columns = ['Unnamed: 0'])
print(diamonds.columns)
print(diamonds.head())
print(diamonds.info())

# Bar plot: Clarity
diamonds.groupby(['clarity']).size().plot(kind='bar')
plt.title('Bar plot of Clarity')
plt.ylabel('Count')
plt.show()

diamonds.groupby(['clarity','color']).size().unstack().plot(kind='bar',stacked= True)
plt.title('Stacked Bar Plot with Clarity and Color')
#plt.ylabel('Count')
plt.savefig('test save fig.jpg')
plt.show()
diamonds['carat'].hist()
plt.show()


# seaborn package
iris= pd.read_csv(r'data/iris.csv')
iris= iris.drop(columns= ['Unnamed: 0'])
sb.pairplot(data=iris, hue= 'species')
plt.show()
sb.pairplot(data=iris)
plt.show()

this_data = sb.load_dataset("mpg")


