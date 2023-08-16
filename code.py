import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px # for data visualization
from textblob import TextBlob # for sentiment analysis

#save csv file as dataframe camed df
data=pd.read_csv('netflix_titles.csv')

###cleaning the data 
#check dataframe for null values
data.isnull().any().any()

#count null values per column
null_counts = data.isnull().sum()

print(null_counts)

#find the percentage of null values per column
null_percentage = data.isnull().sum() / len(data) * 100
print(null_percentage)

#create a new dataframe without null values called 'df'
df = data.dropna()

#check dataframe for null values
df.isnull().any().any()

# Check for duplicate rows
duplicated_rows = df.duplicated()
duplicated_rows 

# Check for duplicate rows
df.duplicated().any().any()

# Get the number of rows and columns
num_rows, num_columns = df.shape

print("Number of rows:", num_rows)
print("Number of columns:", num_columns)

# Show columns
df.columns

#show dataframe's first ten lines
df.head(10)

#show dataframe's last ten lines
df.tail(10)

df.info()

#count releases by year
releases_count_by_year = df['release_year'].value_counts()
releases_count_by_year_sort = releases_count_by_year.sort_values(ascending = False)
releases_count_by_year_sort

#How many releases in the action genre
action_releases_count = df[df['listed_in'].str.contains('Action', case=False)].shape[0]
print("Number of action releases:", action_releases_count)

#How many releases in the drama genre
drama_releases_count = df[df['listed_in'].str.contains('Dramas', case=False)].shape[0]
print("Number of Dramas releases:", drama_releases_count)

#How many releases have 'woman' in their description
woman_descp = df[df['description'].str.contains('woman', case=False)].shape[0]
print("Number of releases about women", woman_descp)

#How many releases have 'man' in their description
man_descp = df[df['description'].str.contains('man', case=False)].shape[0]
print("Number of releases about men", man_descp)


#distribution of content ratings on Netflix
z = df.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rating', 
                  title='Distribution of Content Ratings on Netflix',
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()


"""The majority of content on Netflix is categorized as “TV-MA”, 
which means that most of the content available on Netflix is intended 
for viewing by mature and adult audiences.
"""
### Top 5 directors

data['director']=data['director'].fillna('No Director Specified')
filtered_directors=pd.DataFrame()
filtered_directors=data['director'].str.split(',',expand=True).stack()
filtered_directors=filtered_directors.to_frame()
filtered_directors.columns=['Director']
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
directors=directors[directors.Director !='No Director Specified']
directors=directors.sort_values(by=['Total Content'],ascending=False)
directorsTop5=directors.head()
directorsTop5=directorsTop5.sort_values(by=['Total Content'])
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
fig1.show()


df1=data[['type','release_year']]
df1=df1.rename(columns={"release_year": "Release Year"})
df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content')
df2=df2[df2['Release Year']>=2010]
fig3 = px.line(df2, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
fig3.show()

"""there has been a decline in the production of the content for both movies 
and other shows since 2018"""