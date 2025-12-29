
import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="BERT Text Classification",
    page_icon="📊",
    layout="centered"
)

# ---------------------------------------------------
# Introduction Section
# ---------------------------------------------------
st.title("BERT-Based Text Classification System")

st.markdown(
    """
    This project demonstrates a **production-ready text classification system**
    built using a **fine-tuned BERT-base model**, optimized for **web-based inference**
    using **ONNX Runtime**.

    The objective of this application is to deliver **high-accuracy natural language
    understanding** while maintaining **low-latency performance**, making it suitable
    for real-world deployment scenarios.
    """
)

# ---------------------------------------------------
# Key Highlights
# ---------------------------------------------------
st.subheader("Key Highlights")

st.markdown(
    """
    - **Model Architecture:** BERT-base (Transformer-based encoder)
    - **Training Strategy:** Fine-tuned on a domain-specific labeled dataset
    - **Validation Accuracy:** **93.44%**
    - **Optimization:** Converted to ONNX for faster, CPU-efficient inference
    - **Deployment Target:** Web-based applications using Streamlit
    """
)

# ---------------------------------------------------
# Why ONNX?
# ---------------------------------------------------
st.subheader("Why ONNX Optimization?")

st.markdown(
    """
    While PyTorch models are well-suited for training, ONNX enables
    **framework-agnostic, high-performance inference**.

    Benefits include:
    - Reduced inference latency
    - Lower memory footprint
    - Improved CPU performance
    - Easier deployment in production environments
    """
)

# ---------------------------------------------------
# Use Cases
# ---------------------------------------------------
st.subheader("Potential Use Cases")

st.markdown(
    """
    - Sentiment Analysis (reviews, feedback, social media)
    - Customer Support Ticket Classification
    - Content Moderation
    - Survey and Feedback Categorization
    - Enterprise NLP Pipelines
    """
)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption(
    "Fine-tuned BERT • ONNX Runtime Optimization • Streamlit Web Application"
)
