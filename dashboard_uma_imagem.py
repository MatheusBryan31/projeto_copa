import streamlit as st
from google.cloud import storage
from PIL import Image
from io import BytesIO

st.title("Olá, Mundo!\nSejam bem vindos ao meu site. Minha graça é Matheus Bryan!")

# Cliente autenticado via Streamlit Secrets
client = storage.Client.from_service_account_info(
    st.secrets["gcp_service_account"]
)

bucket_nome = "bryan_copa"
arquivo = "imagens_jogadores/ale_1.jpg"

bucket = client.bucket(bucket_nome)
blob = bucket.blob(arquivo)

imagem_bytes = blob.download_as_bytes()
imagem = Image.open(BytesIO(imagem_bytes))

st.image(
    imagem,
    caption="Imagem do Datalake - Google Cloud Storage"
)