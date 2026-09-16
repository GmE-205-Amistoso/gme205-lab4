# Laboratory 4: Spatial Algorithms and Structured Programming

## Required Dependencies
Before starting, make sure that you have installed the following dependencies:

- **[Python](https://www.python.org/downloads/) >= 3.14**
- **[pip](https://pip.pypa.io/en/stable/installation/) >= 26.2.1**

# Set up the Virtual Environment

## Create a Python Virtual Environment
Create a Python virtual env (venv):

```
python3 -m venv .venv
```

Run the virtual environment:
```
source .venv/bin/activate
```

## Install Dependencies
Upgrade pip.

```
pip install --upgrade pip
```
Install matplotlib and shapely
```
pip install matplotlib shapely
```

Save the installed packages.

```
pip freeze > requirements.txt
```

## How to run the Python scripts
### Running the runner script
Run the runner script using the following command:

```
python3 src/run_lab3.py
```

### Running the test file
Run test_spatial.py using the following command:
```
python3 -m tests.test_spatial
```

# Directory Structure
```
├── data                            # Data files
│   ├── parcels_shapely_ready.json  # 
│   └── suitability_grid.json       # 
├── output                          # Output files
│   ├── lab4_raster_preview.png     # 
│   ├── lab4_report.json            # 
│   └── lab4_vector_preview.png     # 
├── src                             # Source files
│   ├── analysis.py                 # Code containing structured analysis functions
│   ├── demo.py                     # Code for incremental checks
│   ├── run_lab4.py                 # Runner script
│   └── spatial.py                  # Main logic
├── test                            # Verification codes
│   ├── test_analysis               # 
│   └── test_spatial.py             # 
└── requirements.txt                # List of dependencies
```
# Algorithms
### *1. What is the total area in square meters of all active parcels?*
```
PSEUDOCODE
FUNCTION total_active_area(parcels):
    SET total = 0
    FOR each parcel in parcels:
        IF parcel is active:
            total = total + parcel.area_sqm
        END IF
    END FOR
    RETURN total
```

### *2. Which parcels have area greater than or equal to a chosen threshold?*
```
PSEUDOCODE

FUNCTION parcels_above_threshold(parcels, threshold):
    SET result to empty list
    FOR each parcel in parcels:
        IF parcel.area_sqm >= threshold:
            ADD parcel to result
        END IF
    END FOR
    RETURN result
```

### *3. How many parcels belong to each zone?*
```
PSEUDOCODE

FUNCTION count_by_zone(parcels):
    SET zone_count to empty dictionary
    FOR each parcel in parcels:
        SET zone = parcel.zone
        IF zone NOT IN zone_count:
            zone_count[zone] = 0
        END IF
        zone_count[zone] = zone_count[zone] + 1
    END FOR
    RETURN zone_count

```

### *4. Which parcels are development candidates under this rule: active, zone is Residential or Commercial, and area is at least 5,000 m²?*
```
PSEUDOCODE

FUNCTION development_candidates(parcels, min_area, allowed_zones):
    SET result to empty list
    FOR each parcel in parcels:
        IF is_development_candidate(parcel, min_area, allowed_zones):
            ADD parcel to result
        END IF
    END FOR
    RETURN result

FUNCTION is_development_candidate(parcel, min_area, allowed_zones):
    IF NOT parcel is active:
        RETURN False
    END IF
    IF parcel.zone NOT IN allowed_zones:
        RETURN False
    END IF
    IF parcel.area_sqm < min_area:
        RETURN False
    END IF
    RETURN True

```

### *5. Which parcels intersect a defined study-area polygon?*
```
PSEUDOCODE

FUNCTION intersecting_parcels(parcels, study_area):
    SET result to empty list
    FOR each parcel in parcels:
        IF parcel INTERSECTS with study_area:
            ADD parcel to result
        END IF
    END FOR
    RETURN result
```

### *6. Using a small raster-style grid, which cells satisfy both slope and flood criteria?*
```
PSEUDOCODE

FUNCTION classify_suitability_grid(slope_grid, flood_grid, max_slope, max_flood):
    IF NOT is_valid_grid(slope_grid, flood_grid):
        RETURN an empty list

    SET output as empty list
    SET rows to slope_grid length of slope_grid
    SET cols to slope_grid length of first row of slope_grid

    FOR each row in range(rows):
        SET output_cols as empty array
        FOR each col in range(cols):
            IF slope_grid[row][col] is None
                OR slope_grid[row][col] is None:
                ADD None to output_cols
            ELSE IF slope_grid[row][col] <= max_slope
                AND slope_grid[row][col] <= max_flood:
                ADD 1 to output_cols
            ELSE
                ADD 0 to output_cols
            END IF
        END FOR
        ADD output_cols to output
    END FOR

    RETURN output

FUNCTION is_valid_grid(slope_grid, flood_grid):
    SET slope_rows as length of slope_grid
    SET slope_cols as length of first row of slope_grid if slope_rows > 0, otherwise set it as 0

    IF slope_rows == 0 AND slope_cols == 0:
        RETURN False
    END IF

    SET flood_rows as length of flood_grid
    SET flood_cols as length of first row of flood_grid if flood_rows > 0, otherwise set it as 0

    IF flood_rows == 0 AND flood_cols == 0:
        RETURN False
    END IF

    IF NOT (slope_rows == flood_rows OR slope_cols == flood_cols):
        RETURN False
    END IF

    RETURN True

```

# Reflections

## 👤 Author
**ALLAN FRITZGERALD N. AMISTOSO** <br>
2014-73618 <br>
MS Geomatics Engineering - Geoinformatics
