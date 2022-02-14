import pandas as pd
import numpy as np
file='E:\data_cleaning\catalyst_data\companies_sorted.csv'
data=pd.read_csv(file,skipinitialspace=True)

data[['city','state','country1']]=(data['locality'].str.split(",",expand=True))

del data['country1']
data.to_csv('E:\data_cleaning\catalyst_data\companies_sorted.csv')