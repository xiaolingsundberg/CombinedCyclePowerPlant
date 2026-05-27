# Combined Cycle Power Plant Data Quality Analysis

This project demonstrates a Python-based data quality and analysis workflow for a Combined Cycle Power Plant dataset. The workflow focuses on data inspection, cleaning, validation, data cataloging, summary statistics, and correlation analysis.

The project was designed to show practical data analytics skills relevant to enterprise data platform work, including:

- Data quality checks
- Data type validation
- Invalid record identification
- Data catalog creation
- Cleaned dataset export
- Summary and correlation reporting

## Dataset Overview

The original dataset contained **47,844 rows** and **5 columns**.

| Column | Description |
|---|---|
| `AT` / `at` | Ambient temperature |
| `V` / `v` | Exhaust vacuum |
| `AP` / `ap` | Ambient pressure |
| `RH` / `rh` | Relative humidity |
| `PE` / `pe` | Electrical power output |

Column names were standardized from uppercase labels to lowercase names:

```text
AT, V, AP, RH, PE
```

became:

```text
at, v, ap, rh, pe
```

## Workflow

The Python workflow follows these main steps:

1. Load and inspect the dataset.
2. Standardize column names.
3. Check for missing values.
4. Check for duplicate rows.
5. Review and correct data types.
6. Identify invalid non-numeric records.
7. Remove invalid rows.
8. Create a data catalog summary.
9. Generate summary statistics.
10. Create a correlation matrix.
11. Export cleaned data and analysis outputs.

## Data Quality Findings

The initial missing value check showed no blank values in the imported dataset. The duplicate check also showed no fully duplicated records.

However, the data type check showed that all five columns were imported as string/object values instead of numeric values. Since the columns represent measurements, they were converted to numeric data types using `pd.to_numeric()`.

After conversion, four rows became missing across all five columns. These rows contained repeated header records such as:

```text
AT,V,AP,RH,PE
```

Because those rows were not valid measurement records, they were removed.

Final cleaned dataset:

| Item | Count |
|---|---:|
| Original rows | 47,844 |
| Invalid rows removed | 4 |
| Final cleaned rows | 47,840 |
| Final columns | 5 |
| Remaining missing values | 0 |

## Data Catalog Summary

| Column | Data Type | Missing Count | Unique Values | Min | Max | Mean |
|---|---:|---:|---:|---:|---:|---:|
| `at` | float64 | 0 | 2,773 | 1.81 | 37.11 | 19.65 |
| `v` | float64 | 0 | 634 | 25.36 | 81.56 | 54.31 |
| `ap` | float64 | 0 | 2,517 | 992.89 | 1033.30 | 1013.26 |
| `rh` | float64 | 0 | 4,546 | 25.56 | 100.16 | 73.31 |
| `pe` | float64 | 0 | 4,836 | 420.26 | 495.76 | 454.37 |

The unique value counts show that the fields are continuous measurement variables rather than categorical fields.

## Correlation Findings

The correlation analysis compared each operating variable with electrical power output (`pe`).

| Variable | Correlation with `pe` | Interpretation |
|---|---:|---|
| `at` | -0.95 | Very strong negative relationship |
| `v` | -0.87 | Strong negative relationship |
| `ap` | 0.52 | Moderate positive relationship |
| `rh` | 0.39 | Weak to moderate positive relationship |

The strongest relationship is between ambient temperature (`at`) and electrical power output (`pe`). The correlation of **-0.95** means that as ambient temperature increases, power output tends to decrease.

Exhaust vacuum (`v`) also has a strong negative relationship with power output. Ambient pressure (`ap`) and relative humidity (`rh`) have positive relationships with power output, but their relationships are weaker.

## Key Takeaways

- The dataset required data type correction before analysis.
- Four repeated header rows were found inside the raw data and removed.
- The final dataset contains 47,840 clean numeric records.
- Ambient temperature and exhaust vacuum have the strongest relationships with power output.
- The cleaned dataset is ready for additional analysis, dashboard development, or predictive modeling.

## Files in This Repository

| File | Description |
|---|---|
| `combined_cycle_power_plant.py` | Main Python workflow |
| `combined_cycle_power_plant.csv` | Original dataset |
| `cleaned_combined_cycle_power_plant.csv` | Cleaned dataset after validation |
| `data_catalog_summary.csv` | Metadata and quality summary by column |
| `summary_statistics.csv` | Descriptive statistics |
| `correlation_matrix.csv` | Correlation matrix |
| `combined_cycle_power_plant_report.md` | Full written analysis report |

## Tools Used

- Python
- pandas

## How to Run

```bash
python combined_cycle_power_plant.py
```

Running the script regenerates the cleaned dataset and summary output files.
