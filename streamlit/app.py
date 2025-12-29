import streamlit as st
import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer
import time

# ---------------------------------------------------
# App Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="BERT Text Classification",
    page_icon="📄",
    layout="centered"
)

st.title("Text Classification using Fine-Tuned BERT")

# ---------------------------------------------------
# Load Tokenizer
# ---------------------------------------------------
@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("./onnx_model")

tokenizer = load_tokenizer()

# ---------------------------------------------------
# Load ONNX Model
# ---------------------------------------------------
@st.cache_resource
def load_onnx_model():
    providers = ["CPUExecutionProvider"]
    session = ort.InferenceSession(
        "./onnx_model/model.onnx",
        providers=providers
    )
    return session

session = load_onnx_model()

# ---------------------------------------------------
# Helper Functions
# ---------------------------------------------------
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=-1, keepdims=True)

def predict(text):
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="np"
    )

   

    start_time = time.time()
    logits = session.run(None, dict(inputs))[0]
    inference_time = (time.time() - start_time) * 1000

    probabilities = softmax(logits)
    predicted_class = int(np.argmax(probabilities))
    confidence = float(np.max(probabilities))

    return predicted_class, confidence, inference_time

# ---------------------------------------------------
# UI Section
# ---------------------------------------------------
st.subheader("Enter Text for Classification")

user_text = st.text_area(
    "Input Text",
    height=180,
    placeholder="Paste or type text here..."
)

class_labels = {
    0: "Negative",
    1: "Positive"
}

if st.button("Classify Text"):
    if not user_text.strip():
        st.warning("Please enter some text before classification.")
    else:
        with st.spinner("Running inference using ONNX-optimized BERT..."):
            label, confidence, latency = predict(user_text)

        st.success("Inference Completed")

        st.markdown("### Prediction Result")
        st.write(f"**Predicted Class:** {class_labels[label]}")
        st.write(f"**Confidence:** {confidence:.2%}")
        st.write(f"**Inference Time:** {latency:.2f} ms")
