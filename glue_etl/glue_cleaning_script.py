import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1770829358598 = glueContext.create_dynamic_frame.from_catalog(database="amazon_reviews_db", table_name="amazon", transformation_ctx="AmazonS3_node1770829358598")

# Script generated for node SQL Query
SqlQuery0 = '''
SELECT
product_id,
product_name,
category,

CAST(REPLACE(REPLACE(discounted_price,'₹',''),',','') AS DOUBLE) AS discounted_price,

CAST(REPLACE(REPLACE(actual_price,'₹',''),',','') AS DOUBLE) AS actual_price,

CAST(REPLACE(discount_percentage,'%','') AS DOUBLE) AS discount_percentage,

rating.double AS rating,

CAST(REPLACE(rating_count,',','') AS DOUBLE) AS rating_count,

about_product,
user_id,
user_name,
review_id,
review_title,
review_content

FROM myDataSource
WHERE rating.double BETWEEN 1 AND 5



'''
SQLQuery_node1770829390111 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":AmazonS3_node1770829358598}, transformation_ctx = "SQLQuery_node1770829390111")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1770829390111, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1770829193203", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1770829677543 = glueContext.write_dynamic_frame.from_options(frame=SQLQuery_node1770829390111, connection_type="s3", format="glueparquet", connection_options={"path": "s3://amazon-return-analytics/processed/", "partitionKeys": []}, format_options={"compression": "uncompressed"}, transformation_ctx="AmazonS3_node1770829677543")

job.commit()