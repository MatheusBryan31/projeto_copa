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
    st.subheader("Seleção Brasileira")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(carregar_imagem("imagens_jogadores/bra_5.jpg"))
        st.write("Sandro Bahia")
    with col2:
        st.image(carregar_imagem("imagens_jogadores/bra_3.jpg"))
        st.write("Markin do Pneu")
    with col3:
        st.image(carregar_imagem("imagens_jogadores/bra_4.jpg"))
        st.write("Beiçola")
# ========================================================================================================
# ============================================ ALEMANHA ==================================================
with ab2:
    st.subheader("Seleção Alemã")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(carregar_imagem("imagens_jogadores/ale_1.jpg"))
        st.write("Manoel Noiado")
    with col2:
        st.image(carregar_imagem("imagens_jogadores/ale_2.jpg"))
        st.write("Cláudio Emílio")
    with col3:
        st.image(carregar_imagem("imagens_jogadores/ale_11.jpg"))
        st.write("Juninho Pernambucano")
# =========================================================================================================
# -------------------------------------------------------------------------------------------------

#st.image(
#   imagem,
#    caption="Imagem do Datalake - Google Cloud Storage"