import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

df_time_series_confirmed = pd.read_csv("csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv")

def dataVizApp():
    country = input("Which country would you like? ").capitalize()
    df_time_series_confirmed_search = df_time_series_confirmed.loc[df_time_series_confirmed['Country/Region'] == country]
    df_transposed = df_time_series_confirmed_search.T
    df_transposed.reset_index(inplace = True) 
    
#     Grab the name of the columns for each new country 
    columns = []
    for col in df_transposed.columns: 
        columns.append(col)

#     Grab the value of what will tell whether its region or not
    provinceCheck = df_transposed[columns[1]].iloc[0]

    if type(provinceCheck) == str:
        df_transposed.columns = df_transposed.iloc[0]
        df_transposed = df_transposed.rename(columns={'Province/State': 'Date'})
    else: 
        df_transposed.columns = df_transposed.iloc[1]
        df_transposed = df_transposed.rename(columns={'Country/Region': 'Date'})

    df_transposed = df_transposed.drop([0,1,2,3])
    
#     Testing to see things are working - they are as of 7:14 3.24
#     final = df_transposed.head()
#     return final

#     Now testing to see if I can make it work with a map

    columns_mapping = []
    for col in df_transposed.columns: 
        columns_mapping.append(col) 
        
#     Create a line plot for the country or the region
    labels = [columns_mapping[1]]  # can also change the [1] to [1:4] to grab multiple in the case of china
    fig = df_transposed.plot(x = columns_mapping[0], 
                   y= labels, 
                   title = f'Line Plot of COVID-19 Confirmed Cases in {labels}')
    plt.legend(labels)
    plt.ylabel('Number of Cases')
    fig.get_figure().savefig(f'{country}.png')    

    img = Image.open(f'{country}.PNG')      
    img.show()
    return 

dataVizApp()