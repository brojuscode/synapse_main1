import streamlit as st

st.set_page_config(
    page_title="Bengaluru City Police"
)

st.title("BANGALORE CITY POLICE DEPARTMENT")
st.write("Policing in general and specially in a metropolitan city like Bengaluru is an extremely complex job. Whereas, we are well aware of the fact that fullfillment of expectations is not possible without the active support of the citizens. Challenges are many; expectations are high but resources are limited.")
from PIL import Image
image = Image.open('police.jpg')

st.image(image)
