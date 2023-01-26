#  Feature selection with correlation, entropy/ mutual information
# Mobasshira Zaman
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import seaborn as sb
from sklearn.feature_selection import mutual_info_classif

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




# Main program
# Import the Data
ad_data= pd.read_csv(r'Data/Advertising.csv')
ad_corr= ad_data.corr(method= 'pearson')
ad_pvalues= corr_pvalues(ad_data)
print('Ad Correlation:')
print(ad_corr)
print('Ad p_values:')
print(ad_pvalues)
# Visualize data
# heatmap of Correlation
# Colors Corespond to correlation
# text correponds to p values
sb.heatmap(ad_corr, xticklabels = ad_data.columns, yticklabels= ad_data.columns,
           cmap= 'RdBu', linewidths=0.5, annot= ad_pvalues)
plt.title('Correlation for Ad Data')
#plt.show()

# Makes a lower triangle matrix
mask= np.invert(np. tril(ad_pvalues< 0.05))
mask[np.diag_indices(4)]= True
#sb.heatmap(ad_corr, mask=mask, annot= ad_pvalues, cmap= "RdBu", linewidths=0.5, center=0)
sb.heatmap(ad_corr, mask=mask, annot= ad_corr, cmap= "RdBu", linewidths=0.5, center=0)
plt.title("Coorelation with p-values < 0.05")
#plt.show()

# Chi-square Test of Independence
arth_data= pd.read_csv(r"Data/Arthritis.csv")
cross_tab= pd.crosstab(arth_data['Treatment'], arth_data["Improved"])
print(cross_tab)
chi_sq= stats.chi2_contingency(cross_tab)
print("Chi_squared results:",chi_sq)
chi_sq_list= []
for thisCol in arth_data.columns: 
    if (thisCol != 'Improved'):
        cross_tab= pd.crosstab(arth_data[thisCol], arth_data["Improved"])
        chi_sq =stats.chi2_contingency(cross_tab)
        temp= {"Variable": thisCol, 
               "p_values": chi_sq[1]}
        chi_sq_list.append(temp)
chi_sq_results= pd.DataFrame(chi_sq_list)
print(chi_sq_results)


# Mutual Info
# Features must be numeric discrete
arth_mi= arth_data.copy(deep= True)
arth_mi.drop(columns= ["ID", "Age"], inplace=True)
#arth_mi["Treatment"].replace("Placebo", 0, inplace= True)
#arth_mi["Treatment"].replace("Treated", 1, inplace= True)
# for outer loop thru col
for thisCol in arth_mi.columns:
    # for each unique value of current col
    num_replace_with=0
    for thisVal in arth_mi[thisCol].unique():
        # replace values with number
        arth_mi[thisCol].replace(thisVal, num_replace_with, inplace=True)
        num_replace_with= num_replace_with+1

mi = mutual_info_classif(X= arth_mi.drop(columns=["Improved"]), y=arth_mi["Improved"],
                       discrete_features=True)
print("Mutual Info:",mi)
