WITH medians AS (
  SELECT 
    country,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) OVER (PARTITION BY country) as median
  FROM 
    vaccination_stats
),
imputed AS (
  SELECT 
    vs.date,
    vs.country,
    COALESCE(vs.daily_vaccinations, m.median, 0) as daily_vaccinations
  FROM 
    vaccination_stats vs
  LEFT JOIN 
    medians m ON vs.country = m.country
)
SELECT * FROM imputed;