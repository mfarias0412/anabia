import streamlit as st
import time

# Título do aplicativo
st.title(':blue[Conversor de Temperaturas]')
# Exibição da imagem
st.image('https://imagens.climatempo.com.br/climapress/galeria/2023/08/060e88615fdd183f6f26d995a270a0d3.jpg', width=280)

# Seleção da escala termométrica de entrada
op1 = st.selectbox('*Qual escala termométrica você gostaria de converter?*', ('Celsius', 'Fahrenheit', 'Kelvin'))

# Variável para armazenar a mensagem de erro
mensagem_erro = ""

# Captura da temperatura com validação de limites
if op1 == 'Celsius':
    temp = st.number_input('*Temperatura em Celsius*', value=0.0, placeholder='Insira um valor')
    if temp < -273.15:
        mensagem_erro = "O valor inserido não é possível pois o mesmo não existe na escala Kelvin."
elif op1 == 'Fahrenheit':
    temp = st.number_input('*Temperatura em Fahrenheit*', value=0.0, placeholder='Insira um valor')
    if temp < -459.67:
        mensagem_erro = "O valor inserido não é possível pois o mesmo não existe na escala Kelvin."
elif op1 == 'Kelvin':
    temp = st.number_input('*Temperatura em Kelvin*', value=0.0, placeholder='Insira um valor')
    if temp < 0.0:
        mensagem_erro = "O valor inserido não é possível pois o mesmo não existe na escala Kelvin."

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


# Exibição da mensagem de erro, se houver
if mensagem_erro:
    st.error(mensagem_erro)

# Ação do botão de conversão
if st.button('Converter') and not mensagem_erro:
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
