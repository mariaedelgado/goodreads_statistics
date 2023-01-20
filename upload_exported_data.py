import sqlite3

import pandas as pd


# read data
df = pd.read_csv('data/2023-01-19_goodreads_library_export.csv')

# Filter columns
df = df[['Title', 'Author', 'ISBN', 'My Rating',
         'Average Rating', 'Date Added', 'Date Read']]

# rename columns
df.rename(
    columns={'Title': 'title', 'Author': 'author', 'ISBN': 'isbn', 'My Rating': 'my_rating',
             'Average Rating': 'average_rating', 'Date Added': 'date_start', 'Date Read': 'date_end'
             }, inplace=True)

# parse isbn
df.loc[:, 'isbn'] = df.loc[:, 'isbn'].str.replace('=', '').str.replace('"', '')

# set genre # TODO
df.loc[:, 'genre'] = ''

# Create your connection.
try:
    cnx = sqlite3.connect('data/Bookshelf.db')
    df.to_sql(name='Books', con=cnx, if_exists='replace')
finally:
    cnx.close()
