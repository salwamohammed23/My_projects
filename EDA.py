import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# تحميل البيانات
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

df = load_data("first_inten_project.csv")

# معالجة البيانات
@st.cache_data
def preprocess_data(df):

    
    imputer = SimpleImputer(strategy='mean')
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
    
    df.drop_duplicates(inplace=True)
    
    encoder = LabelEncoder()
    for col in df.select_dtypes(include='object'):
        df[col] = encoder.fit_transform(df[col].astype(str))
    
    return df

df = preprocess_data(df)

# تقسيم الصفحة إلى أزرار في Sidebar
st.sidebar.title("🔍 استكشاف البيانات")
if st.sidebar.button("🗂️ عرض البيانات الأساسية"):
    st.write(df.head())

if st.sidebar.button("📊 التحليل الإحصائي"):
    st.write(df.describe())

if st.sidebar.button("📈 الرسوم البيانية التفاعلية"):
    fig = px.scatter_3d(df, x='lead time', y='number of adults', z='average price ', color='booking status')
    st.plotly_chart(fig)

if st.sidebar.button("🔗 تحليل الارتباطات"):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    st.pyplot(fig)
