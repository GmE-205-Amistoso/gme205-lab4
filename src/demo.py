from spatial import Parcel
import json

DATA_PATH = "data/parcels_shapely_ready.json"

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

parcels = Parcel.from_dict(data[0])

print(parcels.area_sqm)
