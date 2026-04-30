import pandas as pd

# === DONNÉES AJA ===
aja_data = {
    'year': list(range(2002, 2025)),
    'domestic': [7243,6970,7403,7827,8300,8753,9751,10117,10372,10715,
                 10987,11946,13105,12458,12226,11473,11715,13136,11805,
                 14288,14685,16243,16705],
    'overseas': [3725,4212,4827,5215,5204,4390,4137,2544,2867,2669,
                 2408,2823,3266,5834,7677,9948,10092,12009,12394,
                 13134,14592,17222,21702]
}
aja_df = pd.DataFrame(aja_data)
aja_df['total'] = aja_df['domestic'] + aja_df['overseas']
aja_df['overseas_pct'] = (aja_df['overseas'] / aja_df['total'] * 100).round(1)

# === USD/JPY MANUEL (taux annuels calendaires — source: macrotrends) ===
# Années calendaires jan-déc, taux moyens annuels historiques
fx_manual = {
    2002: 125.39, 2003: 115.93, 2004: 108.15, 2005: 110.22, 2006: 116.31,
    2007: 117.75, 2008: 103.39, 2009:  93.57, 2010:  87.78, 2011:  79.81,
    2012:  79.82, 2013:  97.60, 2014: 105.74, 2015: 121.04, 2016: 108.79,
    2017: 112.14, 2018: 110.43, 2019: 109.01, 2020: 106.78, 2021: 109.75,
    2022: 131.50, 2023: 140.49, 2024: 151.97
}

fx_df = pd.DataFrame.from_dict(fx_manual, orient='index', columns=['usd_jpy'])
fx_df.index.name = 'year'

# === FUSION ET CORRECTION USD ===
df = aja_df.set_index('year').join(fx_df)
df['overseas_usd_bn'] = (df['overseas'] / df['usd_jpy'] / 100).round(2)
df['domestic_usd_bn'] = (df['domestic'] / df['usd_jpy'] / 100).round(2)
df['total_usd_bn'] = (df['total'] / df['usd_jpy'] / 100).round(2)

print(df[['overseas', 'overseas_usd_bn', 'usd_jpy', 'overseas_pct']])
df.to_csv('aja_fx_combined.csv')