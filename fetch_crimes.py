import requests
import json
from collections import Counter

url = "https://data.police.uk/api/crimes-street/all-crime"

payload = {
    "date": "2025-12",
    "lat": "51.5074",
    "lng": "-0.1278"
}

response = requests.get(url, params=payload)

if response.status_code != 200:
    print("API error:", response.status_code)
    exit()

crimes = response.json()

with open("crimes_london.json", "w", encoding="utf-8") as file:
    json.dump(crimes, file, indent=2, ensure_ascii=False)

category_counts = Counter(crime["category"] for crime in crimes)

print("Toplam suç kaydı:", len(crimes))
print("\nSuç türleri:")

for category, count in category_counts.most_common():
    print(category, ":", count)

print("\nVeriler crimes_london.json dosyasına kaydedildi.")