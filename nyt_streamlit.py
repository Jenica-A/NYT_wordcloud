
"""
Streamlit Interactive Plots Demo
    
Example of a line chart of time-series simulation in Matplotlib
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("New York Times Topics")
st.write("'More information is always better than less. When people know the reason things are happening, even if it's bad news, they can adjust their expectations and react accordingly. Keeping people in the dark only serves to stir negative emotions.' \n\n — Simon Sinek")

trend = st.slider('Trend',  min_value=0.001, max_value=0.10, step=0.01)
noise = st.slider('Noise',min_value=0.01,  max_value=0.10, step=0.01)
st.write(f"Trend = {trend} \n\n Noise = {noise}")

intial_value = 1
n_series = 10 
time_series = np.cumprod(intial_value + np.random.normal(trend, noise, (100, n_series)), 
                         axis=0)

# st.line_chart(time_series)

fig, ax = plt.subplots()
for ts in time_series.T:
    ax.plot(ts)

st.pyplot(fig)

# Notes:
# - Switch from function to procedural
# - Lag in rendering
# - When you deploy you have to add an external dependency file (requirements.txt)
