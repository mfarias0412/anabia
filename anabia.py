import streamlit as st
import time

# Título do aplicativo
st.title(':blue[Conversor de Temperaturas]')
# Exibição da imagem
st.image('https://imagens.climatempo.com.br/climapress/galeria/2023/08/060e88615fdd183f6f26d995a270a0d3.jpg', width=280)

# Seleção da escala termométrica de entrada
op1 = st.selectbox('*Qual escala termométrica você gostaria de converter?*', ('Celsius', 'Fahrenheit', 'Kelvin'))

# Captura da temperatura com validação de limites
if op1 == 'Celsius':
    # Temperatura em Celsius: valores válidos de -273.15 (zero absoluto) a 100 (fervura da água)
    temp = st.number_input('*Temperatura em Celsius*', value=0.0, placeholder='Insira um valor', min_value=-273.15,
                           max_value=100.0)
elif op1 == 'Fahrenheit':
    # Temperatura em Fahrenheit: valores válidos de -459.67 (zero absoluto) a 212 (fervura da água)
    temp = st.number_input('*Temperatura em Fahrenheit*', value=0.0, placeholder='Insira um valor', min_value=-459.67,
                           max_value=212.0)
elif op1 == 'Kelvin':
    # Temperatura em Kelvin: valores válidos de 0 (zero absoluto) a 373.15 (fervura da água)
    temp = st.number_input('*Temperatura em Kelvin*', value=0.0, placeholder='Insira um valor', min_value=0.0,
                           max_value=373.15)

# Seleção da escala termométrica de destino
op2 = st.selectbox('*Converter para:*', ('Celsius', 'Fahrenheit', 'Kelvin'))


# Funções de conversão entre as diferentes escalas termométricas
def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_para_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9


def kelvin_para_celsius(kelvin):
    return kelvin - 273.15


def kelvin_para_fahrenheit(kelvin):
    return (kelvin * 9 / 5) - 459.67


# Ação do botão de conversão
if st.button('Converter'):
    with st.spinner('Calculando...'):
        time.sleep(2)
    # Verificação da combinação de escalas e chamada da função de conversão correspondente
    if op1 == 'Celsius' and op2 == 'Fahrenheit':
        resposta = celsius_para_fahrenheit(temp)
    elif op1 == 'Celsius' and op2 == 'Kelvin':
        resposta = celsius_para_kelvin(temp)
    elif op1 == 'Fahrenheit' and op2 == 'Celsius':
        resposta = fahrenheit_para_celsius(temp)
    elif op1 == 'Fahrenheit' and op2 == 'Kelvin':
        resposta = fahrenheit_para_kelvin(temp)
    elif op1 == 'Kelvin' and op2 == 'Celsius':
        resposta = kelvin_para_celsius(temp)
    elif op1 == 'Kelvin' and op2 == 'Fahrenheit':
        resposta = kelvin_para_fahrenheit(temp)

    # Exibição do resultado
    st.write('Temperatura em {}: {:.2f}'.format(op2, resposta))
