import cv2
from PIL import Image
from image_to_text_description import Transformers_image
import streamlit as st
import threading




cap = cv2.VideoCapture(0)
i = 0
transf = Transformers_image()

def consulta_imagem(frame):
    global texto_imagem
    color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(color_converted)
    texto_imagem = transf.description_image(image = pil_image)
    print(texto_imagem)

z= 0
st.set_page_config(page_title="Image to text")
st.title("Image to text")
frame_text = st.empty()
frame_placeholder = st.empty()
plotarr = st.checkbox('Plotar')
pararr = st.checkbox('Parar')
texto_imagem = ''
while True:
    ret, frame = cap.read()

    frame_text.text(texto_imagem)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame,channels="RGB")

    if (plotarr and i ==50) or i == 250:
        i = 0
        processThread = threading.Thread(target=consulta_imagem, args=(frame,))
        processThread.start()

    if pararr:
        break

    i = i + 1

cap.release()
cv2.destroyAllWindows()
st.text("The end!")

