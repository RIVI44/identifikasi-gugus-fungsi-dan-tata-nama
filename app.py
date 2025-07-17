gugus_fungsi_kamus = {
    'COOH': 'Asam Karboksilat',
    'CHO': 'Aldehid',
    'CO': 'Keton',
    'OH': 'Alkohol',
    'NH2': 'Amina',
    'COO': 'Ester',
    'C=C': 'Alkena',
    'C≡C': 'Alkuna'
}

def identifikasi_gugus_fungsi(rumus):
    hasil = []
    for gugus, nama in gugus_fungsi_kamus.items():
        if gugus in rumus:
            hasil.append(nama)
    return hasil if hasil else ['Tidak teridentifikasi']

st.title("Identifikasi Gugus Fungsi & Tata Nama Senyawa")

rumus = st.text_input("Masukkan rumus senyawa (contoh: CH3COOH):")

if rumus:
    hasil = identifikasi_gugus_fungsi(rumus)

    if 'Asam Karboksilat' in hasil:
        nama = f"Asam {rumus.lower()}"
    elif 'Aldehid' in hasil:
        nama = f"…
