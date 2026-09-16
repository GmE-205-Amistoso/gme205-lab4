# ---------------
# Vector Analysis
# ---------------

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

# ---------------
# Raster Analysis
# ---------------

def classify_suitability_grid(slope_grid, flood_grid, max_slope, max_flood):
    if not is_valid_grid(slope_grid, flood_grid):
        return []

    output = []
    rows = len(slope_grid)
    cols = len(slope_grid[0])

    for row in range(rows):
        output_cols = []
        for col in range(cols):
            if (slope_grid[row][col] == None
                or flood_grid[row][col] == None):
                output_cols.append(None)
                print(row, " ", col, ": None")
            elif (slope_grid[row][col] <= max_slope
                  and flood_grid[row][col] <= max_flood):
                output_cols.append(1)
                print(row, " ", col, ": 1")
            else:
                output_cols.append(0)
                print(row, " ", col, ": 0")
        output.append(output_cols)

    return output
                

def is_valid_grid(slope_grid, flood_grid):
    # Check if slope_grid have values
    slope_rows = len(slope_grid)
    slope_cols = len(slope_grid[0]) if slope_rows > 0 else 0
    if slope_rows == 0 and slope_cols == 0:
        return False

    # Check if slope_grid have values
    flood_rows = len(flood_grid)
    flood_cols = len(flood_grid[0]) if flood_rows > 0 else 0
    if flood_rows == 0 and flood_cols == 0:
        return False

    # Check if no of rows and cols are the same
    if not (slope_rows == flood_rows or slope_cols == flood_cols):
        return False

    return True


def count_suitable_cells(suitability_grid):
    pass