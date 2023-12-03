import pandas as pd

df = pd.read_csv('outputData.csv', header = None, sep = ',',skipinitialspace=True)
data_dict = df.loc[df[9] == 'Apparels>Women>Western Wear>Shirts, Tops & Tunics>Tunics']
df = df.drop(df.columns[[0, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32]], axis=1)
df = df.dropna()
df.to_csv('processed_data.csv',header=False, index=False,index_label=False, sep =',')
