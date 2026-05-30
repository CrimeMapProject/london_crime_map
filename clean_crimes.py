import json

with open("crimes_london.json", "r", encoding="utf-8") as file:
    crimes = json.load(file)

cleaned = []

for crime in crimes:

    location = crime.get("location")

    if not location:
        continue

    lat = location.get("latitude")
    lng = location.get("longitude")

    if not lat or not lng:
        continue

    street = location.get("street", {}).get("name", "Unknown")

    cleaned.append({
        "category": crime["category"],
        "street": street,
        "lat": float(lat),
        "lng": float(lng),
        "month": crime["month"]
    })

with open("cleaned_crimes.json", "w", encoding="utf-8") as file:
    json.dump(cleaned, file, indent=2)

print("Temizlenmiş kayıt sayısı:", len(cleaned))