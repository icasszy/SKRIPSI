# 🧠 Perbandingan Performa Algoritma XGBoost dan CatBoost dalam Klasifikasi Tingkat Depresi Mahasiswa

## 📖 Deskripsi Penelitian

Penelitian ini bertujuan untuk membandingkan performa algoritma **XGBoost** dan **CatBoost** dalam melakukan klasifikasi tingkat depresi mahasiswa berdasarkan faktor-faktor psikologis dan karakteristik responden.

Klasifikasi dilakukan ke dalam tiga kategori tingkat depresi, yaitu:

- Depresi Ringan
- Depresi Sedang
- Depresi Berat

Penelitian menerapkan beberapa tahapan machine learning mulai dari preprocessing data, penanganan ketidakseimbangan kelas menggunakan **SMOTE**, optimasi hyperparameter menggunakan **GridSearchCV**, hingga evaluasi model menggunakan berbagai metrik performa.

---

## 🎯 Tujuan Penelitian

- Mengklasifikasikan tingkat depresi mahasiswa.
- Membandingkan performa algoritma XGBoost dan CatBoost.
- Menentukan model terbaik berdasarkan nilai evaluasi.
- Mengidentifikasi fitur yang paling berpengaruh terhadap prediksi tingkat depresi.

---

## 📊 Dataset

Dataset penelitian terdiri dari data mahasiswa yang mencakup beberapa variabel, antara lain:

| Variabel |
|-----------|
| Jenis Kelamin |
| Usia |
| Tempat Tinggal |
| Semester |
| Total Skor Regulasi Emosi (TOT_RE) |
| Total Skor Kecemasan (TOT_CEMAS) |
| Tingkat Depresi |

Target klasifikasi:

| Label | Kategori |
|---------|---------|
| 0 | Depresi Ringan |
| 1 | Depresi Sedang |
| 2 | Depresi Berat |

---

## ⚙️ Metodologi

Tahapan penelitian:

1. Data Cleaning
2. Data Transformation
3. Label Encoding
4. Feature Selection
5. Data Splitting
   - 80:20
   - 70:30
   - 60:40
6. SMOTE (Synthetic Minority Oversampling Technique)
7. Hyperparameter Tuning menggunakan GridSearchCV
8. K-Fold Cross Validation
9. Pemodelan:
   - XGBoost
   - CatBoost
10. Evaluasi Model
11. Analisis SHAP

---

## 📈 Metrik Evaluasi

Model dievaluasi menggunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🛠️ Library yang Digunakan

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
catboost
imbalanced-learn
shap
```

## 📂 Struktur Project

```bash
Depression-Classification/
│
├── Dataset/
│   └── dataset_depresi.csv
│
├── Notebook/
│   └── penelitian_depresi.ipynb
│
├── Model/
│   ├── xgboost_model.pkl
│   └── catboost_model.pkl
│
├── Images/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── shap_summary.png
│
└── README.md
```

## 🏆 Hasil Penelitian

Berdasarkan hasil eksperimen, model CatBoost menunjukkan performa terbaik dalam klasifikasi tingkat depresi mahasiswa dibandingkan dengan XGBoost pada skenario pembagian data yang diuji.

## 👩‍🎓 Penulis

Deisya Dzakiyyah

Program Studi Sistem Informasi

Universitas Muhammadiyah Kalimantan Timur
