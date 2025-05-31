import pandas as pd

# Load the consolidated data
file_path = "/Users/jomosmith/Desktop/repos/Spotify Hit Predictor/consolidated_billboard_data.csv"
df = pd.read_csv(file_path)

# Define hit thresholds
top_peak_threshold = 10
min_weeks_threshold = 15

df['hit_score'] = (100 - df['highest_peak']) + (2 * df['total_weeks_on_chart'])

# Classify songs as hits based on the hit score threshold (Hit Score >= 120)
df['is_hit'] = (df['hit_score'] >= 120).astype(int)  # Convert Boolean to integer (1 = Hit, 0 = Not a hit)


# Save updated data
output_path = "/Users/jomosmith/Desktop/repos/Spotify Hit Predictor/billboard_with_hit_labels.csv"
df.to_csv(output_path, index=False)

# Display updated dataframe
