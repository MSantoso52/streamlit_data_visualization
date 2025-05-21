from pyspark.sql import SparkSession
from pyspark.sql.functions import col, format_number
from pyspark.sql.types import DoubleType, IntegerType

# Initilization Spark Session
spark = SparkSession.builder.appName("Data Revenue").getOrCreate()

def csvToSpark(file_path, header=True, infer_schema=True):
    
    try:
        df = spark.read.csv(file_path, header=header, inferSchema=infer_schema)
        print(f"Successfully reading at :{file_path}")
        return df
    except Exception as e:
        print(f"Error reading at :{file_path}")
        return None

if __name__=="__main__":

    CUSTOMER_PATH = "customer_data.csv"
    ORDER_PATH= "order_data.csv"

    customer_df = csvToSpark(CUSTOMER_PATH)

    if customer_df is not None:
        customer_df.printSchema()
        customer_df.show(5)

    order_df = csvToSpark(ORDER_PATH)

    if order_df is not None:
        order_df.printSchema()
        order_df.show(5)

    # Register data frame as table for SQL purpose
    customer_df.createOrReplaceTempView("customers")
    order_df.createOrReplaceTempView("orders")

    # query to join two df
    join_query = """
        SELECT
            C.customer_id AS CUSTOMERID,
            C.full_name AS CUSTOMER_NAME,
            COUNT(DISTINCT O.order_id) AS ORDER_COUNT,
            SUM(O.unit_price * O.total_price) AS REVENUE
        FROM
            customers C
        JOIN
            orders O ON C.customer_id=O.customer_id 
        GROUP BY
            CUSTOMERID,
            CUSTOMER_NAME
        ORDER BY
            REVENUE DESC
    """

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
