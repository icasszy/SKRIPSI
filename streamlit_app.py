import streamlit as st

st.set_page_config(
    page_title="Prediksi Tingkat Depresi Mahasiswa",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Prediksi Tingkat Depresi Mahasiswa")

st.markdown("""
Website ini merupakan implementasi penelitian:

**Perbandingan Performa Algoritma XGBoost dan CatBoost dalam Klasifikasi Tingkat Depresi Mahasiswa**

Model terbaik yang digunakan adalah **CatBoost** dengan proporsi data **80:20**.
""")
