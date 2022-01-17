import streamlit as st
import nltk
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

global simular, show_value_of_element, i1, i2, i3, i4
df = pd.read_csv('prog_book.csv')
df.head()

nltk.download('stopwords')
stop = stopwords.words('english')
stop = set(stop)


def lower(text):
    return text.lower()


from string import punctuation


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punctuation))


def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop])


def remove_digits(text):
    return re.sub(r'\d+', '', text)


def clean_text(text):
    text = lower(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = remove_digits(text)
    return text


df['clean_Book_title'] = df['Book_title'].apply(clean_text)
df.head()
df['clean_Description'] = df['Description'].apply(clean_text)
df.head()

vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
X = vectorizer.fit_transform(df['clean_Book_title'])
title_vectors = X.toarray()
desc_vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
Y = desc_vectorizer.fit_transform(df['clean_Description'])
desc_vectors = Y.toarray()


def get_recommendations_posters(value_of_element, feature_locate, vectors_array, feature_show):
    global simular, show_value_of_element, i1, i2, i3, i4

    index_of_element = df[df[feature_locate] == value_of_element].index.values[0]

    show_value_of_element = df.iloc[index_of_element][feature_show]

    df_without = df.drop(index_of_element).reset_index().drop(['index'], axis=1)

    vectors_array = list(vectors_array)

    target = vectors_array.pop(index_of_element).reshape(1, -1)

    vectors_array = np.array(vectors_array)

    most_similar_sklearn = cosine_similarity(target, vectors_array)[0]

    idx = (-most_similar_sklearn).argsort()

    all_values = df_without[[feature_show]]

    for _ in idx:
        simular = all_values.values[idx]
    i1 = df[df['Book_title'] == simular[0][0]].index.values[0]
    i2 = df[df['Book_title'] == simular[1][0]].index.values[0]
    i3 = df[df['Book_title'] == simular[2][0]].index.values[0]
    i4 = df[df['Book_title'] == simular[3][0]].index.values[0]

    return


st.title("R-M-A Book Recommendation ")
df = pd.read_csv('prog_book.csv')

nltk.download('stopwords')
stop = stopwords.words('english')
stop = set(stop)

df['clean_Book_title'] = df['Book_title'].apply(clean_text)
df.head()
df['clean_Description'] = df['Description'].apply(clean_text)
df.head()

vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
X = vectorizer.fit_transform(df['clean_Book_title'])
title_vectors = X.toarray()
desc_vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
Y = desc_vectorizer.fit_transform(df['clean_Description'])
desc_vectors = Y.toarray()


books_dict = pd.read_csv('prog_book.csv')
books = pd.DataFrame(books_dict)


tk = 0
pages = st.sidebar.selectbox('Chose your mode (Default : Search mode) ', ['Search mode', 'Library Mode'])
if pages == 'Search mode':
    col1, col2 = st.columns([10, 1])
    
    with col1:
        selected_book_name = st.selectbox('Enter book name that you liked : ', books['Book_title'].values)

        b1 = st.button('Search')
        '\n'
        '\n'
        '\n'

        if b1:
            st.balloons()
            tk = 1
    if tk == 1:
        import time

        my_bar = st.progress(0)

        for x in range(100):
            time.sleep(0.01)
        my_bar.progress(x + 1)

    if tk == 1:
        col1, col2 = st.columns([1.5, 5])

        i0 = df[df['Book_title'] == selected_book_name].index.values[0]

        with col1:
            st.image(df['image'].values[i0],
                     caption=selected_book_name,
                     width=150)
        with col2:
            st.write("Description : ",
                     df['Description'].values[i0])
            st.write("Rating : ",
                     df['Rating'].values[i0])
            st.write("Price : ",
                     df['Price'].values[i0])
            st.write("Reviews : ",
                     df['Reviews'].values[i0])
            st.write("No. Of Pages : ",
                     df['Number_Of_Pages'].values[i0])

        '\n'
        '\n'
        '\n'
        '\n'
        st.title('You May Also Like.....')
        '\n'
        '\n'
        st.success('Recommending books similar to ' + selected_book_name)
        get_recommendations_posters(selected_book_name, 'Book_title', title_vectors, 'Book_title')
        if tk == 1:
            with st.expander('Click To Show Recommendations'):
                '\n'
                '\n'
                '\n'
                
                st.progress(0)
                if tk == 1:
                    col1, col2 = st.columns([1.5, 5])
                    with col1:
                        st.image(df['image'].values[i1],
                                 caption=df['Book_title'].values[i1],
                                 width=150)

                        '\n'
                        

                    with col2:
                        
                        st.write("Description : ",
                                 df['Description'].values[i1])
                        st.write("Rating : ",
                                 df['Rating'].values[i1])
                        st.write("Price : ",
                                 df['Price'].values[i1])
                        st.write("Reviews : ",
                                 df['Reviews'].values[i1])
                        st.write("No. Of Pages : ",
                                 df['Number_Of_Pages'].values[i1])
                        '\n'
                        '\n'
                        '\n'
                        '\n'
                       
                        
                st.progress(0)
                if tk == 1:
                    col1, col2 = st.columns([1.5, 5])
                    with col1:
                        st.image(df['image'].values[i2],
                                 caption=df['Book_title'].values[i2],
                                 width=150)

                        '\n'
                        

                    with col2:
                        
                        st.write("Description : ",
                                 df['Description'].values[i2])
                        st.write("Rating : ",
                                 df['Rating'].values[i2])
                        st.write("Price : ",
                                 df['Price'].values[i2])
                        st.write("Reviews : ",
                                 df['Reviews'].values[i2])
                        st.write("No. Of Pages : ",
                                 df['Number_Of_Pages'].values[i2])
                        '\n'
                        '\n'
                        '\n'
                        '\n'
                        
                st.progress(0)        
                if tk == 1:
                    col1, col2 = st.columns([1.5, 5])
                    with col1:
                        st.image(df['image'].values[i3],
                                 caption=df['Book_title'].values[i3],
                                 width=150)

                        '\n'

                    with col2:

                        st.write("Description : ",
                                 df['Description'].values[i3])
                        st.write("Rating : ",
                                 df['Rating'].values[i3])
                        st.write("Price : ",
                                 df['Price'].values[i3])
                        st.write("Reviews : ",
                                 df['Reviews'].values[i3])
                        st.write("No. Of Pages : ",
                                 df['Number_Of_Pages'].values[i3])
                        '\n'
                        '\n'
                        '\n'
                        '\n'
                st.progress(0)        
                if tk == 1:
                    col1, col2 = st.columns([1.5, 5])
                    with col1:
                        st.image(df['image'].values[i4],
                                 caption=df['Book_title'].values[i4],
                                 width=150)

                        '\n'

                    with col2:
                        
                        st.write("Description : ",
                                 df['Description'].values[i4])
                        st.write("Rating : ",
                                 df['Rating'].values[i4])
                        st.write("Price : ",
                                 df['Price'].values[i4])
                        st.write("Reviews : ",
                                 df['Reviews'].values[i4])
                        st.write("No. Of Pages : ",
                                 df['Number_Of_Pages'].values[i4])
                st.progress(0)
      
if pages == 'Library Mode':

    j = 0
    for i in books:
        while j < 271:
            st.progress(100)
            col1, col2 = st.columns([2, 5])
            with col1:
                st.image(df['image'].values[j],
                         caption=df['Book_title'].values[j],
                         width=198)
                st.button('------Download------', key=j)

            with col2:
                st.write("Description : ",
                         df['Description'].values[j])
                st.write("Rating : ",
                         df['Rating'].values[j])
                st.write("Price : ",
                         df['Price'].values[j])
                st.write("Reviews : ",
                         df['Reviews'].values[j])
                st.write("No. Of Pages : ",
                         df['Number_Of_Pages'].values[j])
                j+=1
with st.sidebar.expander("See explanation"):
    '\n'
    
    st.write("""when you select a book and click Search
                this Webapp will show you five books 
                like the book that you select  """)
    '\n'
    
               

       

with st.sidebar.expander("POWERED BY"):
    st.write(""" 
                LCT.Rana Ryad    \n                
                Student: \n
                Mohammed Khalid Ibrahim \n
                ALI Anmar Borhan  \n
                 """)
    
                





