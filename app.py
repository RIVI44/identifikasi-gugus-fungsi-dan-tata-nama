# filename: app.py
import streamlit as st

# Kamus gugus fungsi
gugus_fungsi_kamus = {
    'COOH': 'Asam Karboksilat',
    'CHO': 'Aldehid',
    'CO': 'Keton',
    'OH': 'Alkohol',
    'NH2': 'Amina',
    'COO': 'Ester',
    'C=C': 'Alkena',
    'C≡C': 'Alkuna',
    'C-C': 'Alkana',
    'C6H5-': 'Fenil'
    

    
}

# Fungsi identifikasi
def identifikasi_gugus_fungsi(rumus):
    hasil = []
    for gugus, nama in gugus_fungsi_kamus.items():
        if gugus in rumus:
            hasil.append(nama)
    return hasil if hasil else ['Tidak teridentifikasi']

# Judul halaman
st.title("Identifikasi Gugus Fungsi & Tata Nama Senyawa Organik")

# Input rumus
rumus = st.text_input("Masukkan rumus senyawa (contoh: CH3COOH):")

# Jika user memasukkan rumus
if rumus:
    hasil = identifikasi_gugus_fungsi(rumus)

    # Penamaan IUPAC sederhana
    if 'Asam Karboksilat' in hasil:
        nama = f"Asam {rumus.lower()}"
    elif 'Aldehid' in hasil:
        nama = f"{rumus.lower()} - al"
    elif 'Keton' in hasil:
        nama = f"{rumus.lower()} - on"
    elif 'Alkohol' in hasil:
        nama = f"{rumus.lower()} - ol"
    elif 'Amina' in hasil:
        nama = f"{rumus.lower()} - amina"
    else:
        nama = "Tidak diketahui"

    # Output ke layar
    st.markdown("### Hasil Identifikasi:")
    st.write(f"*Rumus:* {rumus}")
    st.write(f"*Gugus Fungsi:* {', '.join(hasil)}")
    st.write(f"*Nama Senyawa:* {nama}")
