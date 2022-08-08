

"""
Streamlit Interactive 
New York Times Article Archive Topic Modelling
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF



st.title("Topic Modeling the New York Times")
st.subheader("January 2020 to August 2022")
st.caption("'More information is always better than less. When people know the reason things are happening, even if it's bad news, they can adjust their expectations and react accordingly. Keeping people in the dark only serves to stir negative emotions.' \n\n — Simon Sinek")

st.write("Choose a range of dates and newspaper sections to generate a wordcloud from terms used in article 'snippets'")

data_path = ("./df_snip_filtered.csv")


@st.cache
def load_data(nrows):
    df = pd.read_csv(data_path, nrows = nrows)
    df.dropna(inplace = True)
    df['pub_date']= pd.to_datetime(df['pub_date']).dt.date
    df = df[["pub_date","section_name","filtered"]]

    return df
df = load_data(1_39000)

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
selections = ['U.S.','Arts','World']
selections = st.multiselect(
     'Choose at least one section to model (by default all sections are shown)',
     section_list, default = section_list)

st.caption(f"Wordcloud of terms in articles from {start_date} to {end_date} in the following section(s): {selections}")
st.caption(f"Larger words appear more frequently")

filtered_data = df[(df['pub_date'] > pd.Timestamp(start_date)) & (df['pub_date'] < pd.Timestamp(end_date))]
#filtered_data = filtered_data[(filtered_data['section_name'].isin(selections).any(selections))]
filtered_data = filtered_data[(filtered_data['section_name'].isin(selections))]
text = " ".join(word for word in filtered_data.filtered)

#generate text from filtered column of df
text = " ".join(word for word in filtered_data.filtered)


# Create and generate a word cloud image:
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")

#@st.cache
def wordcloud_func(text):
    word_cloud = WordCloud(collocations = False, background_color = 'white',width=3000, height=2000, max_words=200, color_func = black_color_func).generate(text)

    # Display the generated image:
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return(st.pyplot(plt))

wordcloud_func(text)


article_count = 5000
df_snip_trim = df.sample(n=article_count)#, random_state = 42)

corpus_snow = list(df_snip_trim.filtered)
indx_label = [e[:100]+"..." for e in df_snip_trim.filtered]
cv = CountVectorizer(stop_words = 'english', min_df = 6, max_df = .95, ngram_range=(1, 3))
#using the snowball stemmed data for the dtm
X_snow = cv.fit_transform(corpus_snow)
dtm_snow = pd.DataFrame(X_snow.toarray(), index=indx_label, columns=cv.get_feature_names_out())
dtm_snow


nmf = NMF(15, init = "nndsvda") 
nmf.fit(dtm_snow)
#st.write('You selected:', section_name)

topic_term = nmf.components_.round(3)


topic_term_df = pd.DataFrame(topic_term, columns = cv.get_feature_names_out())


def display_topics(model, feature_names, no_top_words, topic_names = None): 
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix + 1)
        else:
            print("\nTopic: ", topic_names[ix])
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))
    print("\n")
    return model, feature_names, no_top_words

output = display_topics(nmf, cv.get_feature_names_out(), 10)

st.write(output)
#st.write(f"Publicaiton Date = {pub_date} \n\n Section = {section_name}")

#intial_value = 1
#n_series = 10 
#time_series = np.cumprod(intial_value + np.random.normal(trend, noise, (100, n_series)), 
#                         axis=0)

#for ts in time_series.T:
#    ax.plot(ts) 

#st.pyplot(fig)

# Notes:
# - Switch from function to procedural
# - Lag in rendering
# - When you deploy you have to add an external dependency file (requirements.txt)
