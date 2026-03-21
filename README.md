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
