import sqlite3
import pandas as pd

# create database
connection = sqlite3.connect('../data/database/fire_data.db')
cursor = connection.cursor()

# create table if does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS [Number of fires by month] (Jurisdiction text, Month text, Year int, Number int, [Data Qualifier] text)")

# load csv data then write to a new sqlite table
monthly_fires = pd.read_csv('../data/original/number_fires_by_month.csv')
monthly_fires.to_sql('Number of fires by month', connection, if_exists='replace', index = False)

# stack all the monthly fire data into yearly data, then save to csv for D3.js processing
# cursor.execute("SELECT year, SUM(Number) FROM [Number of fires by month] GROUP BY year")
# print(cursor.fetchall())

yearly_fires = pd.read_sql("SELECT year, SUM(Number) FROM [Number of fires by month] GROUP BY year", connection)
print(yearly_fires)
# save
yearly_fires.to_csv('yearly_fires.csv', index = False)