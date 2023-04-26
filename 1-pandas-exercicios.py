# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Ler e exibir um arquivo CSV usando pandas

# COMMAND ----------

import numpy as np
import pandas as pd

df = spark.read.csv("/FileStore/tables/retail.csv", header=True, sep=',')
df = df.toPandas()

df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Selecionar colunas específicas de um DataFrame usando pandas

# COMMAND ----------

df.filter(['stock_code', 'unit_price'])

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Filtrar linhas com base em uma condição usando pandas

# COMMAND ----------

df.query('invoice_no == "536368"')

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Agrupar dados com base em uma coluna usando pandas

# COMMAND ----------

df.sort_values('invoice_date').head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Usar a função max em alguma coluna do DataFrame

# COMMAND ----------

grouped_by_region = df.groupby('invoice_no').agg({'stock_code': 'count'}).reset_index().head()
print(df)

# COMMAND ----------

