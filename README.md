# Cruise Ship Performance Analysis

This repository contains data and scripts for analyzing cruise ship performance metrics. The following sections provide an overview of the project structure, how to navigate the files, and key scripts for replicating the analysis.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Data](#data)
- [KPIs](#kpis)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [How to Run](#how-to-run)
- [License](#license)

## Project Structure

```bash
cruise-ship-performance-analysis/
│
├── .venv/                        # Virtual environment files
├── cruise/                       # Library root (empty for now)
├── data/                         # Data files
│   ├── data.csv                  # Raw data of cruise ship performance
│   └── data_cleaned.csv          # Cleaned dataset after preprocessing
│
├── docs/                         # Project-related documentation
│   ├── Comparison Narrative between vessels performance trends.pdf  # Performance narrative between vessels
│   ├── data_exploration_findings.md                                 # Markdown file with data exploration results
│   ├── schema.pdf                                                   # Dataset schema details
│   └── Task Description.pdf                                         # Initial task requirements
│
├── KPI/                          # Key Performance Indicator visualizations
│   ├── Diesel Generator Power.png                                  # Diesel Generator power KPI
│   ├── Flue Flow Rate (Main Engine 1).png                          # KPI for Main Engine 1 Flue Flow Rate
│   ├── Flue Flow Rate (Main Engine 2).png                          # KPI for Main Engine 2 Flue Flow Rate
│   ├── Flue Flow Rate (Main Engine 3).png                          # KPI for Main Engine 3 Flue Flow Rate
│   ├── Flue Flow Rate (Main Engine 4).png                          # KPI for Main Engine 4 Flue Flow Rate
│   ├── HVAC Power Consumption.png                                  # KPI for HVAC Power Consumption
│   ├── Propulsion Power.png                                        # Propulsion Power KPI
│   └── Speed Over Ground.png                                       # Speed Over Ground KPI
│
├── notebooks/                    # Jupyter notebooks for data analysis
│   └── data_exploration.ipynb    # Notebook for data exploration and visualizations
│
├── scripts/                      # Python scripts
│   └── vessel_dashboard.py       # Script to create a dashboard for vessel performance metrics
│
├── requirements.txt              # Python dependencies for the project
└── README.md                     # Project documentation (this file)
```
## Installation

### Virtual Environment Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/cruise-ship-performance-analysis.git
    cd cruise-ship-performance-analysis
    ```

2. **Create a virtual environment** in the root directory:

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**:

   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required packages** from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Verify the installation** by running the Python script or Jupyter notebook to ensure all dependencies are installed:

    ```bash
    jupyter notebook
    ```
## Data

The `data/` directory contains two important files:

- **`data.csv`**: This is the raw dataset containing performance data of various cruise ships.
- **`data_cleaned.csv`**: This file contains the cleaned dataset after handling missing values and performing data preprocessing.

You can use the cleaned data for analysis and visualizations.

---

## KPIs

The `KPI/` folder contains visualizations for key performance indicators (KPIs) of the cruise ship performance:

- **Diesel Generator Power.png**: Shows the diesel generator power usage.
- **Flue Flow Rate (Main Engine 1).png**: Flue flow rate for Main Engine 1.
- **Flue Flow Rate (Main Engine 2).png**: Flue flow rate for Main Engine 2.
- **Flue Flow Rate (Main Engine 3).png**: Flue flow rate for Main Engine 3.
- **Flue Flow Rate (Main Engine 4).png**: Flue flow rate for Main Engine 4.
- **HVAC Power Consumption.png**: Shows the HVAC system’s power consumption.
- **Propulsion Power.png**: Power consumed for the propulsion system.
- **Speed Over Ground.png**: The speed of the ship over the ground.

These images provide insights into the vessel’s performance trends across different areas.

---

## Notebooks

The `notebooks/` directory contains Jupyter notebooks for exploring and analyzing the data:

- **`data_exploration.ipynb`**: This notebook contains exploratory data analysis (EDA), including:
  - Data cleaning and handling of missing values
  - Initial exploratory visualizations
  - Statistical analysis and observations

You can open and run this notebook to follow along with the analysis steps and see the initial exploration of the cruise ship data.

---

## Scripts

The `scripts/` directory contains Python scripts used in the project:

- **`vessel_dashboard.py`**: This script generates a dashboard to visualize vessel performance metrics using Plotly and Dash. The dashboard is interactive and allows users to explore key performance indicators for the cruise ship.

To run this script and view the dashboard, follow the steps below.

---

## How to Run

### 1. Running the Data Exploration Notebook

To explore the data and visualizations:

1. Open a terminal and navigate to the project directory.
2. Activate the virtual environment (if not already active).
3. Run the Jupyter notebook:

    ```bash
    jupyter notebook notebooks/data_exploration.ipynb
    ```

This will open the notebook in your browser, where you can explore the data and execute cells for analysis.

### 2. Running the Dashboard Script

To launch the dashboard and interact with the cruise ship performance metrics:

1. Open a terminal and navigate to the project directory.
2. Activate the virtual environment (if not already active).
3. Run the Python dashboard script:

    ```bash
    python scripts/vessel_dashboard.py
    ```

This will start the dashboard server, and you can view the interactive dashboard in your browser at `http://127.0.0.1:8050/`.

Make sure that the necessary dependencies (listed in `requirements.txt`) are installed before running the notebook or script.
