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

# Reflections

## 👤 Author
**ALLAN FRITZGERALD N. AMISTOSO** <br>
2014-73618 <br>
MS Geomatics Engineering - Geoinformatics
