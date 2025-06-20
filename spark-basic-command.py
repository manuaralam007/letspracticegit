from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
