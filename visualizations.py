import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('data/aja_fx_combined.csv', index_col='year')

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Japanese Anime Industry: Monetary Illusion Analysis (2002-2024)',
             fontsize=15, fontweight='bold')

ax1 = axes[0, 0]
ax1.plot(df.index, df['overseas'] / 1000, color='#e63946', linewidth=2.5,
         marker='o', markersize=4, label='Overseas (Trillion JPY)')
ax1_r = ax1.twinx()
ax1_r.plot(df.index, df['overseas_usd_bn'], color='#457b9d', linewidth=2.5,
           linestyle='--', marker='s', markersize=4, label='Overseas (USD Billion)')
ax1.set_title('Overseas Revenue: JPY vs USD')
ax1.set_ylabel('Trillion JPY', color='#e63946')
ax1_r.set_ylabel('USD Billion', color='#457b9d')
ax1.legend(loc='upper left', fontsize=8)
ax1_r.legend(loc='center left', fontsize=8)
ax1.grid(True, alpha=0.3)

ax2 = axes[0, 1]
ax2.fill_between(df.index, df['usd_jpy'], alpha=0.3, color='#f4a261')
ax2.plot(df.index, df['usd_jpy'], color='#e76f51', linewidth=2.5, marker='o', markersize=4)
ax2.axhline(y=df['usd_jpy'].mean(), color='gray', linestyle=':',
            label=f"Average: {df['usd_jpy'].mean():.0f}")
ax2.set_title('USD/JPY Annual Average Rate')
ax2.set_ylabel('JPY per USD')
ax2.legend()
ax2.grid(True, alpha=0.3)

ax3 = axes[1, 0]
ax3.stackplot(df.index, df['domestic_usd_bn'], df['overseas_usd_bn'],
              labels=['Domestic', 'Overseas'],
              colors=['#2a9d8f', '#e9c46a'], alpha=0.8)
ax3.set_title('Total Market in USD: Domestic vs Overseas')
ax3.set_ylabel('USD Billion')
ax3.legend(loc='upper left')
ax3.grid(True, alpha=0.3)

ax4 = axes[1, 1]
colors = ['#e63946' if p > 50 else '#457b9d' for p in df['overseas_pct']]
ax4.bar(df.index, df['overseas_pct'], color=colors, alpha=0.8, edgecolor='white')
ax4.axhline(y=50, color='black', linestyle='--', linewidth=1.2, label='50% threshold')
ax4.set_title('Overseas Share of Total Market (%)')
ax4.set_ylabel('%')
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('anime_market_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("DONE")
