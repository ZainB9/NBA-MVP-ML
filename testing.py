import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plotting environment
plt.style.use('seaborn-darkgrid')
sns.set_context("talk")

# Distribution of Key Metrics

# 1. Histograms for points per game, rebounds per game, and assists per game
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Points per Game
sns.histplot(final_combined_data['pts'], bins=30, kde=True, ax=axes[0], color='blue')
axes[0].set_title('Points per Game Distribution')
axes[0].set_xlabel('Points per Game')

# Rebounds per Game
sns.histplot(final_combined_data['reb'], bins=30, kde=True, ax=axes[1], color='green')
axes[1].set_title('Rebounds per Game Distribution')
axes[1].set_xlabel('Rebounds per Game')

# Assists per Game
sns.histplot(final_combined_data['ast'], bins=30, kde=True, ax=axes[2], color='orange')
axes[2].set_title('Assists per Game Distribution')
axes[2].set_xlabel('Assists per Game')

plt.tight_layout()
plt.show()

# 2. Correlation Heatmap
plt.figure(figsize=(12, 8))
correlation_features = ['pts', 'reb', 'ast', 'usg_pct', 'ts_pct', 'net_rating', 'oreb_pct', 'dreb_pct']
correlation_matrix = final_combined_data[correlation_features].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 3. Player Performance Comparison - Bar chart for top players by points per game
top_players = final_combined_data.sort_values(by='pts', ascending=False).head(10)
plt.figure(figsize=(14, 6))
sns.barplot(x='player_name', y='pts', data=top_players, palette='viridis')
plt.title('Top 10 Players by Points per Game')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Points per Game')
plt.xlabel('Player Name')
plt.show()

# 4. Trend Over Time - Line chart for average points per game over the years
avg_points_per_year = final_combined_data.groupby('season')['pts'].mean().reset_index()

plt.figure(figsize=(14, 6))
sns.lineplot(x='season', y='pts', data=avg_points_per_year, marker='o', color='purple')
plt.title('Average Points per Game Over the Years')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Average Points per Game')
plt.xlabel('Season')
plt.show()

# 5. Scatter Plot - Usage percentage vs. Points per game
plt.figure(figsize=(10, 6))
sns.scatterplot(x='usg_pct', y='pts', data=final_combined_data, hue='player_name', palette='Spectral', alpha=0.7)
plt.title('Usage Percentage vs. Points per Game')
plt.xlabel('Usage Percentage')
plt.ylabel('Points per Game')
plt.show()
