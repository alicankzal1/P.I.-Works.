import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')
print(df["country"].unique())  
def impute_vaccinations(df):
  for country in df['country'].unique():
    df.loc[df['country'] == country, 'daily_vaccinations'] = df[df['country'] == country]['daily_vaccinations'].fillna(df[df['country'] == country]['daily_vaccinations'].min())
  # Fill countries with no data with 0
  df['daily_vaccinations'].fillna(0, inplace=True)
  return df

df = impute_vaccinations(df.copy())


print(df)
print(df.isnull().sum())
 