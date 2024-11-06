import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Model Sistem Dinamika untuk Peningkatan Stunting

# Parameter model
def model(y, t, intervensi_rate):
    # Variabel stok
    stunting = y[0]
    
    # Aliran (misalnya penurunan stunting karena intervensi kesehatan)
    # Semakin tinggi intervensi_rate, semakin cepat penurunan stunting
    d_stunting_dt = -intervensi_rate * stunting
    
    return [d_stunting_dt]

# Persentase stunting awal berdasarkan data
# Data awal stunting di wilayah Sumatera Utara
data_stunting = {
    "Nias": 61.3,
    "Mandailing Natal": 48.3,
    "Padang Lawas Utara": 47.5,
    "Nias Barat": 45.9,
    "Serdang Bedagai": 36.0
}

# Parameter laju intervensi (misalnya, 1% per tahun penurunan stunting)
intervensi_rate = 0.01  # 1% per tahun

# Waktu simulasi (dalam tahun)
t = np.linspace(2018, 2024, 100)

# Plot hasil simulasi untuk setiap wilayah
plt.figure(figsize=(10, 6))

# Menambahkan tingkat intervensi yang berbeda-beda untuk tiap wilayah
intervensi_rate_per_region = {
    "Nias": 0.015,  # 1.5% per tahun
    "Mandailing Natal": 0.01,  # 1% per tahun
    "Padang Lawas Utara": 0.02,  # 2% per tahun
    "Nias Barat": 0.01,  # 1% per tahun
    "Serdang Bedagai": 0.012  # 1.2% per tahun
}

# Plot hasil simulasi untuk setiap wilayah
plt.figure(figsize=(10, 6))

for region, stunting_initial in data_stunting.items():
    # Initial condition (jumlah anak yang mengalami stunting pada tahun pertama)
    y0 = [stunting_initial]
    
    # Ambil tingkat intervensi untuk wilayah tersebut
    intervensi_rate = intervensi_rate_per_region[region]
    
    # Simulasi menggunakan odeint
    result = odeint(model, y0, t, args=(intervensi_rate,))
    
    # Plot hasil simulasi
    plt.plot(t, result[:, 0], label=f'{region} (Awal: {stunting_initial}%)')

# Menambahkan label dan judul
plt.title('Simulasi Penurunan Stunting di Sumatera Utara (Dengan Variasi Intervensi)')
plt.xlabel('Waktu (Tahun)')
plt.ylabel('Persentase Stunting')
plt.legend(loc='best')
plt.grid(True)
plt.show()

