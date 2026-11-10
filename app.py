import streamlit as st
import streamlit.components.v1 as components
import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="Clothes Shop - Minimarket Fashion",
    page_icon="🛍️",
    layout="wide"
)

# Styling CSS utama aplikasi
st.markdown("""
<style>
    .main-header {
        background-color: #03ac0e;
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .product-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 15px;
    }
    .product-title {
        font-weight: 600;
        font-size: 15px;
        color: #212121;
        margin: 8px 0;
    }
    .product-price {
        font-weight: 800;
        color: #fa591d;
        font-size: 16px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Inisialisasi Database Produk Pakaian
if "products" not in st.session_state:
    st.session_state.products = [
        {"id": 1, "name": "Kemeja Flanel Kotak Premium", "price": 150000, "category": "Atasan", "sold": "1.2rb"},
        {"id": 2, "name": "Kaos Polos Cotton Combed 30s", "price": 75000, "category": "Kaos", "sold": "3.4rb"},
        {"id": 3, "name": "Celana Jeans Denim Slim Fit", "price": 250000, "category": "Bawahan", "sold": "850"},
        {"id": 4, "name": "Jaket Hoodie Fleece Oversize", "price": 200000, "category": "Outerwear", "sold": "2.1rb"},
        {"id": 5, "name": "Topi Baseball Bordir Minimalis", "price": 50000, "category": "Aksesoris", "sold": "920"},
        {"id": 6, "name": "Dress Kasual Wanita Katun", "price": 185000, "category": "Wanita", "sold": "640"}
    ]

# Inisialisasi Keranjang Belanja
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "receipt_data" not in st.session_state:
    st.session_state.receipt_data = None

# Header Utama
st.markdown('<div class="main-header"><h2>🛒 CLOTHES SHOP</h2><span>Minimarket Fashion & Apparel</span></div>', unsafe_allow_html=True)

# Jika transaksi sudah selesai dan struk tercetak
if st.session_state.receipt_data:
    r = st.session_state.receipt_data
    st.success("Transaksi Berhasil! Berikut Struk Pembayaran Anda:")
    
    # Render item struk secara dinamis ke dalam HTML
    items_html = ""
    for item in r['items']:
        sub_total_str = f"Rp. {item['subtotal']:,.0f}".replace(",", ".")
        price_str = f"{item['price']:,.0f}".replace(",", ".")
        items_html += f"""
        <div style="margin: 8px 0; font-size: 12px;">
            <div>{item['name']}</div>
            <div style="display: flex; justify-content: space-between;">
                <span>{item['qty']} Pcs X {price_str}</span>
                <span>{sub_total_str}</span>
            </div>
        </div>
        """
        
    sub_str = f"Rp. {r['subtotal']:,.0f}".replace(",", ".")
    bayar_str = f"Rp. {r['bayar']:,.0f}".replace(",", ".")
    kembali_str = f"Rp. {r['kembali']:,.0f}".replace(",", ".")
    
    # Template HTML Struk Utuh
    receipt_html = f"""
    <div style="max-width: 400px; margin: 0 auto; background: #ffffff; padding: 25px; font-family: 'Courier New', Courier, monospace; color: #000; border-top: 5px solid #03ac0e; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <div style="text-align: center;">
            <h3 style="margin:0; font-family: Arial;">CLOTHES SHOP</h3>
            <p style="font-size: 11px; margin: 2px 0;"><strong>MINIMARKET PAKAIAN & FASHION</strong></p>
            <p style="font-size: 11px; margin: 2px 0;">Jl. Rorojonggrang Raya B1 No.13 - Cimahi</p>
        </div>
        <div style="border-top: 1px dashed #000; margin: 10px 0;"></div>
        <div style="display: flex; justify-content: space-between; font-size: 11px;">
            <span>No. Struk : {r['no_struk']}</span>
            <span>{r['waktu']}</span>
        </div>
        <div style="border-top: 1px dashed #000; margin: 10px 0;"></div>
        {items_html}
        <div style="border-top: 1px dashed #000; margin: 10px 0;"></div>
        <div style="font-size: 13px;">
            <div style="display: flex; justify-content: space-between; font-weight: bold;"><span>Subtotal</span> <span>{sub_str}</span></div>
            <div style="display: flex; justify-content: space-between; font-weight: bold;"><span>Bayar</span> <span>{bayar_str}</span></div>
            <div style="display: flex; justify-content: space-between; font-weight: bold;"><span>Kembali</span> <span>{kembali_str}</span></div>
        </div>
        <div style="border-top: 1px dashed #000; margin: 10px 0;"></div>
        <div style="text-align: center; font-size: 12px; letter-spacing: 2px; margin-top: 15px;">
            <p style="margin:2px 0;">T E R I M A &nbsp; K A S I H</p>
            <p style="margin:2px 0;">ATAS KUNJUNGAN ANDA</p>
        </div>
    </div>
    """
    
    # Menampilkan struk menggunakan komponen HTML Streamlit agar 100% rapi tanpa teks tag bocor
    components.html(receipt_html, height=450, scrolling=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🛍️ Belanja Lagi", use_container_width=True):
            st.session_state.receipt_data = None
            st.session_state.cart = {}
            st.rerun()
    with col_btn2:
        if st.button("🖨️ Cetak Struk Baru", use_container_width=True):
            st.session_state.receipt_data = None
            st.rerun()

else:
    # Layout Utama: Katalog Produk (Kiri) & Keranjang / Kasir (Kanan)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📦 Katalog Produk Pakaian")
        cols = st.columns(3)
        for index, p in enumerate(st.session_state.products):
            with cols[index % 3]:
                price_display = f"Rp {p['price']:,.0f}".replace(",", ".")
                st.markdown(f"""
                <div class="product-card">
                    <div style="font-size:10px; color:#03ac0e; font-weight:bold;">{p['category'].upper()}</div>
                    <div class="product-title">{p['name']}</div>
                    <div class="product-price">{price_display}</div>
                    <div style="font-size:11px; color:#757575; margin-bottom:8px;">Terjual {p['sold']}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"+ Keranjang", key=f"add_{p['id']}"):
                    st.session_state.cart[p['id']] = st.session_state.cart.get(p['id'], 0) + 1
                    st.rerun()

    with col2:
        st.subheader("🛒 Keranjang Belanja")
        if not st.session_state.cart:
            st.info("Keranjang masih kosong. Pilih produk di sebelah kiri.")
        else:
            subtotal = 0
            cart_items = []
            
            for pid, qty in list(st.session_state.cart.items()):
                product = next((item for item in st.session_state.products if item["id"] == pid), None)
                if product:
                    item_total = product["price"] * qty
                    subtotal += item_total
                    cart_items.append({
                        "name": product["name"],
                        "price": product["price"],
                        "qty": qty,
                        "subtotal": item_total
                    })
                    
                    c_col1, c_col2, c_col3 = st.columns([3, 2, 1])
                    with c_col1:
                        st.write(f"**{product['name']}**")
                        p_format = f"Rp {product['price']:,.0f}".replace(",", ".")
                        st.caption(f"{p_format} x {qty}")
                    with c_col2:
                        sub_t_str = f"Rp {item_total:,.0f}".replace(",", ".")
                        st.write(f"**{sub_t_str}**")
                    with c_col3:
                        if st.button("❌", key=f"del_{pid}"):
                            del st.session_state.cart[pid]
                            st.rerun()
            
            st.markdown("---")
            total_str = f"Rp {subtotal:,.0f}".replace(",", ".")
            st.markdown(f"### Total: {total_str}")
            
            # Input Nominal Pembayaran Bebas
            st.markdown("---")
            st.subheader("💳 Pembayaran")
            nominal_bayar = st.number_input("Masukkan Nominal Pembayaran (Rp):", min_value=0, step=10000, value=int(subtotal))
            
            if st.button("Bayar & Cetak Struk", type="primary", use_container_width=True):
                if nominal_bayar < subtotal:
                    st.error(f"Uang pembayaran kurang! Total belanja adalah {total_str}")
                else:
                    kembali = nominal_bayar - subtotal
                    waktu_sekarang = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
                    no_struk = datetime.datetime.now().strftime("%Y%m%d%H%M")
                    
                    st.session_state.receipt_data = {
                        "no_struk": no_struk,
                        "waktu": waktu_sekarang,
                        "items": cart_items,
                        "subtotal": subtotal,
                        "bayar": nominal_bayar,
                        "kembali": kembali
                    }
                    st.rerun()
