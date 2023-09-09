from langchain.chains import SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from key import api_key
import os

os.environ['OPENAI_API_KEY']=api_key
llm=OpenAI(temperature=0.6)

def generate_genre(artist):

    prompt_Template_name=PromptTemplate(
        input_variables=['artist'],
        template=''' Suggest all the types of song genre by {artist}.Return it as a comma separated string.'''
    )
    genre_chain=LLMChain(llm=llm,prompt=prompt_Template_name,output_key='genre_list')

    genre_list=genre_chain.run(artist)
    return genre_list

def generate_playlist(artist,genre):

    prompt_Template_name=PromptTemplate(
        input_variables=['artist','genre'],
        template=''' Make a playlist of songs by {artist} of genre {genre}.Return it as a comma separated string.'''
    )
    playlist_chain=LLMChain(llm=llm,prompt=prompt_Template_name,output_key='Playlist')
    playlist=playlist_chain.run({'artist':artist,'genre':genre})
    return playlist

if __name__=='__main__':
    pass

