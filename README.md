# London Crime Risk Map

A data-driven crime risk visualization project for London.

This project collects crime data from the UK Police API, processes and cleans the data, calculates location-based risk scores, and visualizes the results on an interactive map.

## Features

* Fetch crime data from UK Police API
* Clean and normalize crime records
* Calculate risk scores based on crime severity
* Group crimes by location
* Generate interactive London crime map
* Color-coded risk levels:

  * 🔴 High Risk
  * 🟡 Medium Risk
  * 🟢 Low Risk

## Project Structure

```text
fetch_crimes.py
clean_crimes.py
process_crimes.py
crime_map.py

crimes_london.json
cleaned_crimes.json
risk_london.json

london_crime_map.html
```

## Workflow

### 1. Fetch crime data

```bash
python fetch_crimes.py
```

Creates:

```text
crimes_london.json
```

### 2. Clean data

```bash
python clean_crimes.py
```

Creates:

```text
cleaned_crimes.json
```

### 3. Calculate risk scores

```bash
python process_crimes.py
```

Creates:

```text
risk_london.json
```

### 4. Generate interactive map

```bash
python crime_map.py
```

Creates:

```text
http://localhost:63342/Londra_Suclari_Projesi/london_crime_map_filtered.html?_ijt=kes23n6b157b25p5iace2n1lgu
```

Open the generated HTML file in your browser to explore crime risk locations.

## Technologies

* Python
* Requests
* JSON
* Folium
* UK Police API

## Future Improvements

* Time-based risk analysis
* Heatmap visualization
* Mobile application
* Route safety recommendations
* Real-time data updates
* Machine learning risk prediction

## Authors

Developed collaboratively by Arda Yalın Uçar and Mehmet Olgun as a crime-risk visualization and urban safety project.
