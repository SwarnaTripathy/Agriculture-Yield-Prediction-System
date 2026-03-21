# Agriculture-Yield-Prediction-System

## Project Overview

This project focuses on analyzing and predicting agricultural yield using data-driven techniques. It integrates multiple factors such as crop type, weather conditions, rainfall, and pesticide usage to generate meaningful insights and support decision-making.
The system is designed to process raw agricultural data, transform it into structured formats, and perform analytical operations to understand yield trends and patterns. 

The Agriculture Yield Prediction System is a scalable, end-to-end data engineering solution developed to process and analyze large-scale agricultural datasets. The system is designed to transform raw crop production data into structured, analytics-ready formats for deriving actionable insights.

The architecture follows a layered approach (RAW → STAGING → WAREHOUSE), where data is ingested from CSV sources, cleaned and standardized using Python (Pandas), and transformed using SQL within Snowflake. A star schema is implemented with fact and dimension tables to support efficient querying and analytical workloads.

The project leverages advanced SQL constructs including CTEs, Window Functions, and ranking techniques to perform trend analysis, yield comparisons, and performance evaluation across crops and regions. Performance optimization is achieved through clustering, micro-partition pruning, and query tuning.

Additionally, PySpark is used for distributed data processing, enabling scalability for large datasets. The final processed data is visualized through an interactive Power BI dashboard, providing insights into yield trends, weather impact, and crop distribution.

This project showcases expertise in data warehousing, ETL/ELT pipelines, cloud-based analytics, and business intelligence.

## Objective
The objective of this project is to:

- Design a scalable data warehouse using Star Schema  
- Build a Python-based ETL/ELT pipeline for data processing  
- Transform and clean raw agricultural data into structured formats  
- Perform advanced analytical queries using SQL  
- Optimize performance using Snowflake techniques (clustering, pruning)  
- Implement secure data access using RBAC and data masking  
- Visualize insights using Power BI dashboards
- 
## Key Features  

- End-to-end data engineering pipeline (RAW → STAGING → WAREHOUSE)  
- Scalable data warehouse design using Star Schema (Fact & Dimension tables)  
- Data cleaning and preprocessing using Python (Pandas)  
- Distributed data processing using PySpark  
- Advanced SQL analytics using CTEs, Window Functions, and aggregations  
- Performance optimization using clustering and micro-partition pruning  
- Secure data access using RBAC and data masking policies  
- Interactive Power BI dashboard for visualization and insights  
- Analysis of yield trends based on crop, location, and weather conditions

## Tools & Technologies Used  

| Technology       | Category           | Purpose                                      |
|------------------|--------------------|----------------------------------------------|
| Python (Pandas)  | Data Processing    | Data cleaning and preprocessing              |
| Apache Spark     | Big Data           | Distributed data processing (PySpark)        |
| Snowflake        | Data Warehouse     | Scalable storage and ELT operations          |
| SQL              | Query Language     | Data transformation and analytics            |
| Power BI         | Visualization      | Dashboard and reporting                      |
| Jupyter Notebook | Development Tool   | Pipeline development and testing             |
| CSV / Excel      | Data Source        | Input datasets                               | 

## Project Implementation  

The project follows a structured and layered approach to process and analyze agricultural data efficiently:

### 1. Data Ingestion  
Raw agricultural data in CSV format is collected and loaded into the Snowflake **RAW_DATA** schema.  
This layer stores unprocessed data to maintain source integrity and enable traceability.

### 2. Data Cleaning & Preprocessing  
Python (Pandas) is used to clean and preprocess the data by handling missing values, removing unwanted columns, and standardizing column names.  
The cleaned data is then prepared for further transformation.

### 3. Data Transformation (STAGING Layer)  
Data is transformed using SQL within Snowflake in the **STAGING** layer.  
This includes type conversion, feature engineering, and preparing structured datasets for analytical use.

### 4. Data Warehouse Design  
A **Star Schema** is implemented in the **WAREHOUSE** layer with:  
- FACT_CROP_YIELD (central fact table)  
- DIM_CROP, DIM_LOCATION, DIM_WEATHER (dimension tables)  

This design ensures efficient querying and analytical performance.

### 5. Data Loading  
Processed data is loaded into dimension and fact tables using surrogate keys and structured joins.  
Data integrity and consistency are validated during the loading process.

### 6. Advanced Analytics  
SQL queries using CTEs, Window Functions, and aggregations are applied to perform:  
- Year-over-Year analysis  
- Ranking and trend analysis  
- Crop and region-based performance evaluation  

### 7. Performance Optimization  
Clustering is applied on frequently used columns such as **Year and Crop_ID** to improve query performance.  
Micro-partition pruning and query tuning are used to reduce data scan and execution time.

### 8. Visualization  
An interactive dashboard is created using Power BI to visualize key insights such as yield trends, crop distribution, and weather impact.  
Filters and slicers are added for dynamic analysis.

### 9. Security Implementation  
Data security is ensured using:  
- Role-Based Access Control (RBAC)  
- Dynamic Data Masking  
- Row-Level Security policies  

This ensures controlled and secure access to data.
