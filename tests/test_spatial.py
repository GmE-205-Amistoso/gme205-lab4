from src.spatial import Point, Parcel
from shapely.geometry import Polygon

print("Testing valid Point...")
valid_point = Point(1, 121.06, 14.65, 'UPD', 'poi')
expected = (121.06, 14.65)
if valid_point.to_tuple() == expected:
    print("Pass\n")
else:
    print("Fail\n")

print("Testing invalid Point...")
try:
    invalid_point = Point(2, 999.99, 14.65, 'UPD', 'poi')
    print("Fail\n")
except (ValueError, KeyError, TypeError) as exc:
    print(f"Skipping invalid record: {exc}")
    print("Pass\n")

print("Testing valid Point from record...")
valid_dict = {
    "id": 201,
    "geometry": [2, 2],
    "name": "Valid",
    "tag": "POI"
}
valid_point = Point.from_dict(valid_dict)
expected = (2, 2)
if valid_point.to_tuple() == expected:
    print("Pass\n")
else:
    print("Fail\n")

print("Testing invalid Point from record...")
invalid_dict = {
    "id": 202,
    "geometry": [999, 2],
    "name": "Invalid",
    "tag": "POI"
}
try:
    invalid_point = Point.from_dict(invalid_dict)
    print("Fail\n")
except (ValueError, KeyError, TypeError) as exc:
    print(f"Skipping invalid record: {exc}")
    print("Pass\n")

print("Testing point bbox...")
expected = (2.0, 2.0, 2.0, 2.0)
if valid_point.bbox() == expected:
    print("Pass\n")
else:
    print("Fail\n")

print("Testing parcel bbox...")
geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])
attributes = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}
parcel = Parcel(101, geom, attributes)
expected = (0.0, 0.0, 10.0, 5.0)
if parcel.bbox() == expected:
    print("Pass\n")
else:
    print("Fail\n")

inside = Point.from_dict({
        "id": 201,
        "geometry": [2, 2],
        "name": "Inside",
        "tag": "POI"
    }
)
outside = Point.from_dict({
        "id": 202,
        "geometry": [12, 2],
        "name": "Outside",
        "tag": "POI"
    }
)

print("Testing inside.intersects(parcel)...")
if(parcel.intersects(inside)):
    print("Pass\n")
else:
    print("Fail\n")

print("Testing outside.intersects(parcel)...")
if(not parcel.intersects(outside)):
    print("Pass\n")
else:
    print("Fail\n")

print("Testing point as_dict()")
expected = {
    'id': 201,
    'name': 'Valid',
    'tag': 'POI',
    'geometry': (2.0, 2.0),
    'bbox': (2.0, 2.0, 2.0, 2.0)
}
if valid_point.as_dict() == expected:
    print("Pass\n")
else:
    print("Fail\n")

print("Testing parcel as_dict()")
expected = {
    'parcel_id': 101,
    'bbox': (0.0, 0.0, 10.0, 5.0),
    'attributes': {
        'area': 50.0,
        'zone': 'Residential',
        'is_active': True
    },
    'polygon': 'Polygon',
    'wkt': 'POLYGON ((0 0, 10 0, 10 5, 0 5, 0 0))'
}
if parcel.as_dict() == expected:
    print("Pass\n")
else:
    print("Fail\n")