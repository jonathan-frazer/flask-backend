import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup


# --- Amazon Request Headers ---
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/89.0.4389.82 Safari/537.36'
    )
}

# --- Amazon Scraping Function ---
def query_item_from_amazon(item):
    query = item.replace(' ', '+') + "+energy+efficient"
    url = f"https://www.amazon.in/s?k={query}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        results = []
        items = soup.select('div.s-result-item')

        for i in items:
            title_elem = i.select_one('h2 span')
            price_elem = i.select_one('.a-price span.a-offscreen')
            link_elem = i.select_one('a.a-link-normal')

            if title_elem and price_elem and link_elem:
                title = title_elem.text.strip()
                price_text = price_elem.text.strip().replace('₹', '').replace(',', '')
                link = "https://www.amazon.in" + link_elem.get('href')

                try:
                    price = float(price_text)
                    results.append({
                        "name": title,
                        "price": price,
                        "url": link
                    })
                except:
                    continue

        return results

    except Exception as e:
        print(f"Failed to scrape for {item}: {e}")
        return []
    
#Takes a Devices Dataframe and returns the list of Devices as a Dataframe
def search_amazon_from_df(devices_df):
    all_items = []
    seen_urls = set()

    for _, row in devices_df.iterrows():
        device_name = row['Device Name']
        print(f"\nSearching alternatives for: {device_name}")
        scraped = query_item_from_amazon(device_name)

        for item in scraped:
            if item['url'] in seen_urls:
                continue
            
            #Add the thing
            all_items.append({
                "name": item['name'],
                "value": item['price'],
                "url": item['url']
            })
            seen_urls.add(item['url'])
            
        # Sleep randomly to avoid bot detection
        time.sleep(random.uniform(1, 3))

    items_df = pd.DataFrame(all_items)
    return items_df

