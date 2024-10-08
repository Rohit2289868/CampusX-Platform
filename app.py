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

if aws:
    st.header("AWS (Amazon Web Services)")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to Cloud Computing and AWS
        - AWS Global Infrastructure Overview
        - Identity and Access Management (IAM)
        - Amazon EC2 and Elastic Load Balancing
        - Amazon S3 and Storage Solutions
        - AWS Networking (VPC, Route 53)
        - AWS Databases (RDS, DynamoDB)
        - AWS Lambda and Serverless Architecture
        - Monitoring and Management (CloudWatch, CloudTrail)
        - Security Best Practices and Compliance
        - Cost Management and Optimization
        - Deployment and Automation (CloudFormation, CI/CD)
        """)
    st.subheader("Course Price")
    st.write("₹4000")

if ds:
    st.header("Data Science")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to Data Science
        - Python for Data Science
        - Data Exploration and Visualization
        - Statistics for Data Science
        - Data Wrangling and Preprocessing
        - Machine Learning Fundamentals
        - Supervised and Unsupervised Learning
        - Natural Language Processing (NLP)
        - Time Series Analysis
        - Big Data and Cloud Platforms
        - Model Deployment and Monitoring
        - Capstone Project
        """)
    st.subheader("Course Price")
    st.write("₹9000")


