import streamlit as st
from google.cloud import storage
from PIL import Image
from io import BytesIO

# Cliente autenticado via Streamlit Secrets
client = storage.Client.from_service_account_info(
    st.secrets["gcp_service_account"]
)

bucket_nome = "bryan_copa"
#arquivo = "imagens_jogadores/ale_1.jpg"

bucket = client.bucket(bucket_nome)
#blob = bucket.blob(arquivo)

#imagem_bytes = blob.download_as_bytes()
#imagem = Image.open(BytesIO(imagem_bytes))

# -------------------------------------------------------------------------------------------------
def carregar_imagem(nome_arquivo):
    blob = bucket.blob(nome_arquivo)
    imagem_bytes = blob.download_as_bytes()
    return Image.open(BytesIO(imagem_bytes))
# Título do site
st.title("Olá, Mundo!\nSejam bem vindos ao meu site. Minha graça é Matheus Bryan!")

# Adição das abas
ab1, ab2 = st.tabs([
    "Brasil",
    "Alemanha"
])
# ============================================ BRASIL ====================================================
with ab1:
    st.subheader("Seleção brasileira")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(carregar_imagem("imagens_jogadores/ale_1.jpg"))
        st.write("Doidão do Brasil")
    with col2:
        st.image(carregar_imagem("imagens_jogadores/bra_3.jpg"))
        st.write("Mais um do Brasil")
    with col3:
        st.image("imagens_jogadores/bra_4.jpg")
# ========================================================================================================
# ============================================ ALEMANHA ==================================================
with ab2:
    st.subheader("Seleção Alemã")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(carregar_imagem("imagens_jogadores/ale_1.jpg"))
        st.write("Manuel Noier")
    with col2:
        st.image(carregar_imagem("imagens_jogadores/ale_2.jpg"))
        st.write("Malução da alemanha")
    with col3:
        st.image(carregar_imagem("imagens_jogadores/ale_4.jpg"))
        st.write("Mais um da alemanha")
# =========================================================================================================
# -------------------------------------------------------------------------------------------------

#st.image(
#   imagem,
#    caption="Imagem do Datalake - Google Cloud Storage"