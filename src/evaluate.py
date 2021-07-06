import pandas as pd
import joblib
from sklearn import metrics
import yaml
from sklearn.metrics import precision_recall_curve

test = pd.read_csv('data/test.csv')

X = test.drop('shiptype3',axis=1)
y = test['shiptype3']

clf = joblib.load('model.pkl')
y_pred = clf.predict(X)

metrics = {
    'cohen_kappa_score': float(metrics.cohen_kappa_score(y, y_pred)),
    'accuracy_score': float(metrics.accuracy_score(y, y_pred)),
    'balanced_accuracy_score': float(metrics.balanced_accuracy_score(y, y_pred))
}

with open(r'./metrics-evaluate.yaml', 'w') as file:
    yaml.dump(metrics, file)

test.head()

pd.DataFrame({'actual':y,'predicted':y_pred}).to_csv('./confmat.csv',index=False)
