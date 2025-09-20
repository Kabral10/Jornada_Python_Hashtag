# titulo
# imput do chat
# a cada mensagem enviada:
    # Mostrar na tela a mensagem enviada
    # Enviar essa mensagem para a IA responder
    # Aparece a resposta da IA na tela

# Ferramenta: streamlit - frontend / backend

import streamlit as st
from openai import OpenAI

modelo = OpenAI()   #(api_key='Sua chave openai')
st.write('### ChatBot com IA')

#session_state = memória do streamlit
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []


#Adicionar mensagem
#st.session_state['lista_mensagens'].append(mensagem)

#Exibir o Histórico de mensagens
for mensagen in st.session_state['lista_mensagens']:
    role = mensagen['role']
    texto = mensagen['content']
    st.chat_message(role).write(texto)


mensagem_usuario = st.chat_input('Escreva a mensagem para LuizIA')

if mensagem_usuario:
    #Assistant -> Ia
    #User -> Ser humano
    st.chat_message('user').write(mensagem_usuario)
    mensagem = {'role': 'user', 'content': mensagem_usuario}
    st.session_state['lista_mensagens'].append(mensagem)

    #Resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages = st.session_state['lista_mensagens'],
        model = "gpt-4o"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content

    #Exibir resposta da IA
    st.chat_message('assistant').write(resposta_ia)
    mensagem_ia = {'role': 'assistant', 'content': resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)