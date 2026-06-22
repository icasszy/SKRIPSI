import streamlit as st
import pandas as pd
import joblib

model = joblib.load("catboost_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(
    page_title="Prediksi Tingkat Depresi Mahasiswa",
    page_icon="🧠",
    layout="wide"
)
st.title("🧠 Prediksi Tingkat Depresi Mahasiswa")

st.write(
"""
Silakan isi seluruh pertanyaan berikut sesuai kondisi Anda.
Data hanya digunakan untuk proses prediksi menggunakan model Machine Learning CatBoost.
"""
)

st.header("A. Identitas Responden")

usia = st.number_input(
    "Usia",
    17,
    30,
    20
)

jk = st.selectbox(
    "Jenis Kelamin",
    ["Perempuan","Laki-laki"]
)

semester = st.number_input(
    "Semester",
    1,
    14,
    4
)

jk_mapping={
"Perempuan":0,
"Laki-laki":1
}

tempat_mapping = {
    "Keluarga": 0,
    "Sendiri": 1
}
tempat = st.selectbox(
    "Tempat Tinggal",
    ["Keluarga", "Sendiri"]

tempat_mapping={
"Keluarga":0,
"Sendiri":1
}

jk=jk_mapping[jk]
tempat=tempat_mapping[tempat]

st.header("B. Kuesioner Depression ")
list(opsi_dep.keys(
"Tidak Pernah":0,
"Beberapa Hari":1,
"Lebih dari separuh waktu yang dimaksud":2,
"Hampir setiap hari":3
)
    )
phq1=st.radio(
"Kurang berminat atau bergairah dalam melakukan apapun.",
list(opsi.keys())
)

phq2=st.radio(
"Merasa sedih, tertekan, atau putus asa?.",
list(opsi.keys())
)

phq3=st.radio(
"Sulit tidur atau tidur berlebihan?.",
list(opsi.keys())
)

phq4=st.radio(
"Merasa Lelah atau kekurangan energi??.",
list(opsi.keys())
)

phq5=st.radio(
"Nafsu makan buruk atau makan berlebihan?.",
list(opsi.keys())
)

phq6=st.radio(
"Sering merasa tidak berharga, merasa gagal, atau merasa mengecewakan diri sendiri atau keluarga?.",
list(opsi.keys())
)

phq7=st.radio(
"Sulit berkonsetrasi?.",
list(opsi.keys())
)

phq8=st.radio(
"Lambat bergerak atau berbicara, sehingga orang lain memperhatikannya? kurang istirahat dan sulit diam lebih dari biasanya?.",
list(opsi.keys())
)

phq9=st.radio(
"Berpikir bahwa lebih baik mati, memiliki pikiran untuk menyakiti diri sendiri dengan cara tertentu?.",
list(opsi.keys())
)

st.header("B. Kuesioner Anxiety")
list(opsi_anxiety.keys(
"Tidak sama sekali":0,
"Beberapa hari saja":1,
"Lebih dari 7 hari":2,
"Hampir setiap hari":3
)
    )

gad1=st.radio(
"Merasa gugup, cemas atau gelisah.",
list(opsi.keys())
)

gad2=st.radio(
"Sulit mengontrol rasa khawatir?.",
list(opsi.keys())
)

gad3=st.radio(
"Terlalu khawatir tentang berbagai hal  .",
list(opsi.keys())
)

gad4=st.radio(
"Kesulitan untuk merasa tenang/relaks .",
list(opsi.keys())
)

gad5=st.radio(
"Merasa begitu gelisah hingga sulit untuk duduk diam .",
list(opsi.keys())
)

gad6=st.radio(
"Mudah merasa terganggu atau tersinggung.",
list(opsi.keys())
)

gad7=st.radio(
"Merasa takut sesuatu yang buruk akan terjadi .",
list(opsi.keys())
)

st.header("B. Kuesioner Emotion Regulation ")
list(opsi_re.keys(
"Sangat Tidak Setuju":1,
"Beberapa Hari":2,
"Agak Tidak Setuju":3,
"Netral / Ragu-Ragu":4,
"Agak Setuju":5,
"Setuju":6,
"Sangat Setuju":7
)
    )

erq1=st.radio(
"Saya mengendalikan emosi dengan mengubah pola pikir saya sesuai dengan situasi di lingkungan sekitar.",
list(opsi.keys())
)

erq2=st.radio(
"Ketika saya ingin merasakan lebih sedikit emosi negatif, saya mengubah pola pikir berdasarkan situasi yang ada.",
list(opsi.keys())
)

erq3=st.radio(
"Ketika saya ingin merasakan lebih banyak emosi positif, saya mengubah pola pikir berdasarkan situasi yang ada.",
list(opsi.keys())
)

erq4=st.radio(
"Ketika saya ingin merasakan lebih banyak emosi positif, maka saya mengubah pola pikir saya.",
list(opsi.keys())
)

erq5=st.radio(
"Ketika saya ingin merasakan lebih sedikit emosi negatif, maka saya mengubah pola pikir saya.",
list(opsi.keys())
)

erq6=st.radio(
"Ketika saya dihadapkan pada situasi yang penuh tekanan, saya berusaha untuk tetap tenang.",
list(opsi.keys())
)

erq7=st.radio(
"Saya mengendalikan emosi dengan tidak mengungkapkannya .",
list(opsi.keys())
)

erq8=st.radio(
"Ketika saya merasakan emosi negatif, saya tidak mengungkapkannya.",
list(opsi.keys())
)

erq9=st.radio(
"Saya memendam perasaan untuk diri sendiri.",
list(opsi.keys())
)

erq10=st.radio(
"Ketika saya merasakan emosi positif, saya berhati-hati untuk tidak mengungkapkannya.",
list(opsi.keys())
)

input_data=pd.DataFrame({

"JK":[jk],
"USIA":[usia],
"SEMESTER":[semester],
"TEMPAT_TINGGAL":[tempat],
})

if st.button("Prediksi"):

    pred = model.predict(input_data)

    st.write(pred)

st.success(

f"Hasil Prediksi : {hasil[0]}"

)
