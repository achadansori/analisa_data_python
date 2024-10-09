import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
data_fix = pd.read_csv('hour.csv')

# Mengelompokkan data berdasarkan hari dalam seminggu dan menghitung total penyewa
data_harian = data_fix.groupby('weekday')['cnt'].sum().reset_index()

# Mendefinisikan label untuk setiap hari dalam bahasa Indonesia
label_data = {
    0: "Minggu",
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu"
}

# Mengubah nilai weekday menjadi label yang telah didefinisikan
data_harian['weekday'] = data_harian["weekday"].map(label_data)

# Mengurutkan data berdasarkan urutan hari dalam seminggu
data_harian = data_harian.sort_values('weekday', key=lambda x: x.map(label_data))

# Mengelompokkan data berdasarkan jam dan menghitung rata-rata penyewa per jam
data_perjam = data_fix.groupby('hr')['cnt'].mean().reset_index()

# Menampilkan judul utama dashboard
st.title("Dashboard Penyewaan Sepeda")

# Menampilkan subjudul untuk total penyewaan sepeda per hari
st.subheader('Total Penyewaan Sepeda per Hari dalam Seminggu')

# Membuat visualisasi berupa barplot untuk total penyewaan sepeda per hari
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='weekday',
    y='cnt',
    data=data_harian,
    palette='viridis',  # Menggunakan palet warna 'viridis'
    ax=ax
)
ax.set_title('Total Penyewaan Sepeda per Hari')  # Menambahkan judul grafik
ax.set_xlabel('Hari')  # Mengatur label sumbu X
ax.set_ylabel('Total Penyewaan')  # Mengatur label sumbu Y
st.pyplot(fig)  # Menampilkan grafik di Streamlit

# Menampilkan subjudul untuk rata-rata penyewaan per jam
st.subheader('Rata-rata Penyewaan Sepeda per Jam')

# Membuat visualisasi berupa lineplot untuk rata-rata penyewaan sepeda per jam
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(
    x='hr',
    y='cnt',
    data=data_perjam,
    marker='o',  # Memberikan marker berbentuk bulat pada setiap titik data
    color='green',  # Mengatur warna garis menjadi hijau
    ax=ax
)
ax.set_title('Rata-rata Penyewaan Sepeda per Jam')  # Menambahkan judul grafik
ax.set_xlabel('Jam')  # Mengatur label sumbu X
ax.set_ylabel('Rata-rata Penyewaan')  # Mengatur label sumbu Y
ax.set_xticks(range(0, 24))  # Mengatur sumbu X agar menampilkan setiap jam dari 0 hingga 23
ax.grid(True)  # Menampilkan garis grid untuk memudahkan pembacaan data
st.pyplot(fig)  # Menampilkan grafik di Streamlit
