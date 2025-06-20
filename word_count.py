# Word count

text = ["hello world", "hello spark", "spark is fast"]

rdd = sc.parallelize(text)
word_counts = (
    rdd.flatMap(lambda line: line.split())
       .map(lambda word: (word, 1))
       .reduceByKey(lambda a, b: a + b)
)
word_counts.collect()
