import csv

data = [
    # ---------------- 2016 West Bengal Data ----------------
    # Table from 2016_2.jpeg (Cold Wave)
    {
        "Year": 2016,
        "Rainfall": "Severe (A)",
        "Damage": "",
        "Place": "Puruliya",
        "Category of place": "West Bengal"
    },
    # Table from 2016_3.jpeg (Heat Wave Page 6)
    {
        "Year": 2016,
        "Rainfall": "Severe (B)",
        "Damage": "",
        "Place": "Purulia",
        "Category of place": "West Bengal"
    },
    # Table from 2016_1.jpeg (Heat Wave Page 7)
    {
        "Year": 2016,
        "Rainfall": "Severe (B)",
        "Damage": "",
        "Place": "Bankura, Bardhaman, South 24-Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "Severe (B)",
        "Damage": "",
        "Place": "Bardhaman",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "Severe (B)",
        "Damage": "",
        "Place": "Bardhaman, West Midnapur",
        "Category of place": "West Bengal"
    },
    # Table from 2016_4.jpeg (Heat Wave Page 8)
    {
        "Year": 2016,
        "Rainfall": "Severe (B)",
        "Damage": "",
        "Place": "Bankura",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "Severe (B)",
        "Damage": "",
        "Place": "Bankura",
        "Category of place": "West Bengal"
    },
    # Table from 2016_6.jpeg (Dust Storm)
    {
        "Year": 2016,
        "Rainfall": "",
        "Damage": "Damage to crops reported.",
        "Place": "Burdhaman",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "",
        "Damage": "i) Damage to crops reported. ii) Damage to mud houses reported.",
        "Place": "Murshidabad",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "",
        "Damage": "i) Damage to crops reported. ii) Damage to houses reported.",
        "Place": "Howarh",
        "Category of place": "West Bengal"
    },
    # Table from 2016_7.jpeg (Lightning / Thunderstorm)
    {
        "Year": 2016,
        "Rainfall": "",
        "Damage": "",
        "Place": "Malda",
        "Category of place": "West Bengal"
    },
    # Table from 2016_8.jpeg (Squall)
    {
        "Year": 2016,
        "Rainfall": "",
        "Damage": "Several trees, electric/telephone poles uprooted causing disruption in communication and power supply.",
        "Place": "North 24-Parganas",
        "Category of place": "West Bengal"
    },
    # Table from 2016_9.jpeg (Flood/Heavy rains)
    {
        "Year": 2016,
        "Rainfall": "Heavy rains & Landslides",
        "Damage": "",
        "Place": "Darjeeling",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "Flood",
        "Damage": "58000 people affected.",
        "Place": "Alipurduar, Cooch Behar, Darjeeling, Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "Heavy rains",
        "Damage": "Several trees/electric poles uprooted causing disruption in vehicular traffic & power supply.",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2016,
        "Rainfall": "Heavy rains & Flood in Mahananda river",
        "Damage": "i) Extensive damage to the crops reported. ii) 5,550 families in 45 villages affected.",
        "Place": "Hooghly, Howrah",
        "Category of place": "West Bengal"
    },

    # ---------------- 2017 West Bengal Data ----------------
    {
        "Year": 2017,
        "Rainfall": "Heavy rainfall Jul-Aug",
        "Damage": "Flood (Worst affected district, agricultural damage reported)",
        "Place": "Hooghly (Dhaniakhali, Arambagh)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "Heavy rainfall Jul-Aug",
        "Damage": "Flood (Worst affected area, agricultural damage reported)",
        "Place": "Paschim Medinipur (Ghatal, Khirpai, Chandrakona)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "274 mm rainfall recorded",
        "Damage": "Flood (Silabati & Dwarkeswar overflow, agricultural damage reported)",
        "Place": "Bankura",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "> 600 mm (20-26 Jul)",
        "Damage": "Flood (Farmland inundated, villages flooded)",
        "Place": "Birbhum (Suri-II)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "427% above normal rainfall",
        "Damage": "Flood (DVC release worsened situation)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "104 mm rainfall",
        "Damage": "Flood (Excess rainfall)",
        "Place": "Purba Medinipur (Digha)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "721% above normal rainfall",
        "Damage": "Flood (Extreme rainfall anomaly)",
        "Place": "Purulia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "621.5 mm rainfall in July",
        "Damage": "Urban Flooding (Second wettest July since 2008)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "Monsoon flood",
        "Damage": "Flood (60,000+ population affected, relief camps established)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "Monsoon flood",
        "Damage": "Flood (60,000+ population affected, Falakata-Madarihat disconnected)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2017,
        "Rainfall": "Overflow of Fulhaar, Behula, Ganga, Mahananda",
        "Damage": "Flood (200,000+ population affected, agricultural damage reported, 4 blocks submerged)",
        "Place": "Malda",
        "Category of place": "West Bengal"
    },

    # ---------------- 2018 West Bengal Data ----------------
    {
        "Year": 2018,
        "Rainfall": "Overflow of Ganga, Mahananda and tributaries",
        "Damage": "Flood, Crop Damage, River Erosion (Low-lying villages and agricultural land affected)",
        "Place": "Malda",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Heavy monsoon rainfall and river rise",
        "Damage": "Flood, Crop Damage (Flood-prone blocks affected)",
        "Place": "Murshidabad",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Himalayan river swelling",
        "Damage": "Flood (Riverbank inundation in vulnerable areas)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Monsoon rainfall and river overflow",
        "Damage": "Flood (Localized flooding)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "River flooding",
        "Damage": "Flood, Crop Damage (Agricultural areas affected)",
        "Place": "Cooch Behar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Overflow of local rivers",
        "Damage": "Flood, Waterlogging (Rural flooding reported)",
        "Place": "Nadia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "High river levels in Bhagirathi-Hooghly basin",
        "Damage": "Flood, Waterlogging (Low-lying areas vulnerable)",
        "Place": "Hooghly",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Heavy rainfall and drainage congestion",
        "Damage": "Urban Flooding, Waterlogging (Localized inundation)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Monsoon rainfall",
        "Damage": "Waterlogging, Crop Damage (Agricultural impacts in low-lying regions)",
        "Place": "Purba Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "River overflow and rainfall",
        "Damage": "Flood, Crop Damage (Rural flooding in vulnerable blocks)",
        "Place": "Paschim Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Dwarkeswar basin rise",
        "Damage": "Flood Risk, Crop Damage (River levels crossed warning stages)",
        "Place": "Bankura",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2018,
        "Rainfall": "Dwaraka and Mayurakshi basin rise",
        "Damage": "Flood Risk, Crop Damage (Low-lying agricultural land affected)",
        "Place": "Birbhum",
        "Category of place": "West Bengal"
    },

    # ---------------- 2019 West Bengal Data ----------------
    {
        "Year": 2019,
        "Rainfall": "Cyclone Bulbul",
        "Damage": "Crop Damage, Housing Damage, Flooding (Severe damage to agriculture and houses)",
        "Place": "South 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Cyclone Bulbul",
        "Damage": "Crop Damage, Flooding (Low-lying areas inundated)",
        "Place": "North 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Cyclone Bulbul",
        "Damage": "Urban Flooding, Infrastructure Damage (Fallen trees, road blockage, power disruption)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Cyclone Bulbul",
        "Damage": "Coastal Flooding, Crop Damage (Agricultural fields damaged)",
        "Place": "East Midnapore (Purba Medinipur)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Heavy Rainfall",
        "Damage": "Flood, Crop Damage (Local flooding reported)",
        "Place": "West Midnapore (Paschim Medinipur)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Monsoon Flood",
        "Damage": "Flood, River Erosion, Crop Damage (Flood-prone blocks affected)",
        "Place": "Malda",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Monsoon Flood",
        "Damage": "Flood, River Erosion (Agricultural and riverside areas affected)",
        "Place": "Murshidabad",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Monsoon Flood",
        "Damage": "Flood (River overflow in vulnerable regions)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Monsoon Flood",
        "Damage": "Flood (Low-lying areas inundated)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2019,
        "Rainfall": "Monsoon Flood",
        "Damage": "Flood, Crop Damage (Agricultural losses reported)",
        "Place": "Cooch Behar",
        "Category of place": "West Bengal"
    },

    # ---------------- 2020 West Bengal Data ----------------
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Coastal Flooding, Crop Damage, Housing Damage (About 1 million homes damaged; embankment breaches flooded villages and cropland.)",
        "Place": "South 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Flooding, Housing Damage (Around 5,500 homes damaged; widespread inundation.)",
        "Place": "North 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Urban Flooding, Infrastructure Damage (220-240 mm rainfall; ~10,000 trees uprooted; roads waterlogged; power infrastructure damaged.)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Flooding, Infrastructure Damage (Heavy rainfall and wind damage reported.)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Housing Damage, Crop Damage (Thousands of mud houses damaged.)",
        "Place": "Hooghly",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Coastal Flooding, Crop Damage (Severe agricultural and coastal impacts.)",
        "Place": "Purba Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Flooding, Infrastructure Damage (Severe damage reported after heavy rainfall and winds.)",
        "Place": "Nadia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2020,
        "Rainfall": "Cyclone Amphan",
        "Damage": "Flooding, Salinity Intrusion, Crop Damage (Embankments breached, seawater inundation affected villages and farmland.)",
        "Place": "Sundarbans Region",
        "Category of place": "West Bengal"
    },

    # ---------------- 2021 West Bengal Data ----------------
    {
        "Year": 2021,
        "Rainfall": "Cyclone Yaas",
        "Damage": "Coastal Flooding, Crop Damage, Housing Damage (Embankment breaches, seawater intrusion, villages inundated)",
        "Place": "South 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2021,
        "Rainfall": "Cyclone Yaas",
        "Damage": "Flooding, Housing Damage (Flooded villages, damaged homes, displaced population)",
        "Place": "North 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2021,
        "Rainfall": "Cyclone Yaas",
        "Damage": "Coastal Flooding, Infrastructure Damage (Coastal inundation and embankment damage)",
        "Place": "Purba Medinipur (Digha, Mandarmani)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2021,
        "Rainfall": "Heavy Rain + Cyclone Effects",
        "Damage": "Urban Flooding (Waterlogging and riverbank flooding in low-lying areas)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2021,
        "Rainfall": "Heavy Rain + High Tide",
        "Damage": "Flooding (Flooding near Hooghly riverbanks)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2021,
        "Rainfall": "Tornado + Heavy Rain",
        "Damage": "Housing Damage (Houses damaged before Yaas landfall)",
        "Place": "Hooghly",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2021,
        "Rainfall": "Cyclone Yaas",
        "Damage": "Flooding, Salinity Intrusion, Crop Damage (Large-scale agricultural and livelihood losses)",
        "Place": "Sundarbans Region",
        "Category of place": "West Bengal"
    },

    # ---------------- 2022 West Bengal Data ----------------
    {
        "Year": 2022,
        "Rainfall": "Flooding from Ganga, Mahananda and Fulhar river systems",
        "Damage": "Flood, Crop Damage, River Erosion (Flooding from Ganga, Mahananda and Fulhar river systems affected low-lying agricultural areas)",
        "Place": "Malda",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "River rise and heavy monsoon rainfall",
        "Damage": "Flood, River Erosion, Crop Damage (Flood-prone riverbank regions experienced inundation and erosion)",
        "Place": "Murshidabad",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Heavy monsoon rainfall",
        "Damage": "Flood (Heavy monsoon rainfall caused river overflow and localized flooding)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Swollen Himalayan rivers",
        "Damage": "Flood (Flooding reported in low-lying areas due to swollen Himalayan rivers)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "River flooding",
        "Damage": "Flood, Crop Damage (Agricultural land affected by river flooding)",
        "Place": "Cooch Behar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Heavy rainfall",
        "Damage": "Flood, Waterlogging (Heavy rainfall affected low-lying settlements)",
        "Place": "Nadia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Heavy rainfall",
        "Damage": "Flood, Waterlogging (Flood-prone blocks experienced inundation)",
        "Place": "Hooghly",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Heavy rainfall and drainage congestion",
        "Damage": "Urban Waterlogging (Heavy rainfall caused localized flooding and drainage congestion)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "River overflow and rainfall",
        "Damage": "Flood, Crop Damage (River basin flooding affected rural areas)",
        "Place": "Paschim Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Heavy rainfall",
        "Damage": "Waterlogging, Crop Damage (Heavy rainfall affected agricultural land and low-lying villages)",
        "Place": "Purba Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Rising river levels in Dwarkeswar basin",
        "Damage": "Flood Risk, Crop Damage (Rising river levels in Dwarkeswar basin affected surrounding regions)",
        "Place": "Bankura",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2022,
        "Rainfall": "Heavy rainfall in Dwaraka-Mayurakshi basin",
        "Damage": "Flood Risk, Crop Damage (Dwaraka-Mayurakshi basin areas affected by heavy rainfall)",
        "Place": "Birbhum",
        "Category of place": "West Bengal"
    },

    # ---------------- 2023 West Bengal Data ----------------
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall & Landslides",
        "Damage": "Landslide, Road Damage (Multiple landslides disrupted transport and hill connectivity)",
        "Place": "Darjeeling",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall & Landslides",
        "Damage": "Landslide (Roads blocked and settlements affected)",
        "Place": "Kalimpong",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall",
        "Damage": "Flood (River overflow and inundation in low-lying areas)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall",
        "Damage": "Flood (Flooding in river basin regions)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall",
        "Damage": "Flood, Crop Damage (Agricultural land affected)",
        "Place": "Cooch Behar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall",
        "Damage": "Flood, River Erosion (Ganga basin flooding and erosion)",
        "Place": "Malda",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2023,
        "Rainfall": "Heavy Monsoon Rainfall",
        "Damage": "Flood, River Erosion (Riverbank erosion and agricultural losses)",
        "Place": "Murshidabad",
        "Category of place": "West Bengal"
    },

    # ---------------- 2024 West Bengal Data ----------------
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Crop Damage, Infrastructure Damage, Housing Damage (Extreme severity)",
        "Place": "Paschim Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Infrastructure Damage, Housing Damage (High severity)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Crop Damage, Infrastructure Damage, Housing Damage (High severity)",
        "Place": "Hooghly",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Crop Damage, Infrastructure Damage (High severity)",
        "Place": "Purba Medinipur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Crop Damage (Medium severity)",
        "Place": "Bankura",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Crop Damage (Medium severity)",
        "Place": "Purulia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood, Crop Damage (Medium severity)",
        "Place": "Birbhum",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood (Medium severity)",
        "Place": "Nadia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood (Medium severity)",
        "Place": "North 24 Parganas",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2024,
        "Rainfall": "Monsoon Flooding",
        "Damage": "Flood (Medium severity)",
        "Place": "South 24 Parganas",
        "Category of place": "West Bengal"
    },

    # ---------------- 2025 West Bengal Data ----------------
    {
        "Year": 2025,
        "Rainfall": "Heavy Rainfall",
        "Damage": "Flood, Crop Damage (Villages inundated, agricultural land affected)",
        "Place": "Paschim Medinipur (Ghatal)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Heavy Rainfall",
        "Damage": "Flood, Crop Damage (Floodwater entered low-lying villages)",
        "Place": "Hooghly (Khanakul, Arambagh region)",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Heavy Rainfall",
        "Damage": "Flood, Waterlogging (Localized flooding in vulnerable areas)",
        "Place": "Howrah",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Intense Rainfall Episodes",
        "Damage": "Urban Flooding (Waterlogging after intense rainfall episodes)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Continuous heavy rainfall",
        "Damage": "Landslide, Road Damage (Major landslides disrupted transport routes)",
        "Place": "Darjeeling",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Continuous heavy rainfall",
        "Damage": "Landslide (Hill roads blocked and settlements affected)",
        "Place": "Kalimpong",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Continuous heavy rainfall",
        "Damage": "Flood (River overflow and inundation)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Continuous heavy rainfall",
        "Damage": "Flood (Low-lying areas flooded)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Continuous heavy rainfall",
        "Damage": "Flood, Crop Damage (Agricultural land affected)",
        "Place": "Cooch Behar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Continuous heavy rainfall",
        "Damage": "Flood, Waterlogging (Transport and drainage disruption)",
        "Place": "Siliguri Region",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Extreme Rainfall Event",
        "Damage": "Urban Flooding (Severe waterlogging)",
        "Place": "Jadavpur",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Extreme Rainfall Event",
        "Damage": "Urban Flooding (Roads submerged)",
        "Place": "Garia",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Extreme Rainfall Event",
        "Damage": "Urban Flooding (Residential areas affected)",
        "Place": "Bansdroni",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Extreme Rainfall Event",
        "Damage": "Urban Flooding (Transport disruption)",
        "Place": "Bijoygarh",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2025,
        "Rainfall": "Extreme Rainfall Event",
        "Damage": "Infrastructure Damage (Traffic and power disruption)",
        "Place": "Kolkata Metro Area",
        "Category of place": "West Bengal"
    },

    # ---------------- 2026 West Bengal Data ----------------
    {
        "Year": 2026,
        "Rainfall": "Heavy Rain + Squall",
        "Damage": "Heavy Rain + Squall (Trees uprooted, infrastructure disruption, fatalities reported)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2026,
        "Rainfall": "Intense Rainfall & Strong Winds",
        "Damage": "Storm Damage, Rainfall Damage (Widespread damage due to intense rainfall and strong winds)",
        "Place": "South Bengal districts",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2026,
        "Rainfall": "Heavy to very heavy rainfall",
        "Damage": "Flood Risk (Warnings issued)",
        "Place": "Jalpaiguri",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2026,
        "Rainfall": "Heavy rainfall",
        "Damage": "Flood Risk (Potential river flooding due to heavy rainfall)",
        "Place": "Alipurduar",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2026,
        "Rainfall": "Heavy rainfall",
        "Damage": "Landslide Risk (Heavy rainfall warning in hill districts)",
        "Place": "Darjeeling",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2026,
        "Rainfall": "Heavy rainfall",
        "Damage": "Landslide Risk (Heavy rainfall warning in hill districts)",
        "Place": "Kalimpong",
        "Category of place": "West Bengal"
    },
    {
        "Year": 2026,
        "Rainfall": "Repeated heavy rainfall",
        "Damage": "Urban Waterlogging Risk (Repeated heavy rainfall alerts issued)",
        "Place": "Kolkata",
        "Category of place": "West Bengal"
    }
]

output_file = r"c:\Users\Debasmita\Desktop\IEEE\merged_data.csv"
fieldnames = ["Year", "Rainfall", "Damage", "Place", "Category of place"]

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("Merged 2016-2026 West Bengal CSV generated successfully.")
