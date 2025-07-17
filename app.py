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

title("identifikasi gugus fungsi dan tata nama senyawa")

rumus = st.text_input("Masukkan rumus senyawa (contoh: CH3COOH):")

if rumus:
    hasil = identifikasi_gugus_fungsi(rumus)
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

    st.markdown("### Hasil Identifikasi:")
    st.write(f"*Rumus:* {rumus}")
    st.write(f"*Gugus Fungsi:* {', '.join(hasil)}")
    st.write(f"*Nama Senyawa:* {nama}")
