from Chain import Chain
from io import BytesIO
import streamlit as st
from random import randint

variant = randint(10000, 99999)
st.title('Генерирование схем ОТН')
max_elements_number = st.slider('Количество элементов', 3, 50, 10)
max_elements_number_per_connection = st.slider('Максимальное количество элементов в одном соединении', 2, max_elements_number, 3)
col1, col2 = st.columns(2)
with col1:
    exp_min = st.number_input('Минимальное значение параметра экспоненциального распределения', value=0)
    weibull_a_min = st.number_input('Минимальное значение параметра Вейбулла a', value=0)
    weibull_b_min = st.number_input('Минимальное значение параметра Вейбулла b', value=0)
    time_min = st.number_input('Минимальное значение времени', value=0)
with col2:
    exp_max = st.number_input('Максимальное значение параметра экспоненциального распределения', value=10)
    weibull_a_max = st.number_input('Максимальное значение параметра Вейбулла a', value=10)
    weibull_b_max = st.number_input('Максимальное значение параметра Вейбулла b', value=10)
    time_max = st.number_input('Максимальное значение времени', value=10)

chain = Chain(40, 20, 5, 10)
image = chain.create_chain(max_elements_number, max_elements_number_per_connection, variant,
                                    exp_min, exp_max,
                                    weibull_a_min, weibull_a_max,
                                    weibull_b_min, weibull_b_max,
                                    time_min, time_max)

if st.button('Новая схема'):
    image = chain.create_chain(max_elements_number, max_elements_number_per_connection, variant,
                                    exp_min, exp_max,
                                    weibull_a_min, weibull_a_max,
                                    weibull_b_min, weibull_b_max,
                                    time_min, time_max)



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