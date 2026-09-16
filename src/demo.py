from spatial import Parcel
from analysis import *
import json

DATA_PATH = "data/parcels_shapely_ready.json"

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

# parcels = Parcel.from_dict(data[0])
# print(parcels.area_sqm)

parcels = []
for d in data:
    parcels.append(Parcel.from_dict(d))

print("total_active_area test:")
print(total_active_area(parcels))
print("\n\nparcels_above_threshold test:")
print(parcels_above_threshold(parcels, 15000))
print("\n\ncount_by_zone test:")
print(count_by_zone(parcels))
print("\n\ndevelopment_candidates test:")
print(development_candidates(parcels, 15000, ["Residential", "Commercial"]))
print("\n\nintersecting_parcels test:")
print(intersecting_parcels(parcels, parcels[0]))