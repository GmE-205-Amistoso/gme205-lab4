from spatial import Parcel
from analysis import *
import json

PARCEL_DATA_PATH = "data/parcels_shapely_ready.json"
GRID_DATA_PATH = "data/suitability_grid.json"

# with open(PARCEL_DATA_PATH, 'r', encoding='utf-8') as file:
#     data = json.load(file)

# parcels = [Parcel.from_dict(d) for d in data]

with open(GRID_DATA_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

slope_grid = data["slope_deg"]
flood_grid = data["flood_m"]
criteria = data["criteria"]
max_slope = criteria["max_slope_deg"]
max_flood = criteria["max_flood_m"]

print(classify_suitability_grid(slope_grid, flood_grid, max_slope, max_flood))
