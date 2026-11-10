
import streamlit as st

st.set_page_config(
    page_title="Kasir Clothes Shop", page_icon="🛍️", layout="centered"
)

st.title("🛍️ Clothes Shop Makassar")
st.write("Jl. Tamangapa Raya No.23 - Makassar | Hp 083 356 445 980")

katalog = [
    {"nama": "KAOS LENGAN PANJANG", "harga": 34500},
    {"nama": "KAOS LENGAN PENDEK", "harga": 25000},
    {"nama": "CELANA PANJANG", "harga": 56000},
    {"nama": "CELANA PENDEK", "harga": 49000},
    {"nama": "ROK PLISKET", "harga": 37000},
    {"nama": "ROK KAIN", "harga": 35000},
    {"nama": "DALEMAN JILBAB", "harga": 12000},
    {"nama": "JILBAB PASANG BERGO", "harga": 17000},
    {"nama": "JILBAB SEGIEMPAT", "harga": 29000},
    {"nama": "JAKET", "harga": 39000},
    {"nama": "HOODIE", "harga": 4500},
    {"nama": "KEMEJA", "harga": 43000},
    {"nama": "JAS KERJA", "harga": 74000},
    {"nama": "TAS SEKOLAH", "harga": 134000},
    {"nama": "DASI", "harga": 27600},
]

if "keranjang" not in st.session_state:
  st.session_state.keranjang = []

opsi_produk = [
    f"{i+1}. {item['nama']} - Rp {item['harga']:,}"
    for i, item in enumerate(katalog)
]
pilihan = st.selectbox("Pilih Produk (Maks 10 Item)", opsi_produk)
qty = st.number_input("Jumlah (Qty)", min_value=1, value=1, step=1)

if st.button("+ Tambah ke Keranjang"):
  if len(st.session_state.keranjang) >= 10:
    st.error("Keranjang sudah penuh (Maksimal 10 jenis barang)!")
  else:
    idx = opsi_produk.index(pilihan)
    produk_pilihan = katalog[idx]
    subtotal = produk_pilihan["harga"] * qty
    st.session_state.keranjang.append({
        "nama": produk_pilihan["nama"],
        "harga": produk_pilihan["harga"],
        "qty": qty,
        "subtotal": subtotal,
    })
    st.success(f"Berhasil menambahkan {produk_pilihan['nama']} ({qty}x)")

if st.session_state.keranjang:
  st.subheader("🛒 Item Belanjaan")
  total_belanja = sum(item["subtotal"] for item in st.session_state.keranjang)
  total_qty = sum(item["qty"] for item in st.session_state.keranjang)

  for idx, item in enumerate(st.session_state.keranjang):
    st.write(
        f"{idx+1}. **{item['nama']}** - {item['qty']}x @ Rp"
        f" {item['harga']:,} = **Rp {item['subtotal']:,}**"
    )

  st.markdown(f"### Total Belanja: **Rp {total_belanja:,}**")

  bayar = st.number_input("Uang Tunai (Rp)", min_value=0, step=1000)

  if st.button("🖨️ Cetak Struk"):
    if bayar < total_belanja:
      st.error("Uang tunai kurang dari total belanja!")
    else:
      kembalian = bayar - total_belanja
      waktu = datetime.now()
      tgl_str = waktu.strftime("%d.%m.%y")
      jam_str = waktu.strftime("[%H:%M]")

      struk = f"""
========================================
          CLOTHES SHOP         
         ~ MURAH DAN BERKAH ~           

     JL. TAMANGAPA RAYA NO.23 - MAKASSAR    
           Hp 083 356 445 980            
         BISA DELIVERY LHO...           
----------------------------------------
TRANS : 002-194709001                   
KASIR : 002-KELOMPOK 4      {tgl_str} {jam_str}
----------------------------------------
"""
      for item in st.session_state.keranjang:
        struk += f"{item['nama']}\n"
        struk += (
            f"{float(item['qty']):6.2f} X @{item['harga']:7,}"
            f"   : {item['subtotal']:10,}\n"
        )

      struk += f"""----------------------------------------
Item : {len(st.session_state.keranjang):<4} TOTAL    :Rp {total_belanja:>10,}
{'':<21} TUNAI    :Rp {bayar:>10,}
Qty  : {total_qty:<4} KEMBALI  :Rp {kembalian:>10,}
----------------------------------------
   == TERIMA KASIH ATAS KUNJUNGAN ANDA ==

        SELAMAT DATANG KEMBALI         
 BARANG TELAH DIBELI TIDAK DAPAT DIKEMBALIKAN
========================================
"""
      st.code(struk, language="text")
      if st.button("Transaksi Baru"):
        st.session_state.keranjang = []
        st.rerun()
