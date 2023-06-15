import sqlite3
import pandas as pd

# create database
connection = sqlite3.connect('../data/database/fire_data.db')
cursor = connection.cursor()

# number of fires by year
# create table if does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS [Number of fires by month] (Jurisdiction text, Month text, Year int, Number int, [Data Qualifier] text)")

# load csv data then write to a new sqlite table
# I want to add more recent 2022 and 2023 data and onwards in the future, so using a proper database will be preferred.
monthly_fires = pd.read_csv('../data/original/number_fires_by_month.csv')
monthly_fires.to_sql('Number of fires by month', connection, if_exists='replace', index = False)

# sum all the monthly fires add into a row for each year, then save this into a csv for D3 processing.
yearly_fires = pd.read_sql("SELECT year, SUM(Number) FROM [Number of fires by month] GROUP BY year", connection)
print(yearly_fires)
# save
yearly_fires.to_csv('yearly_fires.csv', index = False)


# repeat for other tables
cursor.execute("CREATE TABLE IF NOT EXISTS [Area burned by Month] (Jurisdiction text, Month text, Year int, [Data Qualifier] text, [Area (hectares) null] real)")

# new sql database
monthly_area_fire = pd.read_csv('../data/original/area_burned_by_month.csv')
monthly_area_fire.to_sql('Area burned by Month', connection, if_exists='replace', index = False)

yearly_area_burned = pd.read_sql("SELECT year, SUM([Area (hectares) null]) FROM [Area burned by Month] GROUP BY year", connection)
print(yearly_area_burned)
# save
yearly_area_burned.to_csv('yearly_area_burned.csv', index = False)






