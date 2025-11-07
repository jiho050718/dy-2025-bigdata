import pandas as pd

hi_file_name = './hawaii-covid-data.csv'
df_raw = pd.read_csv(hi_file_name, sep=',')

print('='*50)
print(df_raw.head())
print(type(df_raw))

print('='*50)
print(df_raw.info())

df_raw['date'] = pd.to_datetime(df_raw['submission_date'], format='%m/%d/%Y')

print('='*50)
print(df_raw.info())

print('='*50)
print(df_raw.head())

print('='*50)
print(df_raw['date'].dt.year)