# --- PERSONALIZAÇÃO AVANÇADA + STATUS - DEIXE SEU APP UNICO

import streamlit as st
import time

# --- Configurações da Página --- #
st.set_page_config(
    page_title="Customização do App - Hélio Silvestre dos Santos",
    page_icon="🏭",
    layout='wide'
)

# --- Titulo da Página --- #
st.title('Customização e Componentes')

# --- Explicação do Site --- #
st.markdown("""
Esta aplicação demonstra a tematização e a ideia de componentes customizados.
As cores e fontes que você vê agora são definidas no arquivo `.streamlit/config.tom.ml`
            """)

# --- Exemplo de Status (Carregamento)
st.header('Mensagem de Status')
with st.status("Preparando dados....",expanded=True) as status:
    st.write("Buscando Dados da Fonte...")
    time.sleep(2)
    st.write('Processando Informações...')
    time.sleep(1)
    st.write('Gerando Relatório Final...')
    status.update(label='Dados Carregados',state = 'complete')

st.success('Processo Concluído')




