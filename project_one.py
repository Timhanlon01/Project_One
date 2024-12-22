import pandas as pd

# File path
hitters_path = r"C:\Users\timha\OneDrive\Documents\Project_One\Hitters.csv"
mlb_elo_latest_path = r"C:\Users\timha\OneDrive\Documents\Project_One\mlb_elo_latest.csv"
hitters_df = pd.read_csv(hitters_path)
mlb_elo_latest_df = pd.read_csv(mlb_elo_latest_path)

# Set option to display all rows
pd.set_option('display.max_rows', None)

# Print data
print("Hitters.csv Data:")
print(hitters_df)

print("\nmlb_elo_latest.csv Data:")
print(mlb_elo_latest_df)

# Aggregating OPS by team
team_ops = hitters_df.groupby('Team')['OPS'].mean().reset_index()
team_ops.rename(columns={'OPS': 'Avg_OPS'}, inplace=True)

# Runs scored from mlb_elo-latest
team_runs = mlb_elo_latest_df[['Team1', 'Runs_Scored']].rename(columns={'Team1': 'Team'})

# Combine OPS and runs scored data
merged_df = pd.merge(team_ops, team_runs, on='Team', how='inner')

# Calculating OPS-to-Runs Ratio




#
## Calculate OPS for hitters
#hitters_df['OBP'] = (hitters_df['Hits'] + hitters_df['Walks']) / (hitters_df['AtBat'] + hitters_df['Walks'] + hitters_df['HitbyPitch'] + hitters_df['SacrificeFlies'])
#hitters_df['SLG'] = (hitters_df['Hits'] + 2*hitters_df['Doubles'] + 3*hitters_df['Triples'] + 4*hitters_df['HomeRuns']) / hitters_df['AtBat']
#hitters_df['OPS'] = hitters_df['OBP'] + hitters_df['SLG']
#
## Group hitters by team and year, calculating average OPS
#team_ops = hitters_df.groupby(['Team', 'Year'])['OPS'].mean().reset_index()
#
## Merge with MLB dataset
#merged_df = pd.merge(team_ops, mlb_df, left_on=['Team', 'Year'], right_on=['team', 'year'])
#
## Calculate correlation between OPS and Runs Scored
#correlation = merged_df['OPS'].corr(merged_df['R'])
#
## Visualize the relationship
#plt.figure(figsize=(10, 6))
#sns.scatterplot(data=merged_df, x='OPS', y='R')
#plt.title(f'Team OPS vs Runs Scored (Correlation: {correlation:.2f})')
#plt.xlabel('Team OPS')
#plt.ylabel('Runs Scored')
#plt.show()
#
## Analyze trend over time
#yearly_corr = merged_df.groupby('Year').apply(lambda x: x['OPS'].corr(x['R'])).reset_index()
#yearly_corr.columns = ['Year', 'Correlation']
#
#plt.figure(figsize=(10, 6))
#sns.lineplot(data=yearly_corr, x='Year', y='Correlation')
#plt.title('Correlation between OPS and Runs Scored Over Time')
#plt.xlabel('Year')
#plt.ylabel('Correlation Coefficient')
#plt.show()
#
#print(f"Overall correlation between OPS and Runs Scored: {correlation:.2f}")
#print(f"Average yearly correlation: {yearly_corr['Correlation'].mean():.2f}")
#







