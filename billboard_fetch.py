import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_billboard_hot_100(start_date, end_date):
    base_url = "https://www.billboard.com/charts/hot-100/"
    
    print("Starting Billboard Hot 100 scraping...")
    songs_data = []
    
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")
        chart_url = base_url + formatted_date + "/"
        print(f"Fetching data from {chart_url}...")
        
        response = requests.get(chart_url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print(f"Failed to fetch data for {formatted_date}: {response.status_code}")
            current_date += pd.Timedelta(days=7)
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        chart_items = soup.select("div.o-chart-results-list-row-container")
        print(f"Found {len(chart_items)} chart items for {formatted_date}.")
        
        for item in chart_items:
            try:
                rank = item.select_one("span.c-label.a-font-primary-bold-l").text.strip() if item.select_one("span.c-label.a-font-primary-bold-l") else "N/A"
                title = item.select_one("h3.c-title").text.strip() if item.select_one("h3.c-title") else "N/A"
                artist = item.select_one("span.c-label.a-no-trucate").text.strip() if item.select_one("span.c-label.a-no-trucate") else "N/A"
                
                peak_pos_element = item.select("li.o-chart-results-list__item span.c-label")
                peak_pos = peak_pos_element[-2].text.strip() if len(peak_pos_element) > 2 else "N/A"
                weeks_on_chart = peak_pos_element[-1].text.strip() if len(peak_pos_element) > 1 else "N/A"
                
                songs_data.append([formatted_date, rank, title, artist, peak_pos, weeks_on_chart])
            except Exception as e:
                print(f"Skipping an item due to an error: {e}")
                continue
        
        # Move to the next week
        current_date += pd.Timedelta(days=7)
    
    return songs_data

def save_to_csv(data, filename="billboard_hot_100.csv"):
    df = pd.DataFrame(data, columns=["Date", "Rank", "Title", "Artist", "Peak Position", "Weeks on Chart"])
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    start_date = pd.to_datetime("2010-01-01")
    end_date = pd.to_datetime("2024-12-31")
    
    all_songs = scrape_billboard_hot_100(start_date, end_date)
    save_to_csv(all_songs)
    print("Process completed.")
