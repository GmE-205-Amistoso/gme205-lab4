# Laboratory 4: Spatial Algorithms and Structured Programming

## Required Dependencies
Before starting, make sure that you have installed the following dependencies:

- **[Python](https://www.python.org/downloads/) >= 3.14**
- **[pip](https://pip.pypa.io/en/stable/installation/) >= 26.2.1**

# Set up the Virtual Environment

## Create a Python Virtual Environment
Create a Python virtual env (venv):

```bash
python3 -m venv .venv
```

Run the virtual environment:
```bash
source .venv/bin/activate
```

## Install Dependencies
Upgrade pip.

```bash
pip install --upgrade pip
```
Install matplotlib and shapely
```bash
pip install matplotlib shapely
```

Save the installed packages.

```bash
pip freeze > requirements.txt
```

## How to run the Python scripts
### Running the runner script
Run the runner script using the following command:

```bash
python3 src/run_lab3.py
```

### Running the test files
Run test_spatial.py using the following command:
```bash
python3 -m tests.test_spatial
```
Run test_analysis.py using the following command:
```bash
python3 -m tests.test_analysis
```

# Directory Structure
```text
├── data                            # Data files
│   ├── parcels_shapely_ready.json  # Sample shapely-ready data
│   └── suitability_grid.json       # Sample raster suitability analysis data
├── output                          # Output files
│   ├── lab4_raster_preview.png     # Preview of suitability grid output from runner script
│   ├── lab4_report.json            # Summary dictionary output from runner script
│   └── lab4_vector_preview.png     # Preview of parcel outputs from runner script
├── src                             # Source files
│   ├── analysis.py                 # Code containing structured analysis functions
│   ├── demo.py                     # Code for incremental checks
│   ├── run_lab4.py                 # Runner script
│   └── spatial.py                  # Main logic
├── test                            # Verification codes
│   ├── test_analysis.py            # Targeted tests for analysis.py
│   └── test_spatial.py             # Targeted tests for spatial.py
└── requirements.txt                # List of dependencies
```
# Algorithms
### *1. What is the total area in square meters of all active parcels?*
```bash
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
```bash
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
```bash
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
```bash
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
```bash
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
```bash
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

# Challenges
### *Challenge 1 - Change the Policy Without Rewriting the Algorithm*
For this challenge, I used the parcel objects as inputs for both instances of the testing of development candidates.

First instance is using the given MIN_AREA and ALLOWED_ZONES.
```python
MIN_AREA = 5000.0
ALLOWED_ZONES = {"Residential", "Commercial"}
candidates = development_candidates(
        parcels,
        min_area=MIN_AREA,
        allowed_zones=ALLOWED_ZONES
    )
candidate_ids = [c.parcel_id for c in candidates]
print(candidate_ids)

```
**Output:**
```text
[2, 5, 9, 10, 11, 14, 15, 16, 18, 22, 26, 28, 29, 32, 34, 39, 40, 41, 45, 47, 51, 54, 56, 57, 58, 65, 67, 68, 70, 71, 72, 73, 74, 75, 76, 78, 86, 87, 88, 89, 91, 94, 96, 97, 100]
```

For the second instance, the following parameters are used.
```python
NEW_MIN_AREA = 10000.0
NEW_ALLOWED_ZONES = {"Industrial", "Commercial"}
new_candidates = development_candidates(
    parcels,
    min_area=NEW_MIN_AREA,
    allowed_zones=NEW_ALLOWED_ZONES
)
new_candidates_id = [p.parcel_id for p in new_candidates]
print(new_candidates_id)
```
**Output:**
```text
[10, 11, 17, 39, 48, 49, 56, 67, 70, 73, 84, 89]
```

As seen in both outputs, the output have changed by only supplying different parameters and without having to change the underlying function implementation.

### *Challenge 2 - Compose, Do Not Duplicate*
The runner script already answers this challenge through the following:
```python
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
```
As you can see in the code, the **intersecting_parcels()** function takes the returned value of **development_candidates()** function. The active + zone + area rules are handled in the intersecting_parcels() function while the intersection rule is handled the the development_candidates() function.

### *Challenge 3 - Explain One “Bad vs Good” Refactor*
Below is an example of some sort of nested logic that I have implemented in the development_candidates() function.
```python
def development_candidates(parcels) -> list:
    result = []
    for parcel in parcels:
        if (parcel["is_active"]
            and (parcel["zone"] == "Residential" or parcel["zone"] == "Commercial")
            and parcel["area_sqm"] >= 5000
        ):
            result.append(parcel)
    return result
```
This is the cleaner version of the code:
```python
def development_candidates(parcels, min_area, allowed_zones) -> list:
    result = []
    for parcel in parcels:
        if is_development_candidate(parcel, min_area, allowed_zones):
            result.append(parcel)
    return result

# Helper function
def is_development_candidate(parcel, min_area, allowed_zones):
    if not parcel.is_active:
        return False
    if parcel.zone not in allowed_zones:
        return False
    if parcel.area_sqm < min_area:
        return False
    return True
```
Instead of combining all rule validations into a single conditional statement, I rewrote the logic using a helper function, is_development_candidate(). This implementation improves the readability and flow of the code by separating the validation of each rule from the process of filtering the parcels. The current structure is also easier to extend and maintain. Unlike the previous implementation, where the minimum area and allowed zones were hard-coded into the conditional statement, the current implementation accepts these rules as parameters, allowing changes such as setting a different minimum area or specifying different allowed zones without modifying the main filtering logic. Adding new validation rules is also more straightforward, as they can be added to the is_development_candidate() helper function without significantly changing development_candidates().

### *Challenge 4 - Transfer the Algorithmic Pattern*
Below is an example code for parcel loop:
```python
for parcel in parcels:
    if is_development_candidate(parcel, min_area, allowed_zones):
        result.append(parcel)
```
Below is an example code for raster loop:
```python
for row in range(rows):
    output_cols = []
    for col in range(cols):
        if (slope_grid[row][col] is None
            or flood_grid[row][col] is None):
            output_cols.append(None)
        elif (slope_grid[row][col] <= max_slope
                and flood_grid[row][col] <= max_flood):
            output_cols.append(1)
        else:
            output_cols.append(0)
    output.append(output_cols)
```

The parcel loop and the raster nested loop use different data representations, but they apply similar structured-programming ideas.

The parcel loop is representation-specific in that it iterates directly over a collection of parcel objects. It then accesses parcel properties such as is_active, zone, and area_sqm.

In contrast, in the raster loop makes use of a nested loop to get the row and col indices to access individual raster cells. This is the representation-specific part of it. The nested loop is necessary because a raster is represented as a 2D grid, where each value is identified by its row and column.

Despite these differences, the structured-programming ideas are essentially the same. Both use a for loop to process a collection of data one element at a time, apply conditional logic to determine whether each element satisfies certain rules, and produce a result based on those conditions. The main difference is that the raster requires two levels of iteration because its data is two-dimensional, while the parcel data can be processed using a single loop because it is represented as a one-dimensional collection of parcel objects.

# Reflections

### *1. Algorithm: Choose one vector-analysis question. How did writing the algorithm/pseudocode first change the way you implemented it?*
For the question "Which parcels are development candidates under this rule: active, zone is Residential or Commercial, and area is at least 5,000 m²?", writing the pseudocode first helped guide the final implementation. Personally, I usually code first, then debug afterwards. However, for this exercise, I followed a different process: I first wrote the pseudocode, implemented it, then revisited the pseudocode and refactored the implementation.

Writing the pseudocode first forced me to identify and organize the individual rules before thinking about how to implement it in Python. This made the overall logic clearer and helped me translate each requirement into a specific validation step. My initial implementation combined the rules into a single conditional statement, but after revisiting the pseudocode, I recognized that the validation logic could be separated into a helper function, is_development_candidate(). This resulted in a cleaner implementation where the main function handles the iteration and collection of results, while the helper function handles the rules for determining whether a parcel is a candidate. This refactoring helped me produce code that was more readable, maintainable, and easier to extend.

### *2. Control flow: Where do sequence, selection, and repetition explicitly appear in your final system?*
Sequence appears in the throughout the system like in methods/functions that should be executed in a specific order. It is most prominent in the runner script/orchestrator, where the order of function calls determines whether the required inputs are available for subsequent operations. For instance, the intersecting_parcels() required the development_candidates() output first before it can perform its analysis. Similarly, the plotting scripts and summary dictionary require the results of the preceding analyses before they can generate their respective outputs. These dependencies demonstrate sequence because the operations must be performed in a particular order to produce the correct results.

Selections appeared in methods requiring rule validation or decision-making. An example is the is_development_candidate() function, which uses conditional statements to determine whether a parcel satisfies the required conditions. The function evaluates the parcel's active status, zone, and area and returns either True or False depending on whether the conditions are satisfied.

Repitition appeared usually in parts of the system which would require iterating over a set of objects or records. For example, methods that accept parcel objects iterate through each parcel in the collection to perform an analysis or validation. Repetition is also present in the raster-analysis methods, where nested for loops are used to iterate through each cell in a two-dimensional raster grid. The outer loop processes the rows, while the inner loop processes the cells within each row.

### *3. Responsibility: Give one behavior that belongs to Parcel/SpatialObject and one rule that belongs to analysis.py. Why?*
One behavior that belongs to Parcel/SpatialObject is a geometry-related behavior such as checking whether two spatial objects intersect. This behavior belongs to the object because determining a spatial relationship is a general geometric operation that can be applied to different types of spatial objects. The SpatialObject can provide this behavior without needing to know what the objects represent or what the result will be used for.

On the other hand, a rule such as checking whether a parcel belongs to an allowed zone should belong to analysis.py. This is not an inherent behavior of a parcel or its geometry but a rule defined by a particular analysis. A parcel does not inherently need to know that only Residential or Commercial zones qualify for development. That requirement comes from the development-candidate analysis and could change depending on the purpose of the analysis.

This separation of responsibility keeps Parcel/SpatialObject focused on general spatial and geometric behavior, while analysis.py handles the domain-specific rules and decisions that use those behaviors.

### *4. Conditional structure: What specific design choice prevents your development-candidate logic from becoming nested conditional chaos?*
One specific design choice is through the creation of a helper function is_development_candidate(). This separates the iteration and collection of results from the rules used to determine whether a parcel is a development candidate. Within the helper function, the rules are also checked sequentially using early returns instead of deeply nested conditional statements. Each condition can immediately return False when a requirement is not satisfied, making the logic easier to follow. This refactoring results in code that is more readable, maintainable, and easier to extend when additional rules are introduced.

### *5. Area meaning: Why does this exercise use area_sqm instead of interpreting geometry.area as square meters?*
In this exercise, we use the provided area_sqm property of the parcel instead of calculating geometry.area for several reasons. First, there is no need to recompute the geometry area when an authoritative area value is already provided as a parcel attribute. Recalculating it could also introduce unnecessary differences from the value expected by the analysis. Second, the calculated area depends on the geometry being correct. If the parcel geometry contains errors, such as incorrect boundaries or coordinates, calculating geometry.area would produce an incorrect area. And the third reason is because of the native calculation of geometry.area in Shapely. Shapely performs geometric calculations in a 2D coordinate space and returns the area in the squared units of the geometry's coordinate reference system. It does not automatically account for the projection or transform geographic coordinates into a metric coordinate system. Therefore, if the geometry is stored in a geographic CRS such as latitude and longitude, geometry.area would not directly represent an area in square meters.

### *6. Vector vs raster: How is repetition different when processing Parcel objects versus a 2D raster-style grid? What remains conceptually the same?*
Repetition differs primarily because of how the data is represented. When processing Parcel objects, repetition can be performed using a single loop that iterates directly over a collection of parcel objects. Each iteration processes one parcel at a time. In contrast, a 2D raster-style grid requires nested loops because each cell is organized by both a row and a column. The outer loop iterates through the rows, while the inner loop processes each cell within the current row.

However, the repetition is conceptually the same. In both cases, the algorithm systematically visits each element in a collection and applies the required processing or rules to that element. The main difference is that the vector data is represented as a 1D collection of objects, while the raster data is represented as a 2D grid. Therefore, the programming structure changes to match the data representation, but the underlying idea of iterating over a set of elements and performing an operation on each one remains the same.

### *7. Scale: If the input grew to one million parcels or a 10,000 × 10,000 raster, which parts of this design remain useful and which implementation choices would need to change?*
The overall design would remain useful because the separation of responsibilities and the structured control flow would still apply at a larger scale. For example, keeping the analysis rules separate from the parcel or spatial-object classes would make the system easier to optimize without changing the underlying analysis logic. Similarly, the use of helper functions such as is_development_candidate() would remain useful because the rules for determining a development candidate would not necessarily change just because the dataset became larger.

However, some implementation choices would need to change to handle the increased amount of data. Processing one million parcels using a simple Python for loop may become slow, particularly if each parcel requires expensive spatial operations. The system may need more efficient data structures, vectorized operations, or database-based processing to reduce unnecessary computation. For the 10,000 × 10,000 raster, the nested loop would require processing 100 million cells, so processing the entire grid cell-by-cell in Python could become a significant performance bottleneck. Raster-specific tools or array-based operations could be used instead to process many cells at once, and large rasters may need to be processed in chunks rather than loaded entirely into memory.


## 👤 Author
**ALLAN FRITZGERALD N. AMISTOSO** <br>
2014-73618 <br>
MS Geomatics Engineering - Geoinformatics
