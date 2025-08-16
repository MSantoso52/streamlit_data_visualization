# streamlit_data_visualization
# *Overview*
Repo project to demonstrate Data visualization using Streamlit, input data from customer_data.csv & order_data.csv file through data processing using PySpark to revenue_data.csv. Using Streamlit to display the dashboard into web through localhost:8051 or URL: 192.168.249:8051
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
   ```python3
   join_df = spark.sql(join_query)
    formated_df = join_df.withColumn("REVENUE", join_df["REVENUE"].cast(DoubleType()))

    if formated_df is not None:
        formated_df.printSchema()
        formated_df.show(10)
        formated_df.write \
            .mode("overwrite") \
            .option("header",True) \
            .csv("/home/mulyo/Learning/ELT/Converted")

    spark.stop()
   ```
3. Data Visualization using Streamlit
