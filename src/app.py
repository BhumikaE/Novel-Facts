import streamlit as st
import requests
from xml.etree import cElementTree as ET
from PIL import Image as im

# from web_scraping import Web


image='novelfacts_home2.PNG'


# @st.cache
# def load_image(img):
#     im = Image.open(img)
#     return im

st.image(image, width=700)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# image_file=st.file_uploader("Upload Image")

#
# icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")


def text_analyser(my_text):
    url = 'https://200e73014679.ngrok.io/bot'
    myobj = {'Body': my_text}
    x = requests.post(url, data=myobj)
    txml = x.text
    root = ET.fromstring(txml)
    for body in root.findall('Message'):
        t_body = body.find('Body').text
        return t_body


def main():
    # st.header("This is Novel facts Coronavirus search engine")
    # remote_css('https //fonts.googleapis.com/css?family=Comfortaa')
   # st.markdown(html_template, unsafe_allow_html=True)
    message = st.text_input("Search coronavirus news here")
    if st.button("Search"):
        st.text("")
        st.text("")

        nlp_result = text_analyser(message)
        # nlp_result = text_analyser('Sunlight kills coronavirus')
        st.success(nlp_result)


if __name__ == '__main__':
    main()
