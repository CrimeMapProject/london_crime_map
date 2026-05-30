import json
from collections import defaultdict

with open("cleaned_crimes.json", "r", encoding="utf-8") as file:
    crimes = json.load(file)

crime_weights = {
    "violent-crime": 5,
    "robbery": 5,
    "possession-of-weapons": 5,
    "burglary": 4,
    "theft-from-the-person": 4,
    "vehicle-crime": 3,
    "drugs": 3,
    "public-order": 3,
    "criminal-damage-arson": 3,
    "other-theft": 2,
    "shoplifting": 2,
    "anti-social-behaviour": 2,
    "bicycle-theft": 2,
    "other-crime": 1
}

street_scores = defaultdict(lambda: {
    "street": "",
    "lat": 0,
    "lng": 0,
    "total_crimes": 0,
    "risk_score": 0,
    "crime_types": defaultdict(int)
})

for crime in crimes:
    key = f"{crime['street']}_{crime['lat']}_{crime['lng']}"
    category = crime["category"]
    weight = crime_weights.get(category, 1)

    street_scores[key]["street"] = crime["street"]
    street_scores[key]["lat"] = crime["lat"]
    street_scores[key]["lng"] = crime["lng"]
    street_scores[key]["total_crimes"] += 1
    street_scores[key]["risk_score"] += weight
    street_scores[key]["crime_types"][category] += 1

results = []

for key, data in street_scores.items():
    score = data["risk_score"]

    if score >= 150:
        level = "high"
    elif score >= 50:
        level = "medium"
    else:
        level = "low"

    results.append({
        "location_key": key,
        "street": data["street"],
        "lat": data["lat"],
        "lng": data["lng"],
        "total_crimes": data["total_crimes"],
        "risk_score": score,
        "risk_level": level,
        "crime_types": dict(data["crime_types"])
    })

results.sort(key=lambda x: x["risk_score"], reverse=True)


with open("risk_london.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=2, ensure_ascii=False)

print("Risk noktaları oluşturuldu:", len(results))
print("-" * 50)

print(" En Riskli 10 Nokta:")
for item in results[:10]:
    print(f'{item["street"]} | Skor: {item["risk_score"]} | Seviye: {item["risk_level"]}')

print("-" * 50)

print(" En Güvenli 10 Nokta:")
for item in results[-10:][::-1]:
    print(f'{item["street"]} | Skor: {item["risk_score"]} | Seviye: {item["risk_level"]}')