# Project_One
# Batting stats for a year range 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
# Data source: Baseball Savant (https://www.baseballsavant.com/)
velocity_ranges = ['90-94 mph', '95+ mph', '95+ mph (Upper Zone)']
batting_avg = [0.304, 0.360, 0.360]  # Using overall avg for 90-94 mph as we lack specific data
on_base_pct = [0.412, 0.467, 0.467]  # OBP, estimated for 90-94 mph
slugging_pct = [0.654, 0.480, 0.480]  # SLG, estimated for 90-94 mph

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(velocity_ranges))
width = 0.25

# Plot bars for each statistic
ax.bar(x - width, batting_avg, width, label='Batting Average', color='#BA0021')
ax.bar(x, on_base_pct, width, label='On-Base Percentage', color='#003831')
ax.bar(x + width, slugging_pct, width, label='Slugging Percentage', color='#134A8E')

# Customize the plot
ax.set_ylabel('Percentage')
ax.set_title("Shohei Ohtani's Performance Against High-Velocity Fastballs")
ax.set_xticks(x)
ax.set_xticklabels(velocity_ranges)
ax.legend()

plt.ylim(0, 1)  # Set y-axis limit from 0 to 1 (0% to 100%)
plt.tight_layout()

# Add value labels on the bars
for i, v in enumerate(batting_avg):
    ax.text(i - width, v, f'{v:.3f}', ha='center', va='bottom')
for i, v in enumerate(on_base_pct):
    ax.text(i, v, f'{v:.3f}', ha='center', va='bottom')
for i, v in enumerate(slugging_pct):
    ax.text(i + width, v, f'{v:.3f}', ha='center', va='bottom')

plt.show()

print("Note: Data for 90-94 mph fastballs is estimated based on overall 2023 performance.")
print("Data for 95+ mph fastballs is specific to upper zone performance.")
