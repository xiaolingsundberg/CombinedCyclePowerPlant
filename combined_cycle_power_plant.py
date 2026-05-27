# import library and review the data set structure 
import pandas as pd 

df = pd.read_csv("combined_cycle_power_plant.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.shape)


# standardize the data 
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# data quality check 
missing_values = df.isna().sum()
print(missing_values) # no missing values

duplicate_count = df.duplicated().sum()
print(duplicate_count) # no duplicate counts 

data_type = df.dtypes
print(data_type) # python read the values as strings 
# we need to convert them to numeric before analysis 
df["at"] = pd.to_numeric(df["at"], errors = "coerce")
df["v"] = pd.to_numeric(df["v"], errors = "coerce")
df["ap"] = pd.to_numeric(df["ap"], errors = "coerce")
df["rh"] = pd.to_numeric(df["rh"], errors = "coerce")
df["pe"] = pd.to_numeric(df["pe"], errors = "coerce")
data_type_1 = df.dtypes
print(data_type_1) # it's now numeric (float64)

# check missing values again 
missing_values_1 = df.isna().sum()
print(missing_values_1) 
# after conversion, four invalid rows were found 
# possibly because these rows contained non-numeric in the raw data set 

# identify invalid rows and drop them 
invalid_rows = df[df.isna().any(axis=1)]
print(invalid_rows)
df = df.dropna()

print(df.isna().sum()) # no missing values now 
print(df.shape) # 4 rows were dropped 

# create data catalog 
data_catalog = pd.DataFrame({
    "column_name": df.columns,
    "data_type": df.dtypes.astype(str),
    "missing_count": df.isna().sum().values,
    "missing_percentage":(df.isna().mean()*100).round(2).values,
    "unique_values": df.nunique().values,
    "min_value": df.min().values,
    "max_values": df.max().values,
    "mean_value": df.mean().round(2).values
})
print(data_catalog)

# export data catalog 
data_catalog.to_csv("data_catalog_summary.csv", index=False)

# summary statistics 
summary_statistics = df.describe().round(2)
print(summary_statistics)

# export summary statistics 
summary_statistics.to_csv("summary_statistics.csv")

# check correlation between variables 
correlation_matrix = df.corr().round(2)
print(correlation_matrix)

# export correlation matrix 
correlation_matrix.to_csv("correlation_matrix.csv")

# export the clean data set 
df.to_csv("cleaned_combined_cycle_power_plant.csv", index=False)

