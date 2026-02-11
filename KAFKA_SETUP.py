# Databricks notebook source
# MAGIC %sh
# MAGIC wget https://archive.apache.org/dist/kafka/3.2.0/kafka_2.12-3.2.0.tgz
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC tar -xvzf kafka_2.12-3.2.0.tgz
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l kafka_2.12-3.2.0
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC cd kafka_2.12-3.2.0/
# MAGIC bin/zookeeper-server-start.sh config/zookeeper.properties

# COMMAND ----------

# MAGIC %sh
# MAGIC cd kafka_2.12-3.2.0
# MAGIC  bin/kafka-server-start.sh config/server.properties > kafka.log 2>&1 &
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC cd kafka_2.12-3.2.0/
# MAGIC bin/zookeeper-server-start.sh config/zookeeper.properties

# COMMAND ----------

# MAGIC %sh
# MAGIC cd kafka_2.12-3.2.0
# MAGIC bin/kafka-topics.sh --create --topic test-databricks --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# COMMAND ----------

# MAGIC %sh
# MAGIC ps -ef | grep zookeeper
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC nohup kafka_2.12-3.2.0/bin/kafka-server-start.sh kafka_2.12-3.2.0/config/server.properties > kafka.log 2>&1 &
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC cd kafka_2.12-3.2.0
# MAGIC echo -e "Hello\nKafka\nFrom\nDatabricks" | bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test-databricks
