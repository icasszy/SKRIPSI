import streamlit as st
import pandas as pd
import joblib

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Klasifikasi Tingkat Depresi Mahasiswa",
    layout="wide",
    page_icon="🧠"
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("catboost_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
    .main {
        background: linear-gradient(180deg, #f4f8fb 0%, #eef4f7 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .hero-box {
        background: white;
        padding: 2rem 2.2rem;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #e9eef3;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 0.3rem;
        text-align: center;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #6b7280;
        text-align: center;
        line-height: 1.7;
    }

    .section-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 1.5rem;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        margin-bottom: 1.2rem;
        border: 1px solid #edf2f7;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.8rem;
    }

    .small-note {
        color: #64748b;
        font-size: 0.95rem;
        margin-bottom: 0.8rem;
    }

    .result-box {
        background: #ffffff;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 22px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        text-align: center;
        margin-top: 1.5rem;
    }

    .result-label {
        font-size: 0.95rem;
        color: #6b7280;
        margin-bottom: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .badge-success, .badge-warning, .badge-danger, .badge-info {
        display: inline-block;
        padding: 0.9rem 1.8rem;
        border-radius: 14px;
        font-size: 1.8rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
    }

    .badge-success {
        background: linear-gradient(135deg, #16a34a, #22c55e);
    }

    .badge-warning {
        background: linear-gradient(135deg, #f59e0b, #fbbf24);
    }

    .badge-danger {
        background: linear-gradient(135deg, #dc2626, #ef4444);
    }

    .badge-info {
        background: linear-gradient(135deg, #2563eb, #3b82f6);
    }

    .result-desc {
        color: #475569;
        font-size: 1rem;
        line-height: 1.7;
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #16a34a, #22c55e);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        font-size: 1rem;
        font-weight: 700;
        box-shadow: 0 6px 16px rgba(34,197,94,0.35);
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #15803d, #16a34a);
        color: white;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    input, textarea {
        border-radius: 10px !important;
    }

    .stRadio > label {
        font-weight: 600;
        color: #334155;
    }

    hr {
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="hero-box">
    <div class="hero-title">Klasifikasi Tingkat Depresi Mahasiswa</div>
    <div class="hero-subtitle">
        Silakan isi seluruh pertanyaan berikut sesuai kondisi Anda.<br>
        Data digunakan untuk proses klasifikasi menggunakan model Machine Learning <b>CatBoost</b>.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# MAPPING
# =========================
jk_mapping = {
    "Perempuan": 0,
    "Laki-laki": 1
}

tempat_mapping = {
    "Keluarga": 0,
    "Sendiri": 1
}

opsi_dep = {
    "Tidak Pernah": 0,
    "Beberapa Hari": 1,
    "Lebih dari separuh waktu yang dimaksud": 2,
    "Hampir setiap hari": 3
}

opsi_anxiety = {
    "Tidak sama sekali": 0,
    "Beberapa hari saja": 1,
    "Lebih dari 7 hari": 2,
    "Hampir setiap hari": 3
}

opsi_re = {
    "Sangat Tidak Setuju": 1,
    "Tidak Setuju": 2,
    "Agak Tidak Setuju": 3,
    "Netral / Ragu-Ragu": 4,
    "Agak Setuju": 5,
    "Setuju": 6,
    "Sangat Setuju": 7
}

# =========================
# IDENTITAS
# =========================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">A. Identitas Responden</div>', unsafe_allow_html=True)
st.markdown('<div class="small-note">Masukkan data dasar responden terlebih dahulu.</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    usia = st.number_input("Usia", min_value=17, max_value=30, value=20)

with col2:
    jk = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])

with col3:
    semester = st.number_input("Semester", min_value=1, max_value=14, value=4)

with col4:
    tempat = st.selectbox("Tempat Tinggal", ["Keluarga", "Sendiri"])

st.markdown('</div>', unsafe_allow_html=True)

jk = jk_mapping[jk]
tempat = tempat_mapping[tempat]

# =========================
# PHQ
# =========================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">B. Kuesioner Depression (PHQ)</div>', unsafe_allow_html=True)

phq1 = st.radio("1. Kurang berminat atau bergairah dalam melakukan apapun.", list(opsi_dep.keys()), horizontal=True)
phq2 = st.radio("2. Merasa sedih, tertekan, atau putus asa.", list(opsi_dep.keys()), horizontal=True)
phq3 = st.radio("3. Sulit tidur atau tidur berlebihan.", list(opsi_dep.keys()), horizontal=True)
phq4 = st.radio("4. Merasa lelah atau kekurangan energi.", list(opsi_dep.keys()), horizontal=True)
phq5 = st.radio("5. Nafsu makan buruk atau makan berlebihan.", list(opsi_dep.keys()), horizontal=True)
phq6 = st.radio("6. Sering merasa tidak berharga, merasa gagal, atau merasa mengecewakan diri sendiri/keluarga.", list(opsi_dep.keys()), horizontal=True)
phq7 = st.radio("7. Sulit berkonsentrasi.", list(opsi_dep.keys()), horizontal=True)
phq8 = st.radio("8. Lambat bergerak/berbicara atau justru sangat gelisah dan sulit diam.", list(opsi_dep.keys()), horizontal=True)
phq9 = st.radio("9. Berpikir bahwa lebih baik mati atau memiliki pikiran menyakiti diri sendiri.", list(opsi_dep.keys()), horizontal=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# GAD
# =========================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">C. Kuesioner Anxiety (GAD)</div>', unsafe_allow_html=True)

gad1 = st.radio("1. Merasa gugup, cemas atau gelisah.", list(opsi_anxiety.keys()), horizontal=True)
gad2 = st.radio("2. Sulit mengontrol rasa khawatir.", list(opsi_anxiety.keys()), horizontal=True)
gad3 = st.radio("3. Terlalu khawatir tentang berbagai hal.", list(opsi_anxiety.keys()), horizontal=True)
gad4 = st.radio("4. Kesulitan untuk merasa tenang/relaks.", list(opsi_anxiety.keys()), horizontal=True)
gad5 = st.radio("5. Merasa begitu gelisah hingga sulit untuk duduk diam.", list(opsi_anxiety.keys()), horizontal=True)
gad6 = st.radio("6. Mudah merasa terganggu atau tersinggung.", list(opsi_anxiety.keys()), horizontal=True)
gad7 = st.radio("7. Merasa takut sesuatu yang buruk akan terjadi.", list(opsi_anxiety.keys()), horizontal=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# ERQ
# =========================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">D. Kuesioner Emotion Regulation (ERQ)</div>', unsafe_allow_html=True)

erq1 = st.radio("1. Saya mengendalikan emosi dengan mengubah pola pikir sesuai situasi di lingkungan sekitar.", list(opsi_re.keys()), horizontal=True)
erq2 = st.radio("2. Ketika saya ingin merasakan lebih sedikit emosi negatif, saya mengubah pola pikir berdasarkan situasi yang ada.", list(opsi_re.keys()), horizontal=True)
erq3 = st.radio("3. Ketika saya ingin merasakan lebih banyak emosi positif, saya mengubah pola pikir berdasarkan situasi yang ada.", list(opsi_re.keys()), horizontal=True)
erq4 = st.radio("4. Ketika saya ingin merasakan lebih banyak emosi positif, maka saya mengubah pola pikir saya.", list(opsi_re.keys()), horizontal=True)
erq5 = st.radio("5. Ketika saya ingin merasakan lebih sedikit emosi negatif, maka saya mengubah pola pikir saya.", list(opsi_re.keys()), horizontal=True)
erq6 = st.radio("6. Ketika saya dihadapkan pada situasi yang penuh tekanan, saya berusaha untuk tetap tenang.", list(opsi_re.keys()), horizontal=True)
erq7 = st.radio("7. Saya mengendalikan emosi dengan tidak mengungkapkannya.", list(opsi_re.keys()), horizontal=True)
erq8 = st.radio("8. Ketika saya merasakan emosi negatif, saya tidak mengungkapkannya.", list(opsi_re.keys()), horizontal=True)
erq9 = st.radio("9. Saya memendam perasaan untuk diri sendiri.", list(opsi_re.keys()), horizontal=True)
erq10 = st.radio("10. Ketika saya merasakan emosi positif, saya berhati-hati untuk tidak mengungkapkannya.", list(opsi_re.keys()), horizontal=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# ENCODE
# =========================
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

# =========================
# DATAFRAME
# =========================
input_data = pd.DataFrame({
    "USIA": [usia],
    "SEMESTER": [semester],

    "PHQ_1": [phq1],
    "PHQ_2": [phq2],
    "PHQ_3": [phq3],
    "PHQ_4": [phq4],
    "PHQ_5": [phq5],
    "PHQ_6": [phq6],
    "PHQ_7": [phq7],
    "PHQ_8": [phq8],
    "PHQ_9": [phq9],

    "GAD_1": [gad1],
    "GAD_2": [gad2],
    "GAD_3": [gad3],
    "GAD_4": [gad4],
    "GAD_5": [gad5],
    "GAD_6": [gad6],
    "GAD_7": [gad7],

    "ERQ_1": [erq1],
    "ERQ_2": [erq2],
    "ERQ_3": [erq3],
    "ERQ_4": [erq4],
    "ERQ_5": [erq5],
    "ERQ_6": [erq6],
    "ERQ_7": [erq7],
    "ERQ_8": [erq8],
    "ERQ_9": [erq9],
    "ERQ_10": [erq10],

    "JK": [jk],
    "TEMPAT_TINGGAL": [tempat]
})

# =========================
# BUTTON
# =========================
if st.button("🔍 KLASIFIKASI SEKARANG"):
    pred = model.predict(input_data)
    hasil = label_encoder.inverse_transform(pred.astype(int))[0]

    if hasil == "Depresi Ringan":
        badge_class = "badge-warning"
    elif hasil == "Depresi Sedang":
        badge_class = "badge-warning"
    elif hasil == "Depresi Berat":
        badge_class = "badge-danger"
    else:
        badge_class = "badge-success"

    st.markdown(f"""
    <div class="result-box">
        <div class="result-label">Hasil Klasifikasi Tingkat Depresi</div>
        <div class="{badge_class}">{hasil}</div>
        <div class="result-desc">
            Hasil ini merupakan keluaran otomatis dari model <b>CatBoost</b> dan
            <b>bukan diagnosis psikologis profesional</b>. Jika hasil menunjukkan
            kondisi yang mengkhawatirkan, pertimbangkan untuk berkonsultasi dengan
            psikolog atau tenaga profesional.
        </div>
    </div>
    """, unsafe_allow_html=True)
