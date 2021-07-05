import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

train = pd.read_csv('data/train.csv')

X = train.drop('shiptype3',axis=1)
y = train['shiptype3']

clf = RandomForestClassifier(max_depth=2, random_state=0)

clf.fit(X, y)

filename = 'model.pkl'
_ = joblib.dump(clf, filename, compress=9)

