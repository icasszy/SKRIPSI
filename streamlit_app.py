import streamlit as st
import pandas as pd
import joblib

model = joblib.load("catboost_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(
    page_title="Klasifikasi Tingkat Depresi Mahasiswa",
    page_icon="🧠",
    layout="wide"
)
st.title("🧠 Klasifikasi Tingkat Depresi Mahasiswa")

st.write(
"""
Silakan isi seluruh pertanyaan berikut sesuai kondisi Anda.
Data hanya digunakan untuk proses klasifikasi menggunakan model Machine Learning CatBoost.
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
)

tempat_mapping={
"Keluarga":0,
"Sendiri":1
}

jk=jk_mapping[jk]
tempat=tempat_mapping[tempat]

st.header("B. Kuesioner Depression ")
opsi_dep = {
"Tidak Pernah":0,
"Beberapa Hari":1,
"Lebih dari separuh waktu yang dimaksud":2,
"Hampir setiap hari":3
}

phq1=st.radio(
"Kurang berminat atau bergairah dalam melakukan apapun.",
list(opsi_dep.keys())
)

phq2=st.radio(
"Merasa sedih, tertekan, atau putus asa?.",
list(opsi_dep.keys())
)

phq3=st.radio(
"Sulit tidur atau tidur berlebihan?.",
list(opsi_dep.keys())
)

phq4=st.radio(
"Merasa Lelah atau kekurangan energi??.",
list(opsi_dep.keys())
)

phq5=st.radio(
"Nafsu makan buruk atau makan berlebihan?.",
list(opsi_dep.keys())
)

phq6=st.radio(
"Sering merasa tidak berharga, merasa gagal, atau merasa mengecewakan diri sendiri atau keluarga?.",
list(opsi_dep.keys())
)

phq7=st.radio(
"Sulit berkonsetrasi?.",
list(opsi_dep.keys())
)

phq8=st.radio(
"Lambat bergerak atau berbicara, sehingga orang lain memperhatikannya? kurang istirahat dan sulit diam lebih dari biasanya?.",
list(opsi_dep.keys())
)

phq9=st.radio(
"Berpikir bahwa lebih baik mati, memiliki pikiran untuk menyakiti diri sendiri dengan cara tertentu?.",
list(opsi_dep.keys())
)

st.header("B. Kuesioner Anxiety")
opsi_anxiety = {
"Tidak sama sekali":0,
"Beberapa hari saja":1,
"Lebih dari 7 hari":2,
"Hampir setiap hari":3
}

gad1=st.radio(
"Merasa gugup, cemas atau gelisah.",
list(opsi_anxiety.keys())
)

gad2=st.radio(
"Sulit mengontrol rasa khawatir?.",
list(opsi_anxiety.keys())
)

gad3=st.radio(
"Terlalu khawatir tentang berbagai hal  .",
list(opsi_anxiety.keys())
)

gad4=st.radio(
"Kesulitan untuk merasa tenang/relaks .",
list(opsi_anxiety.keys())
)

gad5=st.radio(
"Merasa begitu gelisah hingga sulit untuk duduk diam .",
list(opsi_anxiety.keys())
)

gad6=st.radio(
"Mudah merasa terganggu atau tersinggung.",
list(opsi_anxiety.keys())
)

gad7=st.radio(
"Merasa takut sesuatu yang buruk akan terjadi .",
list(opsi_anxiety.keys())
)

st.header("B. Kuesioner Emotion Regulation ")
opsi_re = {
"Sangat Tidak Setuju":1,
"Beberapa Hari":2,
"Agak Tidak Setuju":3,
"Netral / Ragu-Ragu":4,
"Agak Setuju":5,
"Setuju":6,
"Sangat Setuju":7
}

erq1=st.radio(
"Saya mengendalikan emosi dengan mengubah pola pikir saya sesuai dengan situasi di lingkungan sekitar.",
list(opsi_re.keys())
)

erq2=st.radio(
"Ketika saya ingin merasakan lebih sedikit emosi negatif, saya mengubah pola pikir berdasarkan situasi yang ada.",
list(opsi_re.keys())
)

erq3=st.radio(
"Ketika saya ingin merasakan lebih banyak emosi positif, saya mengubah pola pikir berdasarkan situasi yang ada.",
list(opsi_re.keys())
)

erq4=st.radio(
"Ketika saya ingin merasakan lebih banyak emosi positif, maka saya mengubah pola pikir saya.",
list(opsi_re.keys())
)

erq5=st.radio(
"Ketika saya ingin merasakan lebih sedikit emosi negatif, maka saya mengubah pola pikir saya.",
list(opsi_re.keys())
)

erq6=st.radio(
"Ketika saya dihadapkan pada situasi yang penuh tekanan, saya berusaha untuk tetap tenang.",
list(opsi_re.keys())
)

erq7=st.radio(
"Saya mengendalikan emosi dengan tidak mengungkapkannya .",
list(opsi_re.keys())
)

erq8=st.radio(
"Ketika saya merasakan emosi negatif, saya tidak mengungkapkannya.",
list(opsi_re.keys())
)

erq9=st.radio(
"Saya memendam perasaan untuk diri sendiri.",
list(opsi_re.keys())
)

erq10=st.radio(
"Ketika saya merasakan emosi positif, saya berhati-hati untuk tidak mengungkapkannya.",
list(opsi_re.keys())
)

phq1 = opsi_dep[phq1]
phq2 = opsi_dep[phq2]
phq3 = opsi_dep[phq3]
phq4 = opsi_dep[phq4]
phq5 = opsi_dep[phq5]
phq6 = opsi_dep[phq6]
phq7 = opsi_dep[phq7]
phq8 = opsi_dep[phq8]
phq9 = opsi_dep[phq9]

gad1 = opsi_anxiety[gad1]
gad2 = opsi_anxiety[gad2]
gad3 = opsi_anxiety[gad3]
gad4 = opsi_anxiety[gad4]
gad5 = opsi_anxiety[gad5]
gad6 = opsi_anxiety[gad6]
gad7 = opsi_anxiety[gad7]

erq1 = opsi_re[erq1]
erq2 = opsi_re[erq2]
erq3 = opsi_re[erq3]
erq4 = opsi_re[erq4]
erq5 = opsi_re[erq5]
erq6 = opsi_re[erq6]
erq7 = opsi_re[erq7]
erq8 = opsi_re[erq8]
erq9 = opsi_re[erq9]
erq10 = opsi_re[erq10]

input_data = pd.DataFrame({

"USIA":[usia],
"SEMESTER":[semester],

"PHQ_1":[phq1],
"PHQ_2":[phq2],
"PHQ_3":[phq3],
"PHQ_4":[phq4],
"PHQ_5":[phq5],
"PHQ_6":[phq6],
"PHQ_7":[phq7],
"PHQ_8":[phq8],
"PHQ_9":[phq9],

"GAD_1":[gad1],
"GAD_2":[gad2],
"GAD_3":[gad3],
"GAD_4":[gad4],
"GAD_5":[gad5],
"GAD_6":[gad6],
"GAD_7":[gad7],

"ERQ_1":[erq1],
"ERQ_2":[erq2],
"ERQ_3":[erq3],
"ERQ_4":[erq4],
"ERQ_5":[erq5],
"ERQ_6":[erq6],
"ERQ_7":[erq7],
"ERQ_8":[erq8],
"ERQ_9":[erq9],
"ERQ_10":[erq10],

"JK":[jk],
"TEMPAT_TINGGAL":[tempat]

})

if st.button("Klasifikasi"):

    pred = model.predict(input_data)

    hasil = label_encoder.inverse_transform(pred.astype(int))

    st.success(f"Hasil Klasifikasi : {hasil[0]}")
