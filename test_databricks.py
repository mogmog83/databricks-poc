# 'test_databricks.py' 파일을 생성하고 기본 Spark 코드를 넣습니다.
@'
# Databricks Spark Test Script
from pyspark.sql import SparkSession

# Spark 세션 확인
spark = SparkSession.builder.getOrCreate()

# 샘플 데이터 생성
data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])

# 결과 출력
df.show()
print("Databricks 연결 테스트 성공!")
'@ | Out-File -FilePath test_databricks.py -Encoding utf8