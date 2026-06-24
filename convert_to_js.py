import csv
import json

rainfall_file = r"c:\Users\Debasmita\Desktop\IEEE\WB_Rainfall_2017_2025_Master.csv"
events_file = r"c:\Users\Debasmita\Desktop\IEEE\merged_data.csv"
output_js_file = r"c:\Users\Debasmita\Desktop\IEEE\data.js"

# Read Rainfall Data
rainfall_data = []
with open(rainfall_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rainfall_data.append({
            "Year": int(row["Year"]),
            "District": row["District"].strip(),
            "Annual_Rainfall_mm": float(row["Annual_Rainfall_mm"]) if row["Annual_Rainfall_mm"] else 0.0
        })

# Read Extreme Events Data
events_data = []
with open(events_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        events_data.append({
            "Year": int(row["Year"]) if row["Year"] else 0,
            "Rainfall": row["Rainfall"].strip(),
            "Damage": row["Damage"].strip(),
            "Place": row["Place"].strip(),
            "Category of place": row["Category of place"].strip()
        })

# Write to data.js
js_content = f"""// Auto-generated data file from CSV sources
const RAINFALL_DATA = {json.dumps(rainfall_data, indent=2)};

const EVENTS_DATA = {json.dumps(events_data, indent=2)};
"""

with open(output_js_file, mode="w", encoding="utf-8") as f:
    f.write(js_content)

print("data.js generated successfully!")
