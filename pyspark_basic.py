# Basic pyspark example

data = [("Alice", 25), ("Bob", 30), ("Clara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.filter(df.Age > 23).show()
