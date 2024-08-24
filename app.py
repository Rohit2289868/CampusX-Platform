import streamlit as st

st.header("CampusX")

st.sidebar.title("Courses")
ml = st.sidebar.button("Machine Learning")
dl = st.sidebar.button("Deep Learning")
aws = st.sidebar.button("AWS")
ds = st.sidebar.button("Data Science")
da = st.sidebar.button("Data Analytics")

if ml:
    st.header("Machine Learning")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to Machine Learning
        - Supervised Learning
        - Unsupervised Learning
        - Reinforcement Learning
        - Feature Engineering
        - Model Evaluation and Selection
        - Deployment of Machine Learning Models
        """)
    st.subheader("Course Price")
    st.write("₹5000")

if dl:
    st.header("Deep Learning")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to Deep Learning
        - Neural Networks and Backpropagation
        - Convolutional Neural Networks (CNN)
        - Recurrent Neural Networks (RNN) and LSTMs
        - Generative Adversarial Networks (GANs)
        - Autoencoders and Dimensionality Reduction
        - Transfer Learning
        - Model Optimization and Fine-tuning
        - Deployment of Deep Learning Models
        """)
    st.subheader("Course Price")
    st.write("₹8000")
