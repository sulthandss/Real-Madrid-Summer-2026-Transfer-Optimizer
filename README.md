# Real Madrid Transfer Optimizer ⚽

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)

Sebuah aplikasi web interaktif yang memodelkan dan mengoptimalkan strategi transfer klub sepak bola menggunakan **Persoalan Knapsack 0/1** dan **Program Dinamis**. Proyek ini merupakan implementasi kode dari makalah akademik untuk mata kuliah Matematika Diskrit (IF1220).

**Oleh:** Sulthan Dhiyazka Suwandi (13525124)  
**Institusi:** Program Studi Teknik Informatika, Sekolah Teknik Elektro dan Informatika, Institut Teknologi Bandung 

## 📖 Latar Belakang

Klub sepak bola modern beroperasi di bawah batasan finansial yang ketat. Setiap target transfer memiliki biaya tertentu (bobot) dan Indeks Kecocokan Taktis atau *Tactical Fit Index* (nilai). Tujuan dari algoritma ini adalah untuk menyeleksi himpunan bagian target yang memaksimalkan kontribusi taktikal tanpa melebihi batas anggaran (kapasitas).

Proyek ini memecahkan dilema tersebut secara matematis, membuktikan bahwa akuisisi beberapa pemain terukur seringkali memberikan nilai skuad yang jauh lebih tinggi dibandingkan merekrut satu megabintang secara *greedy*.

## 🚀 Cara Menjalankan Program

Aplikasi ini dibangun menggunakan **Streamlit**. Ikuti langkah-langkah berikut untuk menjalankannya di mesin lokal Anda:

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/sulthandss/Real-Madrid-Summer-2026-Transfer-Optimizer.git]
   cd real-madrid-knapsack
