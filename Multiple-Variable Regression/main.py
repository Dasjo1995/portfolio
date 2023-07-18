import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('NLSY97_subset.csv')

# -------------- Data Exploration
print(df_data.shape)
print(df_data.columns)
print(df_data.isna().values.any())
print(df_data.duplicated())
print(df_data.duplicated().values.any())

df_data_c = df_data.drop_duplicates()
df_data_c = df_data_c.fillna(0)

# -------------- Data Split into training and testing data

target = df_data_c.EARNINGS
features = df_data_c.drop('EARNINGS', axis=1)   # axis=1 indicates that you want to remove a column, not a row

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,  # here you set how much will remain for testing (20%)
                                                    random_state=10) # add this to get the same split every time

# --------------- If you only want a couple of variables for your regression:

df_data_c_Earn_S = df_data_c[['S', 'EARNINGS']]

target = df_data_c_Earn_S.EARNINGS
features = df_data_c_Earn_S.S

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,  # here you set how much will remain for testing (20%)
                                                    random_state=10) # add this to get the same random split every time

# --------------- If you only use one variable for the feature (explaining) variable, you need to reshape it to 2D:

# Since the X_train and x_test are one dimensional, we need to reshape them to two dimensions to be able to use them in the regression model
X_train = np.array(X_train).reshape(-1, 1)
X_test = np.array(X_test).reshape(-1, 1)

# --------------- Simple Linear Regression

regr = LinearRegression()               # Now you can use the training data to do a linear regression

regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)

print(rsquared)
print(regr.coef_)
print(regr.intercept_)

# ---------------- Multivariate Linear Regression

regr = LinearRegression()

regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)

regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient']) # Here you get a list of the
# coefficients for all feature variables

print(regr.intercept_)
print(regr_coef)
print(rsquared)

# ---------------- Investigate Residuals

predicted_values = regr.predict(X_train)    # This is used to make a line-scatter plot of the linear regression
residuals = (y_train - predicted_values)

plt.figure(dpi=100)
plt.scatter(x=predicted_values, y=residuals, c='indigo', alpha=0.6)   # Here you create a plot of residuals, should look
plt.title('Residuals vs Predicted Values', fontsize=17)             # random.
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()