# Load all the libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data into a pandas Dataframe
cars_df = pd.read_csv("C:/Users/gmode/TripleTen-course/car_advertisement/vehicles_us.csv")

# MARKET ANALYSIS
# Capitalize and update certain 'type' values
cars_df['type'] = cars_df['type'].str.capitalize()
cars_df['type'] = cars_df['type'].replace('Suv', 'SUV')
cars_df['type'] = cars_df['type'].replace('Mini-van', 'Minivan')

# Create header and description
st.header('Market analysis')
st.write('Filter the data below based on car type and model year to see the car market availability and details.')

# Retrieve list of all values for 'type'
type_unique = cars_df['type'].unique()

# Create car type dropdown
type_menu = st.selectbox('Select a car type:', type_unique)

# Create slider based on 'model_year'
min_year = int(cars_df['model_year'].min())
max_year = int(cars_df['model_year'].max())
year_slider = st.slider('Choose year', value=(min_year, max_year), min_value=min_year, max_value=max_year)
actual_range = list(range(year_slider[0], year_slider[1]+1))

# Create filtering ability for dropdown and slider
cars_df__filter = cars_df[(cars_df['type'] == type_menu) & (cars_df['model_year'].isin(list(actual_range)))]
cars_df__filter

# PRICE ANALYSIS 1
# Capitalize columns names and update column value
cars_df.columns = cars_df.columns.str.capitalize()
cars_df.rename(columns={'Type': 'Body_type'}, inplace=True)

# Create header and description
st.header('Price analysis')
st.write('What influences prices the most when considering car characteristics? Here we can compare the price distributions between transmission, fuel type, body type, and condition of the car.')
st.write('**NOTE**: Excludes prices over 150k')

# Create list of variables to compare to price
prices_list = ['Transmission', 'Fuel', 'Body_type', 'Condition']

# Create price variable dropdown
prices_menu = st.selectbox('Select a variable of price distribution:', prices_list)

# Create price histogram
price_fig = px.histogram(cars_df, x='Price', color=prices_menu, range_x=[0, 150000])
price_fig.update_layout(title='<b> Price distribution by {}</b>'.format(prices_menu))
st.plotly_chart(price_fig)

#PRICE ANALYSIS 2
# Create description
st.write('Now, let\'s compare the price distributions based on age characteristics. Below we look to compare the odometer usage and # of days the car has been listed relative to its age.')

# Add age of the car column to DataFrame
cars_df['Car_age'] = 2024 - cars_df['Model_year']

# Create function for different age groups
def age_category(i):
    if i<5:
        return '<5'
    elif i>=5 and i<10:
        return '5-10'
    elif i>=10 and i<20:
        return '10-20'
    else:
        return '>20'

# Apply function to Dataframe
cars_df['Age_category'] = cars_df['Car_age'].apply(age_category)
print(cars_df.head())

# Create list of variables to compare to price relative to age
price_age_list = ['Odometer', 'Days_listed']

# Create price to age variable dropdown
price_age_menu = st.selectbox('Select a variable of price distribution:', price_age_list)

# Create price to age scatterplot
price_age_fig = px.scatter(cars_df, x='Price', y=price_age_menu, color='Age_category', hover_data=['Model_year'])
price_age_fig.update_layout(title='<b> Price vs {}</b>'.format(price_age_menu))
st.plotly_chart(price_age_fig)














#cars_df['date_posted'] = pd.to_datetime(cars_df['date_posted'], format='%Y-%m-%d')
#cars_df['date_posted_year'] = cars_df['date_posted'].dt.year

#print(cars_df.sample(10))









