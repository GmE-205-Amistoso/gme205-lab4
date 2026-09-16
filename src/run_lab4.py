from shapely.geometry import box
from spatial import SpatialObject, Parcel
from analysis import development_candidates, intersecting_parcels

import json

VECTOR_DATA_PATH = "data/parcels_shapely_ready.json"
MIN_AREA = 5000.0
ALLOWED_ZONES = {"Residential", "Commercial"}

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create list of parcel objects from JSON file
parcels = [Parcel.from_dict(d) for d in data]

study_area = SpatialObject(
    box(121.050, 14.648, 121.060, 14.658)
)

# Get candidate parcels
candidates = development_candidates(
    parcels,
    min_area=MIN_AREA,
    allowed_zones=ALLOWED_ZONES
)

# Get intersecting parcels
results = intersecting_parcels(parcels=candidates, study_area=study_area)

for result in results:
    print("parcel_id ", result.parcel_id)