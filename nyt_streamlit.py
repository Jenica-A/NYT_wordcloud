
"""
Streamlit Interactive Plots Demo
    
Example of a line chart of time-series simulation in Matplotlib
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("New York Times Topics")
st.write("'More information is always better than less. When people know the reason things are happening, even if it's bad news, they can adjust their expectations and react accordingly. Keeping people in the dark only serves to stir negative emotions.' \n\n — Simon Sinek")

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.read_csv("./Documents/Metis/Module_7_Engineering/nyt_test.csv")

df
'''
pub_date = st.slider('Publicaiton Date',  min_value=0.001, max_value=0.10, step=0.01)
section_name = st.slider('Section',min_value=0.01,  max_value=0.10, step=0.01)
st.write(f"Publicaiton Date = {pub_date} \n\n Section = {section_name}")

intial_value = 1
n_series = 10 
time_series = np.cumprod(intial_value + np.random.normal(trend, noise, (100, n_series)), 
                         axis=0)

# st.line_chart(time_series)

fig, ax = plt.subplots()
for ts in time_series.T:
    ax.plot(ts)

st.pyplot(fig)
'''
# Notes:
# - Switch from function to procedural
# - Lag in rendering
# - When you deploy you have to add an external dependency file (requirements.txt)
