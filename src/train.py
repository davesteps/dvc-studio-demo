import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
import joblib

with open("./params.yaml", 'r') as s:
    params = yaml.safe_load(s)['train']

train = pd.read_csv('data/train.csv')

X = train.drop('shiptype3',axis=1)
y = train['shiptype3']

clf = RandomForestClassifier(max_depth=params['max_depth'],
                             n_estimators = params['n_estimators'],
                             min_samples_split = params['min_samples_split'],
                             random_state=0)

clf.fit(X, y)

filename = 'model.pkl'
_ = joblib.dump(clf, filename, compress=9)

