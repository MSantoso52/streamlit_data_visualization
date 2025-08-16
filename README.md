# streamlit_data_visualization
# *Overview*
Repo project to demonstrate Data visualization using Streamlit, input data from customer_data.csv & order_data.csv file through data processing using PySpark to revenue_data.csv. 
# *Prerequisites*
To follow along this learning we need to ensure python3 installed 
  ```bash
  python3 --version
  ```
# *Project Flow*
1. Data Processing two CSV files querying using pyspark
   ```python3
   # Import necessary library
   from pyspark.sql import SparkSession
   from pyspark.sql.functions import col, format_number
   from pyspark.sql.types import DoubleType, IntegerType

   # Initilization Spark Session
   spark = SparkSession.builder.appName("Data Revenue").getOrCreate()
   ```
3. Data Visualization using Streamlit
