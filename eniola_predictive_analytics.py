# -*- coding: utf-8 -*-
"""Eniola Predictive Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11xVFwNiV3yCGWOdV2HSjHWeQaViDzI3N
"""

import numpy as np
import os
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import seaborn as sns
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

#import dataset
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/sales_data.csv')

#descriptive statistics
data.head()

data.columns

data.describe()

#include columns with object data type
data.describe(include=['object'])

data.info()

data[(data['gender'] == 'F') & (data['flag'] == 'Y')]

data["flag"].value_counts()

data["education"].value_counts()

data["occupation"].value_counts()

data["region"].value_counts()

data["marriage"].value_counts()

data.education.value_counts().plot.barh()

data.region.value_counts().plot.barh()

data.marriage.value_counts().plot.barh()

sns.boxplot( x=data["house_val"] );
plt.show()

data.isna().any()

print("Missing values distribution: ")
print(data.isnull().mean())
print("")

education_nan_count = data['education'].isna().sum()

marriage_nan_count = data['marriage'].isna().sum()

house_owner_nan_count = data ['house_owner'].isna().sum()

print("The number of values missing from the education column is: " + str(education_nan_count))
print("The number of values missing from the marriage column is: " + str(marriage_nan_count))
print("The number of values missing from the house owner column: " + str(house_owner_nan_count))

data = data.drop('online', axis=1)

#encode ordinal variables
enc = OrdinalEncoder()
#return an array of numerical values
data["fam_income"] = enc.fit_transform(data[["fam_income"]])

data["mortgage"] = enc.fit_transform(data[["mortgage"]])

data["fam_income"].value_counts()

data["mortgage"].value_counts()

count = (data['house_val'] == 0).sum()

print('Count of zeros in House Value column is : ', count)

#deal with zeros in house value column

data['house_val'].mean()

data['house_val'].median()

data['house_val']=data['house_val'].replace(0,data['house_val'].median())

#replace symbols in age and education
data['age'] = data['age'].str.replace('_', '').str.replace('<','').str.replace('=', '').str.replace('>','')

data['education'] = data['education'].str.replace('.', '').str.replace('<','')

data['age'] = data['age'].replace("1Unk", 1)
data['age'] = data['age'].replace("225", 2)
data['age'] = data['age'].replace("335", 3)
data['age'] = data['age'].replace("445", 4)
data['age'] = data['age'].replace("555", 5)
data['age'] = data['age'].replace("665", 6)
data['age'] = data['age'].replace("765", 7)

data['age'].mean()

data['gender'] = data['gender'].replace("M", 0)
data['gender'] = data['gender'].replace("F", 1)
data['gender'] = data['gender'].replace("U", 00)

data['marriage'] = data['marriage'].replace("Single", 0)
data['marriage'] = data['marriage'].replace("Married", 1)

data['child'] = data['child'].replace("N", 0)
data['child'] = data['child'].replace("0", 0)
data['child'] = data['child'].replace("Y", 1)
data['child'] = data['child'].replace("U", 00)

data['house_owner'] = data['house_owner'].replace("Renter", 0)
data['house_owner'] = data['house_owner'].replace("Owner", 1)

#education
data['education'] = data['education'].replace("0 HS", 0)
data['education'] = data['education'].replace("1 HS", 1)
data['education'] = data['education'].replace("2 Some College", 2)
data['education'] = data['education'].replace("3 Bach", 3)
data['education'] = data['education'].replace("4 Grad", 4)

#occupation encode others as 00
data['occupation'] = data['occupation'].replace("Farm", 0)
data['occupation'] = data['occupation'].replace("Retired", 1)
data['occupation'] = data['occupation'].replace("Blue Collar", 2)
data['occupation'] = data['occupation'].replace("Sales/Service", 3)
data['occupation'] = data['occupation'].replace("Professional", 4)
data['occupation'] = data['occupation'].replace("Others", 5)

#region, encode rest as 00
data['region'] = data['region'].replace("South", 0)
data['region'] = data['region'].replace("West", 1)
data['region'] = data['region'].replace("Midwest", 2)
data['region'] = data['region'].replace("Northeast", 3)
data['region'] = data['region'].replace("Rest", 00)

#flag
data['flag'] = data['flag'].replace("N", 0)
data['flag'] = data['flag'].replace("Y", 1)

#handle missing values
data['education'].fillna('U', inplace = True)
data['marriage'].fillna('U', inplace = True)
data['house_owner'].fillna('U', inplace = True)

#replace all unknowns with 00
data['education']= data['education'].replace("U", 00)
data['marriage']= data['marriage'].replace("U", 00)
data['house_owner']= data['house_owner'].replace("U", 00)

data.isna().any()

data.info()

#convert floats to integer
data['education'] = pd.to_numeric(data['education']).astype('Int64')
data['marriage'] = pd.to_numeric(data['marriage']).astype('Int64')
data['house_owner'] = pd.to_numeric(data['house_owner']).astype('Int64')
data['fam_income'] = pd.to_numeric(data['fam_income']).astype('Int64')
data['mortgage'] = pd.to_numeric(data['mortgage']).astype('Int64')

data.info()

data.head()

sns.boxplot(x='flag',y='education',data=data ,palette='rainbow')

pd.crosstab(data.age,data.flag).plot(kind='bar')
plt.title('Frequency')
plt.xlabel('Age')
plt.ylabel('Frequency')

pd.crosstab(data.region, data.flag).plot(kind='bar')
plt.title('Region and Flag')
plt.xlabel('Region')
plt.ylabel('Frequency')

pd.crosstab(data.fam_income, data.flag).plot(kind='bar')
plt.title('Family Income and Flag')
plt.xlabel('Income')
plt.ylabel('Frequency')

figure = px.histogram(data, x = "education",
                      color = "flag",
                      title= "Predicting the Purchase by Education")
figure.show()

sns.catplot(data= data, x="flag", y="house_val", hue="flag", kind="bar")

pd.crosstab(data.education, data.flag).plot(kind='bar')
plt.title('Education and Flag')
plt.xlabel('Education')
plt.ylabel('Frequency')

sns.catplot(data= data, x="occupation", y="house_val", hue="flag", kind="bar")

pd.crosstab(data.child, data.flag).plot(kind='bar')
plt.title('Presenc/Absence of Children and Flag')
plt.xlabel('Children')
plt.ylabel('Frequency')

axes = sns.factorplot('mortgage','flag',
                      data= data , aspect = 2.5, )

axes = sns.factorplot('fam_income','flag',
                      data= data , aspect = 2.5, )

## Create pivot table
result = pd.pivot_table(data=data, index='region', columns='mortgage',values='flag')
## create heat map of region vs mortgage vs purchase_rate
sns.heatmap(result, annot=True, cmap = 'RdYlGn_r').set_title('How does Region and Mortgage type affect Purchase?')
plt.show()

## Create pivot table
result = pd.pivot_table(data=data, index='fam_income', columns='gender',values='flag')
## create heat map of family income vs gender vs subscription_rate
sns.heatmap(result, annot=True, cmap = 'RdYlGn_r').set_title('How do Family Income and Gender affect Purchase?')
plt.show()

#crate a correlation matrix after visualisation
datacorr = pd.DataFrame(data)
corr_matrix = data.corr()
print(corr_matrix)

rs = np.random.RandomState(0)
dc = pd.DataFrame(rs.rand(10, 10))
corr = data.corr()
corr.style.background_gradient(cmap='coolwarm')

scale = StandardScaler()

X = data[['house_val']]

data['house_val']= scale.fit_transform(X)

print(data)

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix, classification_report

y = data.flag
x = data.drop('flag', axis=1)
# implementing train-test-split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state = 23)

logreg = LogisticRegression()
logreg.fit(x_train, y_train)
Y_pred = logreg.predict(x_test)
acc_log = round(logreg.score(x_train, y_train) * 100, 2)
acc_log

print(classification_report(y_test, Y_pred))
print(confusion_matrix(y_test,Y_pred))

lg_cv_score = cross_val_score(logreg, x, y, cv=10, scoring= "roc_auc").mean()
print(lg_cv_score)
print('\n')

rf = RandomForestClassifier(n_estimators=100)
rf.fit(x_train, y_train)
Y_pred = rf.predict(x_test)
acc_rf = round(rf.score(x_train, y_train) * 100, 2)
acc_rf

print(classification_report(y_test, Y_pred))
print(confusion_matrix(y_test,Y_pred))

#cross validation
rf_cv_score = cross_val_score(rf, x, y, cv=10, scoring= "roc_auc").mean()
print(rf_cv_score)
print('\n')

decision_tree = DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)
Y_pred = decision_tree.predict(x_test)
acc_decision_tree = round(decision_tree.score(x_train, y_train) * 100, 2)
acc_decision_tree

print(classification_report(y_test, Y_pred))
print(confusion_matrix(y_test,Y_pred))

decision_cv_score = cross_val_score(decision_tree, x, y, cv=10, scoring= "roc_auc").mean()
print(decision_cv_score)
print('\n')

svc = SVC()
svc.fit(x_train, y_train)
Y_pred = svc.predict(x_test)
acc_svc = round(svc.score(x_train, y_train) * 100, 2)
acc_svc

print(classification_report(y_test, Y_pred))
print(confusion_matrix(y_test,Y_pred))