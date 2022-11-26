import streamlit as st


import streamlit as st
import xlsxwriter
from PIL import Image
st.title("Contact")
image_file = st.file_uploader("UPLOAD THE PICTURE OF THE SUSPICIOUS SITUATION", type=["png","jpg","jpeg"])
if image_file is not None:
     workbook = xlsxwriter.Workbook('book1.xlsx')
     worksheet = workbook.add_worksheet()

     # Widen the first column to make the text clearer.
     worksheet.set_column('A:A', 30)

     # Insert an image.
     worksheet.write('A2', 'Insert an image in a cell:')
     worksheet.insert_image('B2', image_file.name)

     workbook.close()