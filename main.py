from Chain import Chain
from io import BytesIO
import streamlit as st

st.title('Генерирование схем ОТН')
max_elements_number = st.slider('Максимальное количество элементов', 3, 50, 10)
max_elements_number_per_connection = st.slider('Максимальное количество элементов в одном соединении', 2, max_elements_number, 3)

screen_width = st.slider('Ширина картинки', 200, 4000, 500)
screen_height = st.slider('Высота картинки', 100, 4000, 200)

chain = Chain((screen_width, screen_height),30, 10, 5,10,(10, screen_height//2))
image = chain.create_chain(max_elements_number, max_elements_number_per_connection)

if st.button('Новая схема'):
    image = chain.create_chain(max_elements_number, max_elements_number_per_connection)



st.image(image)

buf = BytesIO()
image.save(buf, format='png')
byte_im = buf.getvalue()

btn = st.download_button(
      label="Скачать схему",
      data=byte_im,
      file_name="chain.png",
      mime="image/jpeg",
      )

st.caption('Design by Belousov')