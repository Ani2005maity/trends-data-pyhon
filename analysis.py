import pandas as pd
import matplotlib.pyplot as plt

print("--- Starting CSV Analysis ---")

try:
    df = pd.read_csv('trends.csv')
    
    sector_summary = df.groupby('Sector')['Investment_Billions_USD'].sum().sort_values(ascending=False)
    
    print("\nTotal Investment by Sector (Billions USD):")
    print(sector_summary)
    
    plt.figure(figsize=(10, 6))
    sector_summary.plot(kind='bar', color='#4CAF50')
    plt.title('Global Investment Trends (2024-2025)')
    plt.ylabel('Investment (Billions USD)')
    plt.xlabel('Sector')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig('trends_chart.png')
    print("\nSuccess: Chart saved as 'trends_chart.png'")

except FileNotFoundError:
    print("Error: Could not find 'trends.csv'. Make sure the file exists in this folder.")
