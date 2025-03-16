 # Premier League Predictor

**Premier League Predictor** adalah aplikasi desktop berbasis Python yang memungkinkan pengguna untuk:
- Menampilkan klasemen Liga Inggris dengan format yang rapi.
- Melakukan prediksi pertandingan (termasuk skor) menggunakan model Machine Learning (RandomForestClassifier).
- Menggunakan antarmuka grafis (GUI) dengan Tkinter agar lebih interaktif.

## Fitur Utama

- **Tampilan Klasemen:** Data klasemen ditampilkan dalam jendela baru dengan format yang rapi.
- **Prediksi Pertandingan:** Menggunakan dua model (satu untuk prediksi gol kandang dan satu untuk gol tandang) untuk memprediksi hasil pertandingan, termasuk skor dan hasil akhir (menang, kalah, atau seri).



 # Struktur Proyek
premier_league/
├── src/
│   ├── py/
│   │   ├── main.py                  
│   │   ├── pengambil_data.py         
│   │   ├── prediksi_pertandingan.py  
│   │   └── klasemen.py               
│   └── ipynb/
│       └── premier_league.ipynb      
├── data/
│   ├── raw_data/
│   │   └── premier_league_data.csv       
│   └── result/
│       ├── clasement_premier_league_with_percentage.csv
│       ├── clasement_premier_league.csv
│       ├── football_stats.png
│       └── predict_score.png
├── README.md                         
└── requirements.txt                 
