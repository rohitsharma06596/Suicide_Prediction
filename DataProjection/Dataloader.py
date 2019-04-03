
import pandas
from pyspark.sql import SparkSession

def init_spark():
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    return spark

def datasetLoader(filename):
    df = pandas.read_excel(filename, sheet_name=0)
    df.columns = df.columns.str.strip()
    print("I am here")
    print(df)

datasetLoader("/Users/rohitsharma/PycharmProjects/Suicide_Prediction/Big Data Datasets/Causes/CausesStats2001-2012.xls")