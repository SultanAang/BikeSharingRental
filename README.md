# Bike Sharing Rental

# Proyek Analisis Data: Bike Sharing Dataset

## Tentang Bike Sharing Dataset

Sumber dataset dari kaggle https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset yang berisikan file
  - day.csv
  - hour.csv
  - Readme.txt

## Dataset Information 

Bike sharing systems adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses, mulai dari keanggotaan, penyewaan, hingga pengembalian, telah menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari lokasi tertentu dan mengembalikannya di lokasi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang mencakup lebih dari 500 ribu sepeda. Saat ini, sistem-sistem ini mendapat perhatian besar karena perannya yang penting dalam masalah lalu lintas, lingkungan, dan kesehatan.

Selain aplikasi dunia nyata yang menarik dari Bike sharing systems, karakteristik data yang dihasilkan oleh sistem-sistem ini membuatnya menarik untuk penelitian. Berbeda dengan layanan transportasi lainnya seperti bus atau kereta bawah tanah, durasi perjalanan, posisi keberangkatan, dan posisi kedatangan dicatat secara eksplisit dalam sistem ini. Fitur ini mengubah Bike sharing systems menjadi jaringan sensor virtual yang dapat digunakan untuk memantau mobilitas di kota. Oleh karena itu, diharapkan bahwa sebagian besar peristiwa penting di kota dapat dideteksi dengan memantau data ini.

## Menentukan pertanyaan bisnis 
2. Apa faktor utama yang memengaruhi jumlah penggunaan sepeda ?
3. Pelanggan casual lebih sering bersepeda di hari kerja atau libur ? juga sebaliknya
3. di bulan apakah penyewaan sepeda itu sedang tinggi dan di bulan apakah penyewaan sepeda itu sedang turun ?

## Instalasi proyek ini

1. Clone repository ini di komputer kalian sebagai berikut

```
git clone https://github.com/SultanAang/BikeSharingRental.git
```

2. Install library yang dibutuhkan

```
pip install numpy pandas matplotlib seaborn jupyter streamlit babel
```

dengan versi yang digunakan

```
pip install -r requirements.txt
```

3. ketika selesai, lalu pindah ke folder dashboar dengan mengetikan

```
cd dashboard
```

4. Lalu jalankan file dashboard.py

```
streamlit run dashboard.py
```

