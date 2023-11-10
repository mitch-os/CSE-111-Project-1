# #Jie Jenn on Youtube 'Upload A CSV File' youtube.com/watch?v=UZIhVmkrAEs

# import sqlite3
# import pandas as pd

# connection = sqlite3.connect('data.db')

# dr = pd.read_csv('drivers.csv')

# dr.columns = dr.columns.str.strip() #gets rid of spaces

# dr.to_sql('drivers', connection, if_exists ='replace')

# ds = pd.read_csv('bus.csv')

# ds.columns = ds.columns.str.strip()

# ds.to_sql('busses', connection, if_exists='replace')

# dt = pd.read_csv('routes.csv')

# dt.columns = dt.columns.str.strip() #gets rid of spaces

# dt.to_sql('routes', connection, if_exists='replace')

# du = pd.read_csv('schedule.csv')

# du.columns = du.columns.str.strip()

# du.to_sql('schedule', connection, if_exists='replace')

# dv = pd.read_csv('busstops.csv')

# dv.columns = dv.columns.str.strip()

# dv.to_sql('busstops', connection, if_exists='replace')

# connection.close()