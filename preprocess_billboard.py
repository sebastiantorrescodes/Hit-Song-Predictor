import pandas as pd

# Load data
file_path = "/Users/jomosmith/Desktop/repos/Spotify Hit Predictor/billboard_hot_100.csv"
df = pd.read_csv(file_path)

# Ensure correct column names (modify if needed)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Group by track and artist
# Group by track title and artist
aggregated_df = df.groupby(['title', 'artist']).agg(
    highest_peak=('peak_position', 'min'),
    total_weeks_on_chart=('weeks_on_chart', 'sum'),
    first_appearance=('date', 'min')
).reset_index()

# Save or display results
output_path = "/Users/jomosmith/Desktop/repos/Spotify Hit Predictor/consolidated_billboard_data.csv"
aggregated_df.to_csv(output_path, index=False)

# import ace_tools as tools
# tools.display_dataframe_to_user(name="Consolidated Billboard Data", dataframe=aggregated_df)
