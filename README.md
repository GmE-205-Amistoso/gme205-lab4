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
FUNCTION get_total_active_area(parcels):
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

FUNCTION get_parcels_above_threshold(parcels, threshold):
    SET result to empty array
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

FUNCTION get_count_by_zone(parcels):
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

FUNCTION get_development_candidates(parcels):
    SET result to empty array
    FOR each parcel in parcels:
        IF parcel is active
            AND (parcel.zone is "Residential" OR parcel.zone is "Commercial")
            AND parcel.area_sqm >= 5000:

            ADD parcel to result
        END IF
    END FOR
    RETURN result

```

### *5. Which parcels intersect a defined study-area polygon?*
```
PSEUDOCODE

FUNCTION get_intersecting_parcels(parcels, study_area):
    SET result to empty array
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

FUNCTION get_raster_suitability(suitability_grid):
    SET output as empty array
    # Assumption here is that slope_deg and flood_m have the same dimensions
    SET rows to suitability_grid["slope_deg"] row count
    SET cols to suitability_grid["slope_deg"] column count

    FOR each row in range(rows):
        SET output_cols as empty array
        FOR each col in range(cols):
            IF suitability_grid["slope_deg"][row][col] is null
                OR suitability_grid["flood_m"][row][col] is null:
                ADD null to output_cols
                CONTINUE
            END IF

            IF suitability_grid["slope_deg"][row][col] <= suitability_grid["criteria"]["max_slope_deg"]
                AND suitability_grid["flood_m"][row][col] <= suitability_grid["criteria"]["max_flood_m"]:
                ADD 1 to output_cols
            ELSE
                ADD 0 to output_cols
            END IF
        END FOR
        ADD output_cols to output
    END FOR

    RETURN output
```

# Reflections

## 👤 Author
**ALLAN FRITZGERALD N. AMISTOSO** <br>
2014-73618 <br>
MS Geomatics Engineering - Geoinformatics
