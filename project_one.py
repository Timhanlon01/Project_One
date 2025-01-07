import pandas as pd
import matplotlib.pyplot as plt
# File path
hitters_path = r"C:\Users\timha\OneDrive\Documents\Project_One\Hitters.csv"
mlb_elo_latest_path = r"C:\Users\timha\OneDrive\Documents\Project_One\mlb_elo_latest.csv"
hitters_df = pd.read_csv(hitters_path)
mlb_elo_latest_df = pd.read_csv(mlb_elo_latest_path)

# Column names of both DataFrames
print("Columns in hitters_df:")
print(hitters_df.columns)
print("\nColumns in mlb_elo_latest_df:")
print(mlb_elo_latest_df.columns)

# Combining the datasets
combined_df = pd.concat([hitters_df, mlb_elo_latest_df], axis=1)
print("\nShape of combined data:", combined_df.shape)
print("\nColumns in combined data:")
print(combined_df.columns)

# Calculating OPS on the combined dataset
combined_df['OBP'] = (combined_df['Hits'] + combined_df['Walks']) / combined_df['AtBat']
combined_df['SLG'] = (combined_df['Hits'] + 4 * combined_df['HmRun']) / combined_df['AtBat']
combined_df['OPS'] = combined_df['OBP'] + combined_df['SLG']

# Group by League and calculate average OPS
team_ops = combined_df.groupby('League')['OPS'].mean().reset_index()
team_ops.rename(columns={'OPS': 'Avg_OPS'}, inplace=True)

print("\nAverage OPS by League:")
print(team_ops)

# Correlation between OPS and Runs
correlation = combined_df['OPS'].corr(combined_df['Runs'])
print(f"\nCorrelation between OPS and Runs: {correlation:.2f}")

pivot_table = pd.pivot_table(combined_df, 
                             values=['OPS', 'Runs'], 
                             index=['League'], 
                             columns=['Division'], 
                             aggfunc='mean')

print("\nPivot Table - Average OPS and Runs by League and Division:")
print(pivot_table)

# Bar chart showing each leagues average OPS
plt.figure(figsize=(10, 6))
plt.bar(team_ops['League'], team_ops['Avg_OPS'])
plt.title('Average OPS by League', fontsize=16)
plt.xlabel('League', fontsize=12)
plt.ylabel('Average OPS', fontsize=12)
plt.ylim(0, max(team_ops['Avg_OPS']) * 1.1) 
plt.tight_layout()
plt.show()

# Scatter plot showing correlation between OPS and Runs
plt.figure(figsize=(10, 6))
plt.scatter(combined_df['OPS'], combined_df['Runs'])
plt.xlabel('OPS')
plt.ylabel('Runs')
plt.title('OPS vs Runs')
plt.show()
