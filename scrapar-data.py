import requests
from bs4 import BeautifulSoup
import json
import random
import time

# Output file to save the data
output_file = "dataSC.json"
# Set to ensure unique data (no duplicates)
unique_data = set()

# Function to fetch category links from the main page
def fetch_category_links():
    url = "https://dalil.egyfinder.com/categories/ar"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to access the main page.")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", class_="text-truncate")
    category_links = []
    
    for link in links:
        href = link.get("href")
        title = link.get("title")
        if href and title:
            # Check if the link already contains the base URL
            if href.startswith("https://dalil.egyfinder.com"):
                category_links.append((title, href))
            else:
                # Add the base URL if it's not included
                category_links.append((title, "https://dalil.egyfinder.com" + href))
    
    return category_links


# Function to fetch data from a specific category page
def fetch_data_from_category_page(category_url, page_number):
    url = f"{category_url}?p={page_number}"
    print(url)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access page {page_number} of {category_url}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="_itemBox")
    data = []
    
    for item in items:
        entry = {}

        # Extract the name
        name_tag = item.find("span", itemprop="name")
        entry["name"] = name_tag.text.strip() if name_tag else None

        # Extract the phone number
        phone_tag = item.find("span", itemprop="telephone")
        phone = phone_tag.text.strip() if phone_tag else None
        if phone and phone.startswith("01"):
            entry["phone"] = phone
        else:
            continue  # Skip the entry if it doesn't have a valid phone number

        # Extract the location/address
        address_tag = item.find("span", class_="text-black-50")
        entry["location"] = address_tag.text.strip() if address_tag else None

        # Extract the website URL
        website_tag = item.find("a", rel="nofollow")
        entry["website"] = website_tag["href"].strip() if website_tag else None

        # Ensure that the data is unique
        entry_tuple = tuple(entry.items())
        if entry_tuple not in unique_data:
            unique_data.add(entry_tuple)
            data.append(entry)

    return data

# Function to scrape data from pages 1 to 10 for each category
def scrape_data():
    all_data = []

    # Fetch category links
    category_links = fetch_category_links()
    for category_name, category_url in category_links:
        print(f"Fetching data from the category: {category_name}...")
        for page in range(1, 11):  # Fetch data from pages 1 to 10
            print(f"Fetching data from page {page}...")
            page_data = fetch_data_from_category_page(category_url, page)
            if page_data:
                all_data.extend(page_data)
            time.sleep(random.randint(1, 3))  # Add a random delay between page requests

    return all_data

# Function to save data into a JSON file
def save_to_json(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Main execution of the script
if __name__ == "__main__":
    data = scrape_data()  # Collect the data
    save_to_json(data, output_file)  # Save the data into a JSON file
    print(f"Saved {len(data)} entries into the file {output_file}.")
