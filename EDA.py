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

df = load_data("first inten project.csv")

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


# Sidebar for selection
st.sidebar.title("اختر نوع التحليل")
option = st.sidebar.selectbox(
    "اختر نوع المخطط", 
    ["عدد البالغين مقابل السعر المتوسط", "مدة الحجز مقابل السعر المتوسط", "الطلبات الخاصة مقابل السعر المتوسط", "مخطط ثلاثي الأبعاد"]
)

# Display selected visualization
st.title("📊 تحليل بيانات الحجوزات الفندقية")

if option == "عدد البالغين مقابل السعر المتوسط":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df['number of adults'], y=df['average price '], hue=df['booking status'], ax=ax)
    ax.set_title("عدد البالغين مقابل السعر المتوسط")
    ax.set_xlabel("عدد البالغين")
    ax.set_ylabel("السعر المتوسط")
    st.pyplot(fig)

elif option == "مدة الحجز مقابل السعر المتوسط":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df['lead time'], y=df['average price '], hue=df['booking status'], ax=ax)
    ax.set_title("مدة الحجز مقابل السعر المتوسط")
    ax.set_xlabel("مدة الحجز (أيام)")
    ax.set_ylabel("السعر المتوسط")
    st.pyplot(fig)

elif option == "الطلبات الخاصة مقابل السعر المتوسط":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df['special requests'], y=df['average price '], hue=df['booking status'], ax=ax)
    ax.set_title("الطلبات الخاصة مقابل السعر المتوسط")
    ax.set_xlabel("عدد الطلبات الخاصة")
    ax.set_ylabel("السعر المتوسط")
    st.pyplot(fig)

elif option == "مخطط ثلاثي الأبعاد":
    fig = px.scatter_3d(
        df, x='lead time', y='number of adults', z='average price ', 
        color='booking status', hover_data=['number of children', 'room type', 'market segment type'],
        title="📌 مخطط ثلاثي الأبعاد للحجوزات الفندقية"
    )
    st.plotly_chart(fig)



if st.sidebar.button("📈 الرسوم البيانية التفاعلية"):
    fig = px.scatter_3d(df, x='lead time', y='number of adults', z='average price ', color='booking status')
    st.plotly_chart(fig)

if st.sidebar.button("🔗 تحليل الارتباطات"):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    st.pyplot(fig)
