# Module 7
# Mobasshhira Zaman
import pandas as pd
from scipy import stats

# 7-3 SciPy Stats KendallTau
titanic= pd.read_csv("data/titanic.csv")
print(titanic.head())
print(titanic.info())
tau_corr, p_value= stats.kendalltau(titanic['survived'], titanic['age'], nan_policy='omit')
print('Kendall correlation values: ', round(tau_corr,3))
print("p-value", round(p_value,3))

# 7-4 & 7-5 for loop
print("=======7-4 & 7-5 for loop=======")
cols_picked= ['survived', 'pclass', 'age', 'fare','alone']
corr_list = []
l = len(cols_picked)
for i in range(0,(l-1)):
    print('variable 1 is : ', cols_picked[i])
    for j in range((i+1), l):
        print('variable 2 is: ', cols_picked[j])
        tau,p =stats.kendalltau(titanic[cols_picked[i]], titanic[cols_picked[j]], nan_policy='omit')
        print("Tau is:", tau)
        print("p value is: ", p)
        temp_dict={
            "variable 1": cols_picked[i],
            'variable 2': cols_picked[j],
            'Kendall correlation value': tau,
            'p value': p
        }
        corr_list.append(temp_dict)
corr_k= pd.DataFrame(corr_list)
print(corr_k)
corr_k.to_csv('Kendall_Correlation_results.csv')

# 7-6 Chi-Square Hypothesis
# Calculate Contingency Table
cont_table= pd.crosstab(titanic['survived'], titanic["pclass"], margins= False)
chi2, p, dof, expected = stats.chi2_contingency(cont_table)
print('Chi square value: ', chi2)
print('p value', p)
#  Null reject: Not independent

