def total_active_area(parcels) -> float:
    total = 0
    for parcel in parcels:
        if parcel.is_active:
            total = total + parcel.area_sqm

    return total

def parcels_above_threshold(parcels, threshold) -> list:
    result = []
    for parcel in parcels:
        if parcel.area_sqm >= threshold:
            result.append(parcel)

    return result

def count_by_zone(parcels) -> dict:
    zone_count = {}
    for parcel in parcels:
        zone = parcel.zone
        if zone not in zone_count:
            zone_count[zone] = 0

        zone_count[zone] = zone_count[zone] + 1

    return zone_count

def development_candidates(parcels, min_area, allowed_zones) -> list:
    result = []
    for parcel in parcels:
        if is_development_candidate(parcel, min_area, allowed_zones):
            result.append(parcel)

    return result

def is_development_candidate(parcel, min_area, allowed_zones):
    if not parcel.is_active:
        return False
    if parcel.zone not in allowed_zones:
        return False
    if parcel.area_sqm < min_area:
        return False
    return True

def intersecting_parcels(parcels, study_area) -> list:
    result = []
    for parcel in parcels:
        if parcel.intersects(study_area):
            result.append(parcel)

    return result