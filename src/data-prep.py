import pandas as pd

df = pd.read_csv('data/ais.csv')

df = df[['shiptype3', 'lon', 'lat', 'sog', 'cog', 'hdg', 'date']]

df_train = df[df.date<"2015-03-01"]
df_test = df[df.date>"2015-03-01"]

df_train.drop('date',axis=1).to_csv('data/train.csv')
df_test.drop('date',axis=1).to_csv('data/test.csv')
