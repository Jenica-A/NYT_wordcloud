
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

data_path = ("./df_snip_filtered.csv")

@st.cache
def load_data(nrows):
    df = pd.read_csv(data_path, nrows = nrows)
    df.dropna(inplace = True)
    df['pub_date']= pd.to_datetime(df['pub_date'])    
    return df
df = load_data(1_2000)
df

date_filter = st.slider('pub_date', min_value=1, max_value=100, step=0.01) 

#generate text from filtered column of df
text = " ".join(word for word in df.filtered)

from wordcloud import WordCloud#, STOPWORDS, ImageColorGenerator
# Create and generate a word cloud image:
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


#this visualization formatting code was shared with me by Leaha Nagy, a fellow Metis student.
# change the value to black
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
# set the wordcloud background color to white
# set max_words to 1000
# set width and height to higher quality, 3000 x 2000
word_cloud = WordCloud(collocations = False, background_color = 'white',width=3000, height=2000, max_words=500).generate(text)
#wordcloud = WordCloud(font_path = '/Library/Fonts/Arial Unicode.ttf', background_color="white", width=3000, height=2000, max_words=500).generate_from_frequencies(df['porter'])
# set the word color to black
word_cloud.recolor(color_func = black_color_func)
# set the figsize
plt.figure(figsize=[15,10])
# plot the wordcloud
plt.imshow(word_cloud, interpolation="bilinear")
# remove plot axes
plt.axis("off")
# save the image
plt.savefig('word_cloud_all.png')



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
