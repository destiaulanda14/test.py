import streamlit as st

# Halaman utama
def main():
    st.title("Kalkulator Konsentrasi")
    st.write("Masukkan data di bawah untuk menghitung konsentrasi larutan:")

    # Input
    massa_zat = st.number_input("Massa Zat (gram):", min_value=0.0, format="%.2f")
    volume = st.number_input("Volume Larutan (liter):", min_value=0.0, format="%.2f")
    massa_molar = st.number_input("Massa Molar (g/mol):", min_value=0.0, format="%.2f")

    # Tombol submit
    if st.button("Submit"):
        if volume > 0 and massa_molar > 0:
            konsentrasi = massa_zat / (volume * massa_molar)
            st.success(f"Konsentrasi: {konsentrasi:.4f} mol/L")
        else:
            st.error("Volume dan massa molar harus lebih dari 0.")

    # Tombol kembali
    if st.button("Kembali"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
