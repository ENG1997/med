import streamlit as st
import nltk
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

global simular, show_value_of_element, i1, i2, i3, i4, i5
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
    global simular, show_value_of_element, i1, i2, i3, i4, i5

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
    i5 = df[df['Book_title'] == simular[4][0]].index.values[0]

    return


st.set_page_config(page_title="RAM Library", page_icon="🧊", initial_sidebar_state="collapsed",
                   menu_items={
                       'Get help': 'https://www.instagram.com/eng_mk97/',
                       'Report a bug': "https://www.instagram.com/eng_mk97/",
                       'About': "Project supervisor: ⠀⠀ ⠀⠀ ⠀⠀⠀ "
                                "⠀⠀ ⠀⠀ ⠀⠀ https://uomustansiriyah.edu.iq/e-learn/profile.php?id=2623 "
                                "Implementation and design:⠀⠀"
                                "⠀⠀⠀ ⠀https://www.instagram.com/eng_mk97 ⠀https://www.instagram.com/ali_anmar_17/"
                   }
                   )

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

tk = 0
books_dict = pd.read_csv('prog_book.csv')
books = pd.DataFrame(books_dict)
st.title('Recommendation system (ML)')
pages = st.sidebar.selectbox('Chose your mode (Default : All Books) ', ['All Books',
                                                                        'Collage of Engineering',
                                                                        'College of Medicine',
                                                                        'College of Dentistry',
                                                                        'College of Pharmacy '])
if pages == 'All Books':
    col1, col2 = st.columns([10, 1])

    with col1:
        selected_book_name = st.selectbox('Enter book name that you liked : ', books['Book_title'].values)

        b1 = st.button('Search')
        '\n'

        if b1:
            st.balloons()
            tk = 1
    if tk == 1:
        import time
        with st.spinner('Wait, Please...🧐'):
            time.sleep(3)
        my_bar = st.progress(0)
        x = 0
        for x in range(100):
            time.sleep(0.01)
        my_bar.progress(x + 1)

    if tk == 1:
        col1, col2 = st.columns([2.2, 5])

        i0 = df[df['Book_title'] == selected_book_name].index.values[0]

        with col1:

            st.image(df['image'].values[i0],
                     caption=selected_book_name,
                     width=198)

        with col2:

            if 1 <= df['Rating'].values[i0] < 2:
                rate = '⭐️'
            elif 2 <= df['Rating'].values[i0] < 3:
                rate = '⭐️ ⭐️ ️'
            elif 3 <= df['Rating'].values[i0] < 4:
                rate = '⭐️ ⭐️ ⭐️ ️'
            elif 4 <= df['Rating'].values[i0] < 5:
                rate = '⭐️ ⭐️ ⭐️ ⭐️'
            elif 5 <= df['Rating'].values[i0] < 6:
                rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
            st.write("Rating :       ", rate)
            st.write("Price :        $", df['Price'].values[i0])
            st.write("Reviews :      ", df['Reviews'].values[i0])
            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

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
                st.progress(100)

                if tk == 1:
                    col1, col2 = st.columns([2.2, 5])
                    with col1:
                        st.image(df['image'].values[i1],
                                 caption=df['Book_title'].values[i1],
                                 width=170)

                    with col2:

                        if 1 < df['Rating'].values[i1] < 2:
                            rate1 = '⭐️'
                        elif 2 < df['Rating'].values[i1] < 3:
                            rate1 = '⭐️ ⭐️ ️'
                        elif 3 < df['Rating'].values[i1] < 4:
                            rate1 = '⭐️ ⭐️ ⭐️ ️'
                        elif 4 < df['Rating'].values[i1] < 5:
                            rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                        elif 5 < df['Rating'].values[i1] < 6:
                            rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                        st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                        st.write("Rating :             ", rate1)
                        st.write("Price :              $", df['Price'].values[i1])
                        st.write("Reviews :            ", df['Reviews'].values[i1])
                        st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                        '\n'
                        '\n'
                        '\n'
                    st.progress(100)

                    col1, col2 = st.columns([2.2, 5])
                    with col1:
                        st.image(df['image'].values[i2],
                                 caption=df['Book_title'].values[i2],
                                 width=170)

                    with col2:

                        if 1 <= df['Rating'].values[i2] < 2:
                            rate2 = '⭐️'
                        elif 2 <= df['Rating'].values[i2] < 3:
                            rate2 = '⭐️ ⭐️ ️'
                        elif 3 <= df['Rating'].values[i2] < 4:
                            rate2 = '⭐️ ⭐️ ⭐️ ️'
                        elif 4 <= df['Rating'].values[i2] < 5:
                            rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                        elif 5 <= df['Rating'].values[i2] < 6:
                            rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                        st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                        st.write("Rating :", rate2)
                        st.write("Price :           $", df['Price'].values[i2])
                        st.write("Reviews :         ", df['Reviews'].values[i2])
                        st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                        '\n'
                        '\n'
                        '\n'
                    st.progress(100)

                    col1, col2 = st.columns([2.2, 5])
                    with col1:
                        st.image(df['image'].values[i3],
                                 caption=df['Book_title'].values[i3],
                                 width=170)

                    with col2:
                        if 1 <= df['Rating'].values[i3] < 2:
                            rate3 = '⭐️'
                        elif 2 <= df['Rating'].values[i3] < 3:
                            rate3 = '⭐️ ⭐️ ️'
                        elif 3 <= df['Rating'].values[i3] < 4:
                            rate3 = '⭐️ ⭐️ ⭐️ ️'
                        elif 4 <= df['Rating'].values[i3] < 5:
                            rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                        elif 5 <= df['Rating'].values[i3] < 6:
                            rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                        st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                        st.write("Rating :          ", rate3)
                        st.write("Price :           $", df['Price'].values[i3])
                        st.write("Reviews :         ", df['Reviews'].values[i3])
                        st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                        '\n'
                        '\n'
                        '\n'
                    st.progress(100)

                    col1, col2 = st.columns([2.2, 5])
                    with col1:
                        st.image(df['image'].values[i4],
                                 caption=df['Book_title'].values[i4],
                                 width=170)

                    with col2:
                        if 1 <= df['Rating'].values[i4] < 2:
                            rate4 = '⭐️'
                        elif 2 <= df['Rating'].values[i4] < 3:
                            rate4 = '⭐️ ⭐️ ️'
                        elif 3 <= df['Rating'].values[i4] < 4:
                            rate4 = '⭐️ ⭐️ ⭐️ ️'
                        elif 4 <= df['Rating'].values[i4] < 5:
                            rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                        elif 5 <= df['Rating'].values[i4] < 6:
                            rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                        st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                        st.write("Rating : ", rate4)
                        st.write("Price : $", df['Price'].values[i4])
                        st.write("Reviews : ", df['Reviews'].values[i4])
                        st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                        '\n'
                        '\n'
                        '\n'
                    st.progress(100)

                    col1, col2 = st.columns([2.2, 5])
                    with col1:
                        st.image(df['image'].values[i5],
                                 caption=df['Book_title'].values[i5],
                                 width=170)

                    with col2:
                        if 1 <= df['Rating'].values[i5] < 2:
                            rate5 = '⭐️'
                        elif 2 <= df['Rating'].values[i5] < 3:
                            rate5 = '⭐️ ⭐️ ️'
                        elif 3 <= df['Rating'].values[i5] < 4:
                            rate5 = '⭐️ ⭐️ ⭐️ ️'
                        elif 4 <= df['Rating'].values[i5] < 5:
                            rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                        elif 5 <= df['Rating'].values[i5] < 6:
                            rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                        st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                        st.write("Rating :             ", rate5)
                        st.write("Price :              $", df['Price'].values[i5])
                        st.write("Reviews :            ", df['Reviews'].values[i5])
                        st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                        '\n'
                        '\n'
                        '\n'
                    st.progress(100)
if pages == 'Collage of Engineering':
    with st.sidebar:
        dep = st.radio('Select Your Department ', ['Computer Engineering&Software',
                                                   'Architecture Engineering',
                                                   'Civil Engineering',
                                                   'Electrical Engineering',
                                                   'Mechanical Engineering ',
                                                   'Environmental Engineering',
                                                   'Road and Transportation Engineering',
                                                   'Materials Engineering',
                                                   'Water Resources Engineering'])

    if dep == 'Computer Engineering&Software':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Architecture Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Civilian Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Electrical Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Environmental Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :          $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Road and Transportation Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Materials Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

    elif dep == 'Water Resources Engineering':
        selected_book_name_dep = st.selectbox('', books['Book_title'].values)

        bsearch = st.button('Search')
        tk1 = 0
        if bsearch:
            tk1 = 1
            get_recommendations_posters(selected_book_name_dep, 'Book_title', title_vectors, 'Book_title')

        if tk1 == 1:
            col1, col2 = st.columns([2.1, 5])

            i0 = df[df['Book_title'] == selected_book_name_dep].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name_dep,
                         width=198)

            with col2:
                if 1 <= df['Rating'].values[i0] < 2:
                    rate = '⭐️'
                elif 2 <= df['Rating'].values[i0] < 3:
                    rate = '⭐️ ⭐️ ️'
                elif 3 <= df['Rating'].values[i0] < 4:
                    rate = '⭐️ ⭐️ ⭐️ ️'
                elif 4 <= df['Rating'].values[i0] < 5:
                    rate = '⭐️ ⭐️ ⭐️ ⭐️'
                elif 5 <= df['Rating'].values[i0] < 6:
                    rate = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i0])
                st.write("Rating :       ", rate)
                st.write("Price :        $", df['Price'].values[i0])
                st.write("Reviews :      ", df['Reviews'].values[i0])
                st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i0])

            '\n'
            '\n'
            st.title('You May Also Like.....')
            '\n'
            '\n'
            st.success('Recommending books similar to ' + selected_book_name_dep)
            if tk1 == 1:
                with st.expander('Click To Show Recommendations'):
                    '\n'
                    '\n'
                    '\n'
                    st.progress(100)

                    if tk1 == 1:
                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i1],
                                     caption=df['Book_title'].values[i1],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i1] < 2:
                                rate1 = '⭐️'
                            elif 2 <= df['Rating'].values[i1] < 3:
                                rate1 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i1] < 4:
                                rate1 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i1] < 5:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i1] < 6:
                                rate1 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i1])
                            st.write("Rating :             ", rate1)
                            st.write("Price :              $", df['Price'].values[i1])
                            st.write("Reviews :            ", df['Reviews'].values[i1])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i1])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i2],
                                     caption=df['Book_title'].values[i2],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i2] < 2:
                                rate2 = '⭐️'
                            elif 2 <= df['Rating'].values[i2] < 3:
                                rate2 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i2] < 4:
                                rate2 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i2] < 5:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i2] < 6:
                                rate2 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i2])
                            st.write("Rating :          ", rate2)
                            st.write("Price :           $", df['Price'].values[i2])
                            st.write("Reviews :         ", df['Reviews'].values[i2])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i2])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i3],
                                     caption=df['Book_title'].values[i3],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i3] < 2:
                                rate3 = '⭐️'
                            elif 2 <= df['Rating'].values[i3] < 3:
                                rate3 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i3] < 4:
                                rate3 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i3] < 5:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i3] < 6:
                                rate3 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i3])
                            st.write("Rating :          ", rate3)
                            st.write("Price :           $", df['Price'].values[i3])
                            st.write("Reviews :         ", df['Reviews'].values[i3])
                            st.write("No. Of Pages :    ", df['Number_Of_Pages'].values[i3])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i4],
                                     caption=df['Book_title'].values[i4],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i4] < 2:
                                rate4 = '⭐️'
                            elif 2 <= df['Rating'].values[i4] < 3:
                                rate4 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i4] < 4:
                                rate4 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i4] < 5:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i4] < 6:
                                rate4 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'

                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i4])
                            st.write("Rating : ", rate4)
                            st.write("Price : $", df['Price'].values[i4])
                            st.write("Reviews : ", df['Reviews'].values[i4])
                            st.write("No. Of Pages : ", df['Number_Of_Pages'].values[i4])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)

                        col1, col2 = st.columns([2.1, 5])
                        with col1:
                            st.image(df['image'].values[i5],
                                     caption=df['Book_title'].values[i5],
                                     width=198)

                        with col2:
                            if 1 <= df['Rating'].values[i5] < 2:
                                rate5 = '⭐️'
                            elif 2 <= df['Rating'].values[i5] < 3:
                                rate5 = '⭐️ ⭐️ ️'
                            elif 3 <= df['Rating'].values[i5] < 4:
                                rate5 = '⭐️ ⭐️ ⭐️ ️'
                            elif 4 <= df['Rating'].values[i5] < 5:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐️'
                            elif 5 <= df['Rating'].values[i5] < 6:
                                rate5 = '⭐️ ⭐️ ⭐️ ⭐ ⭐️'
                            st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒 👇 👇", df['Description'].values[i5])
                            st.write("Rating :             ", rate5)
                            st.write("Price :              $", df['Price'].values[i5])
                            st.write("Reviews :            ", df['Reviews'].values[i5])
                            st.write("No. Of Pages :       ", df['Number_Of_Pages'].values[i5])
                            '\n'
                            '\n'
                            '\n'
                        st.progress(100)
with st.sidebar.expander("POWERED BY"):
    st.write(""" 
                |𝐄𝐍𝐆. 𝐌𝐎𝐇𝐀𝐌𝐌𝐄𝐃 𝐊𝐇𝐀𝐋𝐈𝐃| \n
                
                 """)
    co1, co2 = st.columns([3, 3])
    with co1:
        st.image('https://cdn3.iconfinder.com/data/icons/social-icons-33/512/Telegram-128.png',
                 caption='Eng_m1997',
                 width=73)
    with co2:
        st.image(
            'https://cdn3.iconfinder.com/data/icons/2018-social-media-logotypes/1000'
            '/2018_social_media_popular_app_logo_instagram-512.png',
            caption='Eng_mk97',
            width=73)
