import pandas as pd
import numpy as np

# Veri setini oku
df = pd.read_csv('/workspaces/P.I.-Works./country_vaccination_stats.csv')

# Eksik değerleri impute et
df['daily_vaccinations'].fillna(df['daily_vaccinations'].median(), inplace=True)

# 'date' sütununu doğru tarih formatına dönüştür
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# 1/6/2021 tarihinde yapılan toplam aşılamaların sayısını bul
total_vaccinations = df[df['date'] == '2021-01-06']['daily_vaccinations'].sum()
total_vaccinations = total_vaccinations.astype(np.int64)
print(total_vaccinations)