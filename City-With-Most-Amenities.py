# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details

df['n_amenities']=df['amenities'].apply(lambda x : len(str.split(x,',')))

df1 = df.groupby('city').sum().reset_index()

city = df1[df1.n_amenities == df1.n_amenities.max()].iat[0, 0]

#Method 2
df1 = df[['amenities', 'city']]

#split the amenities string into a list by calling the split method.
df1['amenities'] = df1['amenities'].str.split(',')

#invoke the explode() method on the amenities column.
df2 = df1.explode('amenities')

#aggregate by city
df2.groupby('city', as_index = False)['amenities'].agg('count').sort_values(by = ['amenities'], ascending = False)['city'].iloc[0]

#df2.groupby('city', as_index = False).agg({'amenities' : 'count'})
