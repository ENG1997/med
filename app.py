# import authenticator as authenticator
import streamlit as st
import streamlit.components.v1 as components
import nltk
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import streamlit_authenticator as stauth

st.set_page_config(page_title="RAM Library", page_icon="📚", initial_sidebar_state="collapsed",
                   menu_items={
                       'Get help': 'https://www.instagram.com/eng_mk97/',
                       'Report a bug': "https://www.instagram.com/eng_mk97/",
                       'About': "Project supervisor: ⠀⠀ ⠀⠀ ⠀⠀⠀ "
                                "⠀⠀ ⠀⠀ ⠀⠀ https://uomustansiriyah.edu.iq/e-learn/profile.php?id=2623 "
                                "Implementation and design:⠀⠀"
                                "⠀⠀⠀ ⠀https://www.instagram.com/eng_mk97 ⠀https://www.instagram.com/ali_anmar_17/"
                   }
                   )
names = ['ENG-Mohammed Khalid', 'ENG-Ali Annmar', 'Supervisor ENG-Rana']
usernames = ['mohammed97', 'ali2000', 'rana1981']
passwords = ['123456', '123456', '123456']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'some_cookie_name', 'some_signature_key',
                                    cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
    style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">WELCOME DEAR STUDENT</span> </h2> """, width=750)

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


    df['clean_title'] = df['title'].apply(clean_text)
    df.head()

    vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
    X = vectorizer.fit_transform(df['clean_title'])
    title_vectors = X.toarray()


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
        i1 = df[df['title'] == simular[0][0]].index.values[0]
        i2 = df[df['title'] == simular[1][0]].index.values[0]
        i3 = df[df['title'] == simular[2][0]].index.values[0]
        i4 = df[df['title'] == simular[3][0]].index.values[0]
        i5 = df[df['title'] == simular[4][0]].index.values[0]

        return


    df = pd.read_csv('prog_book.csv')

    nltk.download('stopwords')


    df['clean_title'] = df['title'].apply(clean_text)
    df.head()

    vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
    X = vectorizer.fit_transform(df['clean_title'])
    title_vectors = X.toarray()

    tk = 0
    books_dict = pd.read_csv('prog_book.csv')
    books = pd.DataFrame(books_dict)

    pages = st.sidebar.selectbox('Chose your mode (Default : All Books) ', ['All Books',
                                                                            'Collage of Engineering',
                                                                            'College of Medicine',
                                                                            'College of Dentistry',
                                                                            'College of Pharmacy'], key=1)
    if pages == 'All Books':
        col1, col2 = st.columns([10, 1])

        with col1:
            selected_book_name = st.selectbox('Enter book name that you liked : ', books['title'].values, key=2)

            b1 = st.button('Search', key=1)
            '\n'

            if b1:
                tk = 1
        if tk == 1:
            import time

            with st.spinner('Wait, Please...🧐'):
                time.sleep(3)
            with st.spinner('Generating Download Links...'):
                time.sleep(1)
            my_bar = st.progress(0)
            x = 0
            for x in range(100):
                time.sleep(0.01)
            my_bar.progress(x + 1)

        if tk == 1:
            col1, col2 = st.columns([2.2, 5])

            i0 = df[df['title'] == selected_book_name].index.values[0]

            with col1:

                st.image(df['image'].values[i0],
                         caption=selected_book_name,
                         width=198)

            with col2:
                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                st.write("author :       ", df['author'].values[i0])
                st.write("publisher :        ", df['publisher'].values[i0])
                st.write("No. Of Pages : ", df['pages'].values[i0])
                st.write("language :      ", df['language'].values[i0])
                st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])

            '\n'
            '\n'
            st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
            style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> <a 
            href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
            #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> Powered 
            by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; margin-bottom: 
            20px;">&nbsp;</div> """, width=750)

            get_recommendations_posters(selected_book_name, 'title', title_vectors, 'title')

            if tk == 1:
                col1, col2 = st.columns([2.2, 5])
                with col1:
                    st.image(df['image'].values[i1],
                             caption=df['title'].values[i1],
                             width=170)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                    st.write("author :       ", df['author'].values[i1])
                    st.write("publisher :        ", df['publisher'].values[i1])
                    st.write("No. Of Pages : ", df['pages'].values[i1])
                    st.write("language :      ", df['language'].values[i1])
                    st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                    '\n'
                    '\n'
                    '\n'
                st.progress(100)

                col1, col2 = st.columns([2.2, 5])
                with col1:
                    st.image(df['image'].values[i2],
                             caption=df['title'].values[i2],
                             width=170)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                    st.write("author :       ", df['author'].values[i2])
                    st.write("publisher :        ", df['publisher'].values[i2])
                    st.write("No. Of Pages : ", df['pages'].values[i2])
                    st.write("language :      ", df['language'].values[i2])
                    st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])

                    '\n'
                    '\n'
                    '\n'
                st.progress(100)

                col1, col2 = st.columns([2.2, 5])
                with col1:
                    st.image(df['image'].values[i3],
                             caption=df['title'].values[i3],
                             width=170)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                    st.write("author :       ", df['author'].values[i3])
                    st.write("publisher :        ", df['publisher'].values[i3])
                    st.write("No. Of Pages : ", df['pages'].values[i3])
                    st.write("language :      ", df['language'].values[i3])
                    st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                    '\n'
                    '\n'
                    '\n'
                st.progress(100)

                col1, col2 = st.columns([2.2, 5])
                with col1:
                    st.image(df['image'].values[i4],
                             caption=df['title'].values[i4],
                             width=170)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                    st.write("author :       ", df['author'].values[i4])
                    st.write("publisher :        ", df['publisher'].values[i4])
                    st.write("No. Of Pages : ", df['pages'].values[i4])
                    st.write("language :      ", df['language'].values[i4])
                    st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                    '\n'
                    '\n'
                    '\n'
                st.progress(100)

                col1, col2 = st.columns([2.2, 5])
                with col1:
                    st.image(df['image'].values[i5],
                             caption=df['title'].values[i5],
                             width=170)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                    st.write("author :       ", df['author'].values[i5])
                    st.write("publisher :        ", df['publisher'].values[i5])
                    st.write("No. Of Pages : ", df['pages'].values[i5])
                    st.write("language :      ", df['language'].values[i5])
                    st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                    '\n'
                    '\n'
                    '\n'
                st.progress(100)
    deps = ['Computer Engineering&Software',
                                                       'Architecture Engineering',
                                                       'Civilian Engineering',
                                                       'Electrical Engineering',
                                                       'Mechanical Engineering',
                                                       'Environmental Engineering',
                                                       'Road and Transportation Engineering',
                                                       'Materials Engineering',
                                                       'Water Resources Engineering']
    if pages == 'Collage of Engineering':
        with st.sidebar:
            dep = st.radio('Select Your Department ', deps)

        if dep == 'Computer Engineering&Software':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=3)

            bsearch = st.button('Search', key=2)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])
                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Architecture Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=4)

            bsearch = st.button('Search', key=3)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])

                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Civilian Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=5)
            search = st.button('Search', key=4)
            tk1 = 0
            if search:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])

                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Electrical Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=6)

            bsearch = st.button('Search', key=5)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])

                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Environmental Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=8)

            bsearch = st.button('Search', key=7)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])

                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                            style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                            <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                            #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                            Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                            margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Mechanical Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=9)

            bsearch = st.button('Search', key=8)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])
                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Road and Transportation Engineering':

            selected_book_name_dep = st.selectbox('', books['title'].values, key=11)

            bsearch = st.button('Search', key=10)

            tk1 = 0

            if bsearch:
                tk1 = 1

                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:

                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],

                             caption=selected_book_name_dep,

                             width=198)

                with col2:

                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)

                    st.write("author :       ", df['author'].values[i0])

                    st.write("publisher :        ", df['publisher'].values[i0])

                    st.write("No. Of Pages : ", df['pages'].values[i0])

                    st.write("language :      ", df['language'].values[i0])

                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])

                    '\n'

                    '\n'

                    '\n'

                '\n'

                '\n'

                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 

                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 

                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 

                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 

                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 

                margin-bottom: 20px;">&nbsp;</div> """, width=750)

                '\n'

                '\n'

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

                                         caption=df['title'].values[i1],

                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)

                                st.write("author :       ", df['author'].values[i1])

                                st.write("publisher :        ", df['publisher'].values[i1])

                                st.write("No. Of Pages : ", df['pages'].values[i1])

                                st.write("language :      ", df['language'].values[i1])

                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])

                                '\n'

                                '\n'

                                '\n'

                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])

                            with col1:
                                st.image(df['image'].values[i2],

                                         caption=df['title'].values[i2],

                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)

                                st.write("author :       ", df['author'].values[i2])

                                st.write("publisher :        ", df['publisher'].values[i2])

                                st.write("No. Of Pages : ", df['pages'].values[i2])

                                st.write("language :      ", df['language'].values[i2])

                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])

                                '\n'

                                '\n'

                                '\n'

                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])

                            with col1:
                                st.image(df['image'].values[i3],

                                         caption=df['title'].values[i3],

                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)

                                st.write("author :       ", df['author'].values[i3])

                                st.write("publisher :        ", df['publisher'].values[i3])

                                st.write("No. Of Pages : ", df['pages'].values[i3])

                                st.write("language :      ", df['language'].values[i3])

                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])

                                '\n'

                                '\n'

                                '\n'

                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])

                            with col1:
                                st.image(df['image'].values[i4],

                                         caption=df['title'].values[i4],

                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)

                                st.write("author :       ", df['author'].values[i4])

                                st.write("publisher :        ", df['publisher'].values[i4])

                                st.write("No. Of Pages : ", df['pages'].values[i4])

                                st.write("language :      ", df['language'].values[i4])

                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])

                                '\n'

                                '\n'

                                '\n'

                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])

                            with col1:
                                st.image(df['image'].values[i5],

                                         caption=df['title'].values[i5],

                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)

                                st.write("author :       ", df['author'].values[i5])

                                st.write("publisher :        ", df['publisher'].values[i5])

                                st.write("No. Of Pages : ", df['pages'].values[i5])

                                st.write("language :      ", df['language'].values[i5])

                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'

                                '\n'

                                '\n'

                            st.progress(100)

        if dep == 'Water Resources Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=12)

            bsearch = st.button('Search', key=11)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])
                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

        if dep == 'Materials Engineering':
            selected_book_name_dep = st.selectbox('', books['title'].values, key=3)

            bsearch = st.button('Search', key=2)
            tk1 = 0
            if bsearch:
                tk1 = 1
                get_recommendations_posters(selected_book_name_dep, 'title', title_vectors, 'title')

            if tk1 == 1:
                col1, col2 = st.columns([2.1, 5])

                i0 = df[df['title'] == selected_book_name_dep].index.values[0]

                with col1:

                    st.image(df['image'].values[i0],
                             caption=selected_book_name_dep,
                             width=198)

                with col2:
                    st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i0], key=1)
                    st.write("author :       ", df['author'].values[i0])
                    st.write("publisher :        ", df['publisher'].values[i0])
                    st.write("No. Of Pages : ", df['pages'].values[i0])
                    st.write("language :      ", df['language'].values[i0])
                    st.write("Download :      ", df['download_link'].values[i0], df['file'].values[i0])
                    '\n'
                    '\n'
                    '\n'

                '\n'
                '\n'
                st.components.v1.html("""<h2 class="color1" style="margin-top:50px;overflow: hidden;"> <span 
                style="float:left;font-size: 25px; color: #49afd0;line-height: 16pt;">You may be interested in</span> 
                <a href="https://www.instagram.com/eng_mk97/" style="float:right;font-size: 12px; color: 
                #49afd0;line-height: 16pt;" target="_blank" title="recommender system and recommendation engine"> 
                Powered by ENG-Mohammed </a> </h2> <div style="background: #49AFD0; height:2px; width: 100%; 
                margin-bottom: 20px;">&nbsp;</div> """, width=750)
                '\n'
                '\n'
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
                                         caption=df['title'].values[i1],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i1], key=2)
                                st.write("author :       ", df['author'].values[i1])
                                st.write("publisher :        ", df['publisher'].values[i1])
                                st.write("No. Of Pages : ", df['pages'].values[i1])
                                st.write("language :      ", df['language'].values[i1])
                                st.write("Download :      ", df['download_link'].values[i1], df['file'].values[i1])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i2],
                                         caption=df['title'].values[i2],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i2], key=3)
                                st.write("author :       ", df['author'].values[i2])
                                st.write("publisher :        ", df['publisher'].values[i2])
                                st.write("No. Of Pages : ", df['pages'].values[i2])
                                st.write("language :      ", df['language'].values[i2])
                                st.write("Download :      ", df['download_link'].values[i2], df['file'].values[i2])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i3],
                                         caption=df['title'].values[i3],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i3], key=4)
                                st.write("author :       ", df['author'].values[i3])
                                st.write("publisher :        ", df['publisher'].values[i3])
                                st.write("No. Of Pages : ", df['pages'].values[i3])
                                st.write("language :      ", df['language'].values[i3])
                                st.write("Download :      ", df['download_link'].values[i3], df['file'].values[i3])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i4],
                                         caption=df['title'].values[i4],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i4], key=5)
                                st.write("author :       ", df['author'].values[i4])
                                st.write("publisher :        ", df['publisher'].values[i4])
                                st.write("No. Of Pages : ", df['pages'].values[i4])
                                st.write("language :      ", df['language'].values[i4])
                                st.write("Download :      ", df['download_link'].values[i4], df['file'].values[i4])
                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

                            col1, col2 = st.columns([2.1, 5])
                            with col1:
                                st.image(df['image'].values[i5],
                                         caption=df['title'].values[i5],
                                         width=198)

                            with col2:
                                st.text_area("𝐃𝐄𝐓𝐀𝐈𝐋𝐒", df['desc'].values[i5], key=6)
                                st.write("author :       ", df['author'].values[i5])
                                st.write("publisher :        ", df['publisher'].values[i5])
                                st.write("No. Of Pages : ", df['pages'].values[i5])
                                st.write("language :      ", df['language'].values[i5])
                                st.write("Download :      ", df['download_link'].values[i5], df['file'].values[i5])

                                '\n'
                                '\n'
                                '\n'
                            st.progress(100)

    if pages == 'College of Medicine':
        st.components.v1.html(
            """<h2 class="color1" style="margin-top:50px;overflow: hidden;"><span style="float:left;font-size: 25px; 
            color: #49afd0;line-height: 25pt;"> Comming Soon 🔥 ⚙️ 🕗</span></h2><a 
            href="https://www.instagram.com/eng_mk97/" style="float:left;font-size: 12px; color: #49afd0;line-height: 
            16pt;" target="_blank" title="recommender system and recommendation engine">Powered by ENG-Mohammed</a>""",
            width=750)
    if pages == 'College of Dentistry':
        st.components.v1.html(
            """<h2 class="color1" style="margin-top:50px;overflow: hidden;"><span style="float:left;font-size: 25px; 
            color: #49afd0;line-height: 25pt;"> Comming Soon 🔥 ⚙️ 🕗</span></h2><a 
            href="https://www.instagram.com/eng_mk97/" style="float:left;font-size: 12px; color: #49afd0;line-height: 
            16pt;" target="_blank" title="recommender system and recommendation engine">Powered by ENG-Mohammed</a>""",
            width=750)
    if pages == 'College of Pharmacy':
        st.components.v1.html(
            """<h2 class="color1" style="margin-top:50px;overflow: hidden;"><span style="float:left;font-size: 25px; 
            color: #49afd0;line-height: 25pt;"> Comming Soon 🔥 ⚙️ 🕗</span></h2><a 
            href="https://www.instagram.com/eng_mk97/" style="float:left;font-size: 12px; color: #49afd0;line-height: 
            16pt;" target="_blank" title="recommender system and recommendation engine">Powered by ENG-Mohammed</a>""",
            width=750)

    with st.sidebar.expander("Contact Us"):
        st.components.v1.html("""<a href="https://www.instagram.com/eng_mk97/" style="float:left;font-size: 20px; 
        color: #BB0A4E;line-height: 20pt;" target="_blank" title="recommender system and recommendation engine"> 
        Instagram </a> <a href="https://t.me/ENG_M1997" style="float:left;font-size: 20px; color: 
        #49afd0;line-height: 20pt;" target="_blank" title="recommender system and recommendation engine"> Telegram 
        </a> <a href="https://www.facebook.com/M.Fitness97/" style="float:left;font-size: 20px; color: 
        #030D96;line-height: 20pt;" target="_blank" title="recommender system and recommendation engine"> FaceBook </a> 

                                         """, width=120)


elif not authentication_status:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
