import streamlit as st
import main

st.title(" Playlist Generator ")
artist=st.text_input(" ## Enter the name of artist.")

if artist:   
    genre=main.generate_genre(artist)
    genre_list=genre.split()
    st.write("**Genre names**")
    choice=st.selectbox("select genre",genre_list)

    if choice:
        playlist=main.generate_playlist(artist,choice)
        playlist=playlist.split(',')
        for item in playlist:
            st.write("-", item)

