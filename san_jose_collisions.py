import requests
import pandas as pd
import sqlite3
import os

url = "https://geo.sanjoseca.gov/server/rest/services/OPN/OPN_OpenDataService/MapServer/512/query"

params = {
    "where": "1=1",
    "outFields": "*",
    "f": "json"
}

response = requests.get(url, params=params)
data = response.json()
records = [f["attributes"] for f in data["features"]]
df = pd.DataFrame(records)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "data", "sj_data.db")

conn = sqlite3.connect(r"C:\Users\campb\Downloads\data\sj_data.db")

df.to_sql("collisions", conn, if_exists="replace", index=False)

conn.close()
