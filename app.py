
import streamlit as st
import pickle
import pandas as pd  
import requests

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_dic = pd.DataFrame(movies_dict)

similar = pickle.load(open('similar.pkl', 'rb'))

def recommend_movie(movies):
     movies_index = movies_dic[movies_dic['title'] == movies].index[0]
     major_index = similar[movies_index]
     movies_list = sorted(list(enumerate(major_index)), reverse= True, key = lambda x:x[1])[1:6]

     recommend_movie_list = []  
     recommend_movies_poster = []
     for i in movies_list:
          movie_id = movies_dic.iloc[i[0]].id
          recommend_movie_list.append(movies_dic.iloc[i[0]].title)
          #fetching poster  data
          recommend_movies_poster.append(fetch_poster(movie_id))

     return recommend_movie_list, recommend_movies_poster

def fetch_poster(movie_id):
     #To hit the api from web browser
     response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6d04b53adea90d3a66d46660919c8b83&language=en-US'.format(movie_id))
     data = response.json()
     return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']  


st.title('Movie recommendation')   
selected_movie_name = st.selectbox(
     'How would you like to be contacted?',
     movies_dic['title'].values)

if st.button('Recommend'):
     recommanditon_movie, poster  = recommend_movie(selected_movie_name)
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
        st.text(recommanditon_movie[0])
        st.image(poster[0])
     with col2:
        st.text(recommanditon_movie[1])
        st.image(poster[1])

     with col3:
        st.text(recommanditon_movie[2])
        st.image(poster[2])
     with col4:
        st.text(recommanditon_movie[3])
        st.image(poster[3])   
     with col5:
        st.text(recommanditon_movie[4])
        st.image(poster[4])
