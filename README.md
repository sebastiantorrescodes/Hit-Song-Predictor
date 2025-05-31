# Hit-Song-Predictor

A Data Mining project that analyzes and predicts hit songs using a combination of Billboard Hot 100 chart data and Spotify data. This project aims to understand what makes a song successful and predict potential hits based on musical features and historical performance data.

## Project Overview

The Hit-Song-Predictor combines historical Billboard Hot 100 chart data with Spotify's audio features to create a comprehensive dataset for analyzing and predicting hit songs. The project includes:

- Billboard Hot 100 data scraping and processing
- Hit song classification based on chart performance
- Integration with Spotify's audio features
- Machine learning models for hit prediction

## Features

### Data Collection

- Automated scraping of Billboard Hot 100 charts (2010-2024)
- Historical performance tracking including:
  - Peak positions
  - Weeks on chart
  - Artist and song information
- Integration with Spotify's audio features

### Hit Song Classification

- Custom hit score calculation based on:
  - Peak position on Billboard charts
  - Total weeks on the chart
- Binary classification of songs as hits/non-hits using a threshold-based scoring system

### Data Processing

- Automated data cleaning and preprocessing
- Feature engineering for machine learning models
- Consolidation of Billboard and Spotify data

## How It Works

1. **Data Collection**

   - The system scrapes Billboard Hot 100 charts weekly
   - Historical data is processed and consolidated
   - Spotify data is integrated for additional audio features

2. **Hit Score Calculation**

   - Songs are scored using the formula: `hit_score = (100 - highest_peak) + (2 * total_weeks_on_chart)`
   - Songs with a hit score ≥ 120 are classified as hits

3. **Prediction Model**
   - Uses machine learning to predict potential hits
   - Incorporates both chart performance and audio features
   - Provides probability scores for new songs

## Project Structure

- `billboard_fetch.py`: Scrapes Billboard Hot 100 data
- `preprocess_billboard.py`: Processes and consolidates Billboard data
- `add_hit_score_to_billboard.py`: Calculates hit scores and classifies songs
- `Spotify_predictor.ipynb`: Jupyter notebook containing the prediction model

## Requirements

- Python 3.x
- Required Python packages:
  - pandas
  - requests
  - BeautifulSoup4
  - scikit-learn (for prediction models)
  - spotipy (for Spotify API integration)

## Getting Started

1. Clone the repository
2. Install required dependencies
3. Set up Spotify API credentials
4. Run the data collection scripts
5. Use the prediction model to analyze new songs

## Future Improvements

- Enhanced feature engineering
- Real-time prediction capabilities
- Web interface for easy song analysis
- Expanded dataset with more years of historical data
- Additional audio feature analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
