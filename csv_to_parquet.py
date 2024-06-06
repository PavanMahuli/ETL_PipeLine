import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


def main():
    ## @params: [JOB_NAME]
    df = spark.read.csv('s3://mybucketgithubactions/test3.csv', header = True)
    df.repartition(1).write.mode('append').parquet("s3a://mybucketgithubactions/github_action2/publish/")

main()
