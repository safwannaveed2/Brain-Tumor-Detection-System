import streamlit as st
import numpy as np
import cv2
import tensorflow

st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="centered"
)


@st.cache_resource
def load_trained_model():
    return tensorflow.keras.models.load_model("brain_tumor_model (1).keras")

model = load_trained_model()


st.title("🧠 Brain Tumor Detection System")
st.write(
    "Upload a brain MRI image to check whether **Tumor** is present or **Not**."
)


uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)


def preprocess_image(image):
    img = cv2.resize(image, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


if uploaded_file is not None:
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()), dtype=np.uint8
    )
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, caption="Uploaded MRI", use_container_width=True)

    if st.button("Predict"):
        processed_img = preprocess_image(image)
        prediction = model.predict(processed_img)[0][0]

        if prediction > 0.5:
            st.error("🧠 Tumor Detected")
        else:
            st.success("✅ No Tumor Detected")
