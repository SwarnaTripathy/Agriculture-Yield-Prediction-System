#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd


df = pd.read_csv('C:/Users/swarn/OneDrive/Documents/wipro 24 Agriculture Yield Prediction System/Dataset/Raw Data/yield_df.csv')
print(df.head())


# In[33]:


import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user="swarnatripathy",
    password="ssu6GLQVaBgcFmF",
    account="zbtaykt-kt72506",
    warehouse="COMPUTE_WH",
    database="AGRICULTURE_DB",
    schema="RAW_DATA"
)

# Create cursor
cur = conn.cursor()
cur.execute("SELECT * FROM YIELD_DF LIMIT 10")
df = pd.DataFrame(
    cur.fetchall(),
    columns=[desc[0] for desc in cur.description]
)
df


# In[26]:


import pandas as pd
import numpy as np

def transform_data(df):

    # Standardize column names 
    df.columns = df.columns.str.strip().str.upper()

    # Convert numeric columns properly
    numeric_cols = [
        "YEAR",
        "HG_HA_YIELD",
        "AVERAGE_RAIN_FALL_MM_PER_YEAR",
        "PESTICIDES_TONNES",
        "AVG_TEMP"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Handle missing values
    df = df.fillna(0)

    # Feature Engineering

    # Rainfall-Yield ratio
    df["RAIN_YIELD_RATIO"] = (
        df["HG_HA_YIELD"] / (df["AVERAGE_RAIN_FALL_MM_PER_YEAR"] + 1)
    )

    # Temperature-Yield ratio
    df["TEMP_YIELD_RATIO"] = (
        df["HG_HA_YIELD"] / (df["AVG_TEMP"] + 1)
    )

    # High yield flag
    df["HIGH_YIELD_FLAG"] = np.where(
        df["HG_HA_YIELD"] > df["HG_HA_YIELD"].mean(),
        1,
        0
    )

    print("Transformation completed successfully.")

    return df


# Apply transformation
df = transform_data(df)

df.head()


# In[27]:


from snowflake.connector.pandas_tools import write_pandas

success, nchunks, nrows, _ = write_pandas(
    conn,
    df,
    "YIELD_DF_TRANSFORMED",
    auto_create_table=True
)

print("Success:", success)
print("Rows inserted:", nrows)


# In[28]:


df.info()


# In[29]:


# Standardize column names 
df.columns = df.columns.str.upper()

# Convert numeric columns 
df["YEAR"] = pd.to_numeric(df["YEAR"], errors="coerce")
df["HG_HA_YIELD"] = pd.to_numeric(df["HG_HA_YIELD"], errors="coerce")
df["AVERAGE_RAIN_FALL_MM_PER_YEAR"] = pd.to_numeric(df["AVERAGE_RAIN_FALL_MM_PER_YEAR"], errors="coerce")
df["PESTICIDES_TONNES"] = pd.to_numeric(df["PESTICIDES_TONNES"], errors="coerce")
df["AVG_TEMP"] = pd.to_numeric(df["AVG_TEMP"], errors="coerce")

# Fill nulls
df = df.fillna(0)
df.info()


# In[31]:


import pandas as pd

# Load raw CSV
df = pd.read_csv(r'C:/Users/swarn/OneDrive/Documents/wipro 24 Agriculture Yield Prediction System/Dataset/Raw Data/yield_df.csv')

# Remove unwanted index column (like Unnamed: 0)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Original Columns:")
print(df.columns)

# Force rename ALL columns by position
df.columns = [
    "Area",
    "Item",
    "Year",
    "Yield",
    "Rainfall",
    "Pesticides",
    "Temperature"
]

print("New Columns:")
print(df.columns)

# Save cleaned CSV
df.to_csv(
    r'C:/Users/swarn/OneDrive/Documents/wipro 24 Agriculture Yield Prediction System/Dataset/Processed Data/cleaned_data.csv',
    index=False
)

print("FINAL CLEAN CSV CREATED")

