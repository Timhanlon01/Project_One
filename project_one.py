# Project_One
# Batting stats for a year range 
import pandas as pd
import matplotlib.pyplot as plt
# Matchup with Shota Imanaga
# Data source: Statmuse (https://www.statmuse.com/)
data = { 
    'Player': ['Shohei Ohtani'],
    'PA': [5],
    'AB': [5],
    'H': [0],
    'BB': [0],
    'SO': [1],
    'AVG': [0.000],
    'OBP': [0.000],
    'SLG': [0.000],
    'OPS': [0.000],
    }
df = pd.DataFrame(data)
print(df)

df.plot(x='Player', y=['AVG', 'OBP', 'SLG', 'OPS'], kind = 'bar')
plt.title("Shohei Ohtani vs Shota Imanaga")
plt.ylabel("Statistic Value")
plt.show()

#Pitch Mix for Shota Imanaga
# Data source: FanGraphs Baseball (https://www.fangraphs.com/)
pitch_data = {
    'Pitch Type': ['Four-Seam Fastball', 'Split-Finger', 'Sweeper', 'Changeup', 'Curveball'],
    'Pitches Thrown': [1347, 792, 199, 101, 84],
    'Percentage': [52.0, 30.6, 7.7, 3.9, 3.2]
}
df = pd.DataFrame(pitch_data)

#Pie chart of pitch mix
plt.figure(figsize=(10, 7))
plt.pie(df['Percentage'], labels=df['Pitch Type'], autopct='%1.1f%%')
plt.title("Shota Imanaga's 2024 Pitch Mix")
plt.show()

# Additional Pitch Characteristics
print("Pitch Velocities:")
print("Four-Seam Fastball: 92 mph")
print("Split-Finger: 83 mph")
print("Sweeper: 82 mph")
print("Changeup: 82 mph")
print("Curveball: 73 mph")

# Ohtani's performance against fastballs
fastball_data = {
    'Velocity': ['95+ mph'],
    'AVG': [0.360],
    
}