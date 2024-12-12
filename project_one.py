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