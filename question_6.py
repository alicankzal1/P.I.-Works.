import pandas as pd
import numpy as np


df = pd.read_csv('/workspaces/P.I.-Works./country_vaccination_stats.csv')

df['daily_vaccinations'].fillna(df['daily_vaccinations'].median(), inplace=True)

top_countries = df.groupby('country')['daily_vaccinations'].median().sort_values(ascending=False)

top_3_countries = top_countries[:3].index.tolist()

print(top_3_countries)