import streamlit as st

st.set_page_config(
    page_title="Prediksi Tingkat Depresi Mahasiswa",
    page_icon="🧠",
    layout="wide"
)

jk = st.selectbox(
    "Jenis Kelamin",
    ["Perempuan","Laki-laki"]
)

usia = st.number_input(
    "Usia",
    17,
    30,
    20
)

semester = st.number_input(
    "Semester",
    1,
    14,
    4
)

if jk=="Perempuan":
    jk=0
else:
    jk=1

tempat_mapping = {
    "Keluarga": 0,
    "Sendiri": 1
}
tempat = st.selectbox(
    "Tempat Tinggal",
    ["Keluarga", "Sendiri"]
)

tempat = tempat_mapping[tempat]

import pandas as pd

input_data=pd.DataFrame({

"JK":[jk],
"USIA":[usia],
"SEMESTER":[semester],
"TEMPAT_TINGGAL":[tempat],
})

if st.button("Prediksi"):

    pred = model.predict(input_data)

    st.write(pred)

hasil=label_encoder.inverse_transform(pred)

st.success(

f"Hasil Prediksi : {hasil[0]}"

)
