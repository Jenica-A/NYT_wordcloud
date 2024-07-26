
"""
Streamlit Interactive Plots Demo
    
Example of a line chart of time-series simulation in Matplotlib
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import datetime


st.title("New York Times Topic Modelling")
st.text("This app will allow you to choose a range of dates, and a section from the New York Times and generate a wordcloud image, based on word frequency wihtin article excerpts")

data_path = ("./df_snip_filtered.csv")


@st.cache
def load_data(nrows):
    df = pd.read_csv(data_path, nrows = nrows)
    df.dropna(inplace = True)
    df['pub_date']= pd.to_datetime(df['pub_date']).dt.date
    df = df[["pub_date","section_name","filtered"]]

    return df
df = load_data(1_000)

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(df)


start_date = st.date_input('Start date', min(df.pub_date))
end_date = st.date_input('End date', max(df.pub_date))
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

section_list = df.section_name.unique()
selection = st.selectbox(
     'Which section would you like to model?',
     section_list)

#filtered_data = df[df['pub_date'] == start_date]
st.subheader(f"Wordcloud of words in {start_date}")

filtered_data = df[(df['pub_date'] > pd.Timestamp(start_date)) & (df['pub_date'] < pd.Timestamp(end_date))]
filtered_data = filtered_data[(filtered_data.section_name == selection)]
text = " ".join(word for word in filtered_data.filtered)

#generate text from filtered column of df
text = " ".join(word for word in filtered_data.filtered)


# Create and generate a word cloud image:
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")

#@st.cache
def wordcloud_func(text):
    word_cloud = WordCloud( collocations = False, background_color = 'white',width=3000, height=2000, max_words=100, color_func = black_color_func ).generate(text)

    # Display the generated image:
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return(st.pyplot(plt))

wordcloud_func(text)

st.write("'More information is always better than less. When people know the reason things are happening, even if it's bad news, they can adjust their expectations and react accordingly. Keeping people in the dark only serves to stir negative emotions.' \n\n — Simon Sinek")

# Notes:
# - Switch from function to procedural
# - Lag in rendering
