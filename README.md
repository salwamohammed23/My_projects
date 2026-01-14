# My_projects
# 🤖 Context-Aware Smart Agent

An intelligent agent system that understands and processes user queries with optional contextual information. Built with LangChain,
Groq API, and Gradio, this system can extract answers from provided context or perform web searches when needed.
- **Live Demo**: Try the application on [Hugging Face Spaces](https://huggingface.co/spaces/SalwaM/Context-Aware_Smart_Agent)
 **✨ Features**

- **Contextual Understanding**: Process questions with additional context using the `||` separator
- **Intelligent Answer Extraction**: Attempt to extract answers directly from provided context
- **Web Search Integration**: Fall back to real-time web searches using Tavily API when context is insufficient
- **Multi-language Support**: Handles both Arabic and English queries seamlessly
- **User-Friendly Interface**: Clean Gradio web interface with interactive examples
- **Error Handling**: Robust error handling for API failures and malformed inputs
  

# 📚 PDF Research Assistant

A research assistant application that allows users to upload PDF files and ask questions about their content.
The system extracts text from the PDF, splits it into chunks, generates embeddings, stores them in a Chroma database,
and uses Groq's language model to answer questions based on the document.
- **Live Demo**: Try the application on [Hugging Face Spaces](https://huggingface.co/spaces/SalwaM/PDF_Research_Assistant)
 **✨ Features**
- Upload PDF files (supports scanned PDFs if OCR is applied externally).
- Ask questions related to the PDF content.
- Provides concise, context-based answers.
- Returns bullet points and references when appropriate.
- Supports **English** and **Arabic** interfaces.
- Uses semantic search for relevant document retrieval with `ChromaDB`.
- Powered by `SentenceTransformer` embeddings and `Groq` LLM for question answering.


# Machine Learning Data Preprocessing and Training Application

This application provides a user-friendly command-line interface for loading, preprocessing, exploring, and training machine learning models on structured datasets. Users can input a dataset, handle missing values, perform exploratory data analysis (EDA), and train models interactively.

# Code Generation using RAG

**LangGraph-Powered Python Code Assistant** is an intelligent, interactive assistant designed to analyze, explain, and improve Python code using AI models.
The project leverages **LangGraph** for stateful conversational logic, **Gradio** for a user-friendly web interface, and **ChromaDB** for semantic code search, with support from **Groq** models to generate smart responses.
- **Live Demo**: Try the application on [Hugging Face Spaces](https://huggingface.co/spaces/SalwaM/Powered_Python_Code_Assistant)

This assistant helps developers to:

* Analyze and debug code.
* Provide context-aware explanations.
* Execute and test code directly.
* Interact via an AI-driven interface.

# Face Detection Project

This project demonstrates face detection in videos using the MTCNN (Multi-task Cascaded Convolutional Networks) model from the `facenet-pytorch` library. The workflow includes downloading a YouTube video, processing it to detect faces, and visualizing the results.

# Data Cleaning, Visualization

This project provides a streamlined process for **Data Cleaning**, **Visualization**, and **Statistical Analysis** of a dataset, with a focus on improving data quality and extracting valuable insights through geographic and exploratory visualizations, as well as statistical summaries.

# Diabetes Prediction Using Deep Learning

This project aims to predict the presence of diabetes in patients using a deep learning model. The dataset used contains several medical attributes related to diabetes diagnosis, and the model is built using PyTorch.

# Smart_Code_Evaluator
this tool would be quite useful for peer-reviewing code or as part of a learning platform where users receive instant feedback on their coding assignments.
# Illumination Control for Images

This project allows you to upload an image and apply gamma correction to it using an interactive **Streamlit** user interface. You can adjust the gamma value and see its effect on the image in real-time, and also download the modified image.

**Access the App**

You can also access the live app hosted on Streamlit using the following link:

[Streamlit App](https://myprojects-misvahlt3gdndgsdwt9tsk.streamlit.app/)

# ImageResizer Pro
is a Streamlit-based tool for resizing images with ease. It provides a simple interface where users can upload an image, specify new dimensions, and view the resized output instantly. This tool is ideal for quick image resizing tasks for web use, digital design, or personal use.

# Blog_and_Image_Generator project
 The app uses `streamlit` to create a simple interface for generating a blog post, divided into an introduction, body, and conclusion. It also generates relevant images to go along with the text.

# Dashourd
The purpose of this code is to create a Streamlit web dashboard for visualizing various types of data related to user registrations, subscriptions, course completions, capstone evaluations, coupons, and user statistics. The app provides interactive visualizations and tables to explore data across different time intervals (daily, weekly, monthly, yearly) and user-related metrics.


# Pulsar Star Classification using SVM

This project applies Support Vector Machine (SVM) classifiers to classify pulsar stars based on their physical characteristics. The dataset used for this classification is the `pulsar_data.csv`, containing 17898 instances and 9 features, including the target variable `target_class`.

# Flower Classification using Transfer Learning with MobileNetV2
This project demonstrates the use of transfer learning to classify flower images into five categories: daisy, dandelion, roses, sunflowers, and tulips. The model is built using TensorFlow and employs a pre-trained MobileNetV2 model to extract features, which are then fine-tuned for the classification task. The dataset is sourced from TensorFlow Flower Photos.



# Abalone Age Prediction with Ridge Regression

This project focuses on predicting the age of abalone based on its physical attributes using a machine learning pipeline with **Ridge Regression**. The dataset includes various physical measurements of abalones, such as length, diameter, and weight, along with their corresponding age. The goal is to predict the abalone's age based on these features.

# House Price Predictionusing
- [Decision Trees and Random Forests]
This project demonstrates the use of Decision Trees and Random Forests to predict house sale prices using the Ames housing dataset. The goal is to train a model that accurately predicts house prices based on various features such as lot area, year built, number of rooms, and more.
- [Linear Regression, Logistic Regression, and Support Vector Regression (SVR)]
This project aims to predict house prices based on various features using machine learning techniques. It implements three regression models: Linear Regression, Logistic Regression, and Support Vector Regression (SVR). The dataset used is House_Price.csv, which contains features such as crime rate, residential area, air quality, number of rooms, age, and various distances to amenities.

# House Rent Prediction 

This project focuses on predicting house rents using two machine learning models: **Linear Regression** and **Support Vector Regression (SVR)**. The dataset used is a CSV file containing various features related to house rentals.

# Drug Classification Using Decision Trees
This project aims to classify drugs based on patient data using a Decision Tree Classifier. The dataset includes various features such as age, sex, blood pressure, cholesterol levels, and sodium to potassium ratio. The goal is to predict which drug a patient should be prescribed based on these features.

# Diabetes Prediction Model

This project involves building a deep learning model to predict diabetes using a dataset containing various health metrics. The model is designed to help in early diagnosis and treatment planning for diabetes.


# Earthquake Data Analysis

This project involves analyzing earthquake data to predict earthquake magnitudes using Support Vector Regression (SVR). The dataset contains historical earthquake records with features such as latitude, longitude, depth, and datetime.

# KMeans Clustering Project

This project demonstrates how to apply the KMeans clustering algorithm using the scikit-learn library on a synthetic dataset. The goal is to group similar data points into clusters based on their feature values.


# Customer Conversion Prediction Model
This project builds a neural network model to predict customer conversion based on a dataset from a bank marketing campaign. The dataset contains various features such as customer demographics, past interactions with the bank, and economic indicators. The target variable is whether or not the customer subscribed to a term deposit (y), which is binary-encoded for training purposes.
