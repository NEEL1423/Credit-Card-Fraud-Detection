import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('creditcard.csv')
data.head()


features = ['V%d' % number for number in range(1,4)] + ['Amount']
target = 'Class'
X = data[features]
Y = data[target]
# X.hist(figsize=(10,10))
# plt.show()


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
# X.hist(figsize=(10,10))
# plt.show()


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=101)


#Random Forest

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,Y_train)
Y_pred = clf.predict(X_test)

from sklearn import metrics
from sklearn.metrics import classification_report
print(classification_report(Y_test, Y_pred))
print('Accuracy RF:',metrics.accuracy_score(Y_test, Y_pred))