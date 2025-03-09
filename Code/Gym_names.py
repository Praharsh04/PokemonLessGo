import requests
import json

API_KEY = "YOUR_GOOGLE_PLACES_API_KEY"
BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def fetch_gyms_nagpur():
    query = "gyms in Nagpur"
    
    params = {
        "query": query,
        "key": API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        print("Failed to retrieve data:", response.text)
        return []
    
    data = response.json()
    gyms = []
    
    for place in data.get("results", []):
        gym_data = {
            "name": place.get("name", "N/A"),
            "address": place.get("formatted_address", "N/A"),
            "rating": place.get("rating", "N/A"),
            "user_ratings_total": place.get("user_ratings_total", "N/A")
        }
        gyms.append(gym_data)
    
    return gyms

if __name__ == "__main__":
    gyms_list = fetch_gyms_nagpur()
    print(json.dumps(gyms_list, indent=4, ensure_ascii=False))
