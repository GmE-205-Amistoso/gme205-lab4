from shapely.geometry import box
import matplotlib.pyplot as plt
import numpy as np

from spatial import SpatialObject, Parcel
from analysis import *

import json

VECTOR_DATA_PATH = "data/parcels_shapely_ready.json"
GRID_DATA_PATH = "data/suitability_grid.json"
OUTPUT_DIR = "output"

def main():
    # Load data/parcels_shapely_ready.json
    print("Loading parcel data...")
    with open(VECTOR_DATA_PATH, 'r', encoding='utf-8') as file:
        vector_data = json.load(file)

    # Create list of valid parcel objects
    print("Creating parcel objects...")
    parcels = []
    for d in vector_data:
        try:
            p = Parcel.from_dict(d)
        except (ValueError, KeyError, TypeError) as exc:
            print(f"Skipping invalid polygon: {exc}")
            continue
        parcels.append(p)

    # Define analysis parameters
        MIN_AREA = 5000.0
        ALLOWED_ZONES = {"Residential", "Commercial"}
        study_area = SpatialObject(
            box(121.050, 14.648, 121.060, 14.658)
        )

    # Vector analyses
    print("Computing parcel count...")
    parcel_count = len(parcels)
    print("Computing total area of active parcels...")
    total_active_area_sqm = total_active_area(parcels)
    print("Computing count per zone...")
    zone_counts = count_by_zone(parcels)
    print("Getting parcels above threshold...")
    above_threshold = parcels_above_threshold(parcels, MIN_AREA)
    above_threshold_ids = [p.parcel_id for p in above_threshold]
    print("Getting candidate parcels...")
    candidates = development_candidates(
        parcels,
        min_area=MIN_AREA,
        allowed_zones=ALLOWED_ZONES
    )
    candidate_ids = [c.parcel_id for c in candidates]
    print("Getting candidate parcels that intersect with study area...")
    study_area_candidates = intersecting_parcels(parcels=candidates, study_area=study_area)
    study_area_candidates_ids = [p.parcel_id for p in study_area_candidates]

    # Raster analyses

    # Load data/suitability_grid.json
    print("Loading grid data...")
    with open(GRID_DATA_PATH, 'r', encoding='utf-8') as file:
        grid_data = json.load(file)

    slope_grid = grid_data["slope_deg"]
    flood_grid = grid_data["flood_m"]
    criteria = grid_data["criteria"]
    max_slope = criteria["max_slope_deg"]
    max_flood = criteria["max_flood_m"]

    print("Analyzing suitability...")
    suitability_grid = classify_suitability_grid(slope_grid, flood_grid, max_slope, max_flood)
    rows = len(suitability_grid)
    cols = len(suitability_grid[0])
    suitable_cell_count = count_suitable_cells(suitability_grid)

    # Construct dictionaries
    print("Building dictionaries...")
    vector = {
        "parcel_count": parcel_count,
        "total_active_area_sqm": total_active_area_sqm,
        "zone_counts": zone_counts,
        "above_threshold_ids": above_threshold_ids,
        "candidate_ids": candidate_ids,
        "study_area_candidates_ids": study_area_candidates_ids
    }

    raster = {
        "rows": rows,
        "cols": cols,
        "suitable_cell_count": suitable_cell_count,
        "suitability_grid": suitability_grid
    }

    summary = {
        "vector": vector,
        "raster": raster
    }

    # Write summary to JSON file
    print("Generating summary file...")
    with open(OUTPUT_DIR+"/lab4_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    # Plot parcels
    print("Generating parcel plot...")
    fig, ax = plt.subplots()
    for parcel in study_area_candidates:
        x,y = parcel.geometry.exterior.xy
        ax.plot(x, y, color="red", linewidth=2, label='Parcel')
        ax.fill(x, y, alpha=0.2, color="red")
        centroid = parcel.geometry.centroid
        ax.text(centroid.x, centroid.y, f"Parcel {parcel.parcel_id}", fontsize=10, ha='center', va='center', color='black')
    plt.savefig(OUTPUT_DIR+"/lab4_vector_preview.png", dpi=300, bbox_inches="tight")
    plt.close()

    grid = np.array(
        [[np.nan if cell is None else cell for cell in row] for row in suitability_grid],
        dtype=float
    )

    # Visualize suitability_grid
    print("Generating suitability grid plot...")
    fig, ax = plt.subplots(figsize=(5, 5))
    # Use a masked array so NaN cells render distinctly (e.g. as gray)
    masked_grid = np.ma.masked_invalid(grid)
    cmap = plt.cm.Blues
    cmap.set_bad(color="lightgray")  # color for null/NaN cells

    im = ax.imshow(masked_grid, cmap=cmap)

    # Annotate each cell with its value
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            val = suitability_grid[r][c]
            text = "null" if val is None else f"{val:.2f}"
            ax.text(c, r, text, ha="center", va="center", color="black", fontsize=9)

    ax.set_title("Suitability grid")
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    plt.savefig(OUTPUT_DIR+"/lab4_raster_preview.png", dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()