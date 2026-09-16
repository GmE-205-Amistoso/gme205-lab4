from spatial import Parcel

def total_active_area(parcels) -> float:
    total = 0
    for parcel in parcels:
        if parcel["is_active"]:
            total = total + parcel["area_sqm"]

    return total

def parcels_above_threshold(parcels, threshold) -> list:
    result = []
    for parcel in parcels:
        if parcel["area_sqm"] >= threshold:
            result.append(parcel)

    return result

def count_by_zone(parcels) -> dict:
    zone_count = {}
    for parcel in parcels:
        zone = parcel["zone"]
        if zone not in zone_count:
            zone_count[zone] = 0

        zone_count[zone] = zone_count[zone] + 1

    return zone_count

def development_candidates(parcels) -> list:
    result = []
    for parcel in parcels:
        if (parcel["is_active"]
            and (parcel["zone"] == "Residential" or parcel["zone"] == "Commercial")
            and parcel["area_sqm"] >= 5000
        ):
            result.append(parcel)

    return result

def intersecting_parcels(parcels, study_area: dict) -> list:
    result = []
    p2 = Parcel.from_dict(study_area)
    for parcel in parcels:
        p1 = Parcel.from_dict(parcel)
        if p1.intersects(p2):
            result.append(parcel)

    return result