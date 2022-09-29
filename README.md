# A Data Pipeline for Topic Modeling the New York Times
### Data Engineering Project Write-Up
### Jenica Andersen
#### Metis DSML Data Engineering Module, August 9, 2022

#### Abstract
Large amounts of data are gathered, stored, leveraged, and shared continuously across the planet today. Being able to handle the data, process it and tell a story with it is powerful, especially when done well. The stories can share insights that allow organizations or individuals to connect with people in more effective ways. Our client wants to connect with consumers, and wants to have clearer contextualization around past events in order to create more pointed and meaningful consumer-focused communications.  To help our client succeed, this project illustrates and executes an end-to-end data pipeline. Data are gathered from the New York Times (NYT) application program interface (API) by way of a series of get requests. The data were then stored and cleaned in SQL and pandas. An Amazon Web Services(AWS) EC2 instance was used to deploy jupyter notebooks, create word use visualizations and run topic modeling. AWS S3 was used to store the large dataset files. Ultimately, a user-controlled Streamlit app was created to share results.  

#### Design
The design for this project includes the data pipeline described in the abstract. 
1. Interact with the NYT API via a series of 'get' requests to pull article archive data from their database. 
2. Unpack the raw data json with pandas. 
3. Move data into a sql database, where the data is cleaned, queried, and saved in an AWS S3 bucket. 
4. Conduct topic modeling via python code, executed within a jupyter notebook that is hosted on an aws EC2 instance. 
5. Make the Cleaned and modeled data available to streamlit .py files that are used to build an end-user controlled application.

#### Data
As stated above, the data, accessed via the NYT archives API is in a raw json format. Converted to tabular data, it included about 10 years of articles (747,468 articles) with 20 columns of article information. (Entire articles were not included in the data set.) Columns of interest include: publication date, abstract or snippet, headline, key words, lead paragraph, and section name. 

#### Algorithms
The bulk of this project focused on end-to-end data engineering. Machine Learning Algorithms were used in the data gathering and processing stage of this data pipeline project. *Request* was used to access data from the NYT API, *wordcloud* was used to generate the word use visualizations, *Non-negative Matrix Factorization* was used to conduct topic modeling.

#### Tools
The tools used in this project include: Jupyter Notebook (the IDE for writing code), New York Times Developer API, pandas for conversion of the json file to a dataframe and then a .csv, DB Browser for SQLite for cleaning and processing data on my local machine, AWS EC2 for running topic modeling on the large dataset, S3 for storing the large .csv files, streamlit for building the end user applicaiton, and github for hosting files and streamlit code. 

#### Communication
This project resulted in the creation of a streamlit app which can be found [here](https://jenica-a-nyt-wordcloud-nyt-app-uqe5rx.streamlitapp.com/). (Due to intermittent app functioning, a simplified version of the app--with reduced date range and selection of only one New York Times section--can be found [at this link](https://jenica-a-nyt-wordcloud-nyt-streamlit-adel68.streamlitapp.com/). Please also see accompanying presentation and jupyter notebook code files located in [this github repository](https://github.com/Jenica-A/NYT_wordcloud).

