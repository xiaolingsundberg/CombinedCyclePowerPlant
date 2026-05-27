Combined Cycle Power Plant Data Quality and Analysis Report
Project Purpose
This project demonstrates a Python data analysis workflow for a Combined Cycle Power Plant dataset. The goal was to inspect the raw dataset, evaluate data quality, clean and validate the data, create a basic data catalog, and summarize relationships between operating conditions and electrical power output.

The analysis was completed using Python and pandas. The workflow focused on data quality, data cataloging, and repeatable reporting, which are directly relevant to enterprise data platform work.

Dataset Overview
The original dataset contained 47,844 rows and 5 columns. The columns were:

Column	Description
AT / at	Ambient temperature
V / v	Exhaust vacuum
AP / ap	Ambient pressure
RH / rh	Relative humidity
PE / pe	Electrical power output
The column names were standardized by removing extra spaces, converting names to lowercase, and replacing spaces with underscores. This changed the column names from AT, V, AP, RH, and PE to at, v, ap, rh, and pe.

Data Quality Review
The first data quality check reviewed missing values, duplicate rows, and data types.

The initial missing value check showed no blank values in the imported dataset. The duplicate check also showed no fully duplicated records. However, the data type check showed that all five columns were imported as string/object values instead of numeric values.

Because the columns represent numeric measurements, all five columns were converted to numeric data types using pd.to_numeric(). After conversion, four rows became missing across all five columns. These rows contained non-numeric values, specifically repeated header records such as AT, V, AP, RH, PE embedded inside the dataset. Since these rows were not valid measurement records, they were removed.

After removing the invalid rows, the final cleaned dataset contained 47,840 rows and 5 columns. A final missing value check confirmed that the cleaned dataset had no remaining missing values.

Data Catalog Summary
The cleaned dataset contains five numeric columns, all stored as float64.

Column	Data Type	Missing Count	Unique Values	Min	Max	Mean
at	float64	0	2,773	1.81	37.11	19.65
v	float64	0	634	25.36	81.56	54.31
ap	float64	0	2,517	992.89	1033.30	1013.26
rh	float64	0	4,546	25.56	100.16	73.31
pe	float64	0	4,836	420.26	495.76	454.37
The unique value counts show that the fields are continuous measurement variables rather than categorical fields. The dataset is therefore appropriate for statistical analysis, correlation analysis, and potential predictive modeling.

Summary Statistics
The cleaned dataset shows that electrical power output ranges from 420.26 to 495.76, with an average value of 454.37. Ambient temperature ranges from 1.81 to 37.11, with an average of 19.65. Exhaust vacuum ranges from 25.36 to 81.56, with an average of 54.31.

These summary statistics provide a general profile of the operating conditions represented in the dataset and confirm that the cleaned data contains reasonable numeric ranges for analysis.

Correlation Analysis
The correlation analysis compared each variable with electrical power output (pe). The strongest relationships were:

Variable	Correlation with pe	Interpretation
at	-0.95	Very strong negative relationship
v	-0.87	Strong negative relationship
ap	0.52	Moderate positive relationship
rh	0.39	Weak to moderate positive relationship
Ambient temperature has the strongest relationship with power output. The correlation of -0.95 means that as ambient temperature increases, electrical power output tends to decrease. Exhaust vacuum also has a strong negative relationship with power output, with a correlation of -0.87.

Ambient pressure and relative humidity show positive relationships with power output, but these relationships are weaker than temperature and vacuum.

Key Findings
The main data quality finding was that the dataset initially appeared complete, but the data type conversion step revealed four invalid rows. These rows were repeated header records inside the raw dataset. Removing them produced a clean numeric dataset suitable for analysis.

The main analytical finding is that power output is most strongly associated with ambient temperature and exhaust vacuum. Higher ambient temperature and higher exhaust vacuum are both associated with lower electrical power output. Ambient pressure and relative humidity are positively related to power output, but their relationships are less influential based on correlation values.

Outputs Created
The Python workflow produced the following files:

cleaned_combined_cycle_power_plant.csv
data_catalog_summary.csv
summary_statistics.csv
correlation_matrix.csv
These outputs support a repeatable workflow for data quality review, metadata documentation, statistical summary, and analysis reporting.

Conclusion
This project demonstrates a practical data analysis workflow using Python. The process included importing and inspecting the dataset, standardizing column names, checking for missing values and duplicates, correcting data types, identifying invalid records, removing invalid rows, creating a data catalog, generating summary statistics, and analyzing correlations.

The cleaned dataset is now ready for further analysis, dashboard development, or predictive modeling. From a business and data platform perspective, the workflow supports reliable data preparation, transparent documentation, and reusable reporting.
