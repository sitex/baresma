import streamlit as st
import pandas as pd

# st prompt with dropdown list

df = pd.DataFrame({
    'sign': ['♈ Овен','♉ Телец','♊ Близнецы','♋ Рак','♌ Лев','♍ Дева','♎ Весы','♏ Скорпион','♐ Стрелец','♑ Козерог','♒ Водолей','♓ Рыбы'],
    'planet': ['Марс','Венера','Меркурий','Луна','Солнце','Меркурий','Венера','Марс','Юпитер','Сатурн','Сатурн','Юпитер'],
    'number': [16,8,4,2,1,4,8,16,32,64,64,32],
    'sex':['m','f','m','f','m','f','m','f','m','f','m','f'],
    'f':['ПраПраБабушка','ПраБабушка','Бабушка','Мама','Я','Бабушка','ПраБабушка','ПраПраБабушка','ПраПраПраБабушка','ПраПраПраПраБабушка','ПраПраПраПраБабушка','ПраПраПраБабушка'],
    'm':['ПраПраДедушка','ПраДедушка','Дедушка','Папа','Я','Дедушка','ПраДедушка','ПраПраДедушка','ПраПраПраДедушка','ПраПраПраПраДедушка','ПраПраПраПраДедушка','ПраПраПраДедушка'],
})

st.header('Предки по Лилит и Селене')

def multiply_decimal_part(number):
    """Multiply the decimal part of a number by 1.6666"""
    number = float(number)  # Convert the number to a float
    decimal_part = number - int(number)  # Extract the decimal part
    decimal_part *= 1.6666  # Multiply the decimal part by 1.6666
    return int(number) + decimal_part  # Add the integer part and the modified decimal part

def show_result():
    sex = df.loc[df['sign'] == st.session_state['option'], 'sex'].iloc[0]
    number = df.loc[df['sign'] == st.session_state['option'], 'number'].iloc[0]
    prompt = multiply_decimal_part(st.session_state['prompt'])

    # devide 30 by number
    result = int(prompt / float(30 / number)) + 1
    # is even number?
    if result % 2 == 0:
        if sex == 'f':
            sex = 'm'
        else:
            sex = 'f'

    st.session_state.result = df.loc[df['sign'] == option, sex].iloc[0]

    if number not in [1, 2]:
        st.session_state.result += ' по '
        st.session_state.result += 'Маме' if sex == 'f' else 'Папе'

option = st.radio('1 - Знак зодиака', df['sign'], key='option')

prompt = st.text_input('2 - Градус (от 0 до 30). Через точку, например: 15.5', 
    '15.5',
    key='prompt', help='Введите градус')

if st.button('Рассчитать', key='button'):
    show_result()

if 'result' in st.session_state:
    st.write(st.session_state['result'])