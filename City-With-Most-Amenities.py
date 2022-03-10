# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details

df['n_amenities']=df['amenities'].apply(lambda x : len(str.split(x,',')))

df1 = df.groupby('city').sum().reset_index()

city = df1[df1.n_amenities == df1.n_amenities.max()].iat[0, 0]
