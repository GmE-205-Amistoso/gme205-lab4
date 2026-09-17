from src.analysis import *
from src.spatial import Parcel, SpatialObject
from shapely.geometry import box

test_parcels = [
    {
    "parcel_id": 1,
    "zone": "Industrial",
    "is_active": True,
    "area_sqm": 1000.00,
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
            [
                121.05688171036667,
                14.659729581375492
            ],
            [
                121.0574645876991,
                14.659756496799949
            ],
            [
                121.05749751608974,
                14.660557628773537
            ],
            [
                121.05680744386929,
                14.660463376913276
            ],
            [
                121.05688171036667,
                14.659729581375492
            ]
            ]
        ]
    }
    },
    {
        "parcel_id": 2,
        "zone": "Commercial",
        "is_active": True,
        "area_sqm": 1234.56,
        "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
            [
                121.071351005625,
                14.641728576672572
            ],
            [
                121.07203139739157,
                14.641678906393368
            ],
            [
                121.07201327739315,
                14.642599064355336
            ],
            [
                121.07141277027327,
                14.642675470707387
            ],
            [
                121.071351005625,
                14.641728576672572
            ]
            ]
        ]
        }
    },
    {
        "parcel_id": 3,
        "zone": "Residential",
        "is_active": False,
        "area_sqm": 500.00,
        "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
            [
                121.05787430282267,
                14.659176592398131
            ],
            [
                121.05901578913408,
                14.659167883624269
            ],
            [
                121.05897729742796,
                14.66043946052274
            ],
            [
                121.05787535602205,
                14.660385477871337
            ],
            [
                121.05787430282267,
                14.659176592398131
            ]
            ]
        ]
        }
    }
]

print("Testing Parcel.from_dict with valid records...")
try:
    parcels = [Parcel.from_dict(p) for p in test_parcels]
    print("Pass")
except (ValueError, KeyError, TypeError) as exc:
    print(f"Fail: Valid records raised exception: {exc}")

print("Testing Parcel.from_dict with invalid records...")
test_invalid_record = [{
    "parcel_id": 99,
    "zone": "Industrial",
    "is_active": True,
    "area_sqm": 1000.00,
    "geometry": {
        "type": "Polygon",
        "coordinates": [[[999.99, 14.66], [121.05, 14.66]]]
    }
}]
try:
    test = [Parcel.from_dict(p) for p in test_invalid_record]
    print("Fail: Created a record from invalid coordinates.")
except (ValueError, KeyError, TypeError) as exc:
    print(f"Pass: Correctly rejected: {exc}")

print("Testing total_active_area...")
expected = 2234.56
area = total_active_area(parcels)
if(area == expected):
    print("Pass")
else:
    print("Fail")

test_thresholds = {
    "max_value": 1000.00,
    "zones": {"Residential", "Commercial"}
}

print("Testing parcels_above_threshold...")
res = parcels_above_threshold(parcels, test_thresholds["max_value"])
res_ids = [r.parcel_id for r in res]
expected_ids = [1, 2]

if(res_ids == expected_ids):
    print("Pass")
else:
    print("Fail")

print("Testing count_by_zone...")
expected_zones = {
    "Commercial": 1,
    "Industrial": 1,
    "Residential": 1
}
zones = count_by_zone(parcels)

if(expected_zones == zones):
    print("Pass")
else:
    print("Fail")

print("Testing development_candidates...")
expected_candidate_ids = [2]
candidates = development_candidates(parcels, 1000, test_thresholds["zones"])
candidate_ids = [c.parcel_id for c in candidates]

if candidate_ids == expected_candidate_ids:
    print("Pass")
else:
    print("Fail")

print("Testing intersecting_parcels...")
study_area = SpatialObject(box(121.05700, 14.65980, 121.05800, 14.66080))
expected_intersects_ids = [1, 3]
intersects = intersecting_parcels(parcels, study_area)
intersects_ids = [i.parcel_id for i in intersects]

if intersects_ids == expected_intersects_ids:
    print("Pass")
else:
    print("Fail")

test_flood_grid = [
    [0.2, None, 1.0],
    [0.5, 0.4, 0.3],
    [0.7, 0.1, 0.6]
]
test_slope_grid = [
    [6, None, 12],
    [19, 12, 15],
    [3, 16, 4]
]
test_criteria = {
    "max_slope_deg": 15.0,
    "max_flood_m": 0.5
}

print("Testing classify_suitability_grid...")
expected_suitability_grid = [
    [1, None, 0],
    [0, 1, 1],
    [0, 0, 0]
]
suitability_grid = classify_suitability_grid(
    test_slope_grid,
    test_flood_grid,
    test_criteria["max_slope_deg"], 
    test_criteria["max_flood_m"]
)
if suitability_grid == expected_suitability_grid:
    print("Pass")
else:
    print("Fail")

print("Testing count_suitable_cells...")
expected_suitable_count = 3
suitable_count = count_suitable_cells(suitability_grid)

if suitable_count == expected_suitable_count:
    print("Pass")
else:
    print("Fail")