import datetime
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Kasir Mini - Clothes Shop</title>
    <style>
        * { box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #f4f6f9; margin: 0; padding: 20px; color: #333; }
        .container { max-width: 900px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        @media (max-width: 768px) { .container { grid-template-columns: 1fr; } }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h2 { margin-top: 0; color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        select, input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-size: 14px; }
        button { background: #27ae60; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; font-size: 14px; width: 100%; font-weight: bold; }
        button:hover { background: #219150; }
        .receipt { font-family: 'Courier New', Courier, monospace; background: #fffdf8; padding: 15px; border: 1px dashed #ccc; font-size: 13px; line-height: 1.4; white-space: pre-wrap; }
        .badge { background: #e74c3c; color: white; padding: 3px 8px; border-radius: 3px; font-size: 12px; }
    </style>
</head>
<body>

<div class="container">
    <!-- Panel Input Transaksi -->
    <div class="card">
        <h2>🛍️ Clothes Shop Makassar</h2>
        <div class="form-group">
            <label for="produk">Pilih Produk (Maks 10 Item)</label>
            <select id="produk"></select>
        </div>
        <div class="form-group">
            <label for="qty">Jumlah (Qty)</label>
            <input type="number" id="qty" min="1" value="1">
        </div>
        <button onclick="tambahItem()">+ Tambah ke Keranjang</button>

        <hr style="margin: 20px 0; border: 0; border-top: 1px solid #eee;">

        <div class="form-group">
            <label for="bayar">Uang Tunai (Rp)</label>
            <input type="number" id="bayar" placeholder="Masukkan jumlah uang">
        </div>
        <button onclick="prosesPembayaran()" style="background: #2980b9;">🖨️ Cetak Struk Belanja</button>
    </div>

    <!-- Tampilan Struk / Output -->
    <div class="card">
        <h2>🧾 Struk Transaksi</h2>
        <div id="receipt-output" class="receipt">Silakan tambah barang dan lakukan pembayaran...</div>
    </div>
</div>

<script>
    // Data Katalog Barang (15 Produk)
    const katalog = [
        { nama: "KAOS LENGAN PANJANG", harga: 34500 },
        { nama: "KAOS LENGAN PENDEK", harga: 25000 },
        { nama: "CELANA PANJANG", harga: 56000 },
        { nama: "CELANA PENDEK", harga: 49000 },
        { nama: "ROK PLISKET", harga: 37000 },
        { nama: "ROK KAIN", harga: 35000 },
        { nama: "DALEMAN JILBAB", harga: 12000 },
        { nama: "JILBAB PASANG BERGO", harga: 17000 },
        { nama: "JILBAB SEGIEMPAT", harga: 29000 },
        { nama: "JAKET", harga: 39000 },
        { nama: "HOODIE", harga: 4500 },
        { nama: "KEMEJA", harga: 43000 },
        { nama: "JAS KERJA", harga: 74000 },
        { nama: "TAS SEKOLAH", harga: 134000 },
        { nama: "DASI", harga: 27600 }
    ];

    let keranjang = [];
    let totalBelanja = 0;
    let totalQty = 0;

    // Load Produk ke Dropdown
    const selectProduk = document.getElementById("produk");
    katalog.forEach((item, index) => {
        let opt = document.createElement("option");
        opt.value = index;
        opt.text = `${index + 1}. ${item.nama} - Rp ${item.harga.toLocaleString('id-ID')}`;
        selectProduk.add(opt);
    });

    function tambahItem() {
        if (keranjang.length >= 10) {
            alert("[!] Keranjang sudah penuh (Maksimal 10 jenis barang)!");
            return;
        }

        const idx = selectProduk.value;
        const qty = parseInt(document.getElementById("qty").value);

        if (isNaN(qty) || qty <= 0) {
            alert("[!] Masukkan jumlah Qty yang valid!");
            return;
        }

        const produkPilihan = katalog[idx];
        const subtotal = produkPilihan.harga * qty;

        keranjang.push({
            nama: produkPilihan.nama,
            harga: produkPilihan.harga,
            qty: qty,
            subtotal: subtotal
        });

        totalBelanja += subtotal;
        totalQty += qty;

        alert(`Berhasil menambahkan: ${produkPilihan.nama} (${qty}x)`);
        document.getElementById("qty").value = 1;
    }

    function prosesPembayaran() {
        if (keranjang.length === 0) {
            alert("[!] Keranjang masih kosong!");
            return;
        }

        const bayar = parseInt(document.getElementById("bayar").value);
        if (isNaN(bayar) || bayar < totalBelanja) {
            alert("[!] Uang tunai kurang dari total belanja!");
            return;
        }

        const kembalian = bayar - totalBelanja;

        // Ambil Waktu Lokal WITA
        const now = new Date();
        const hari = String(now.getDate()).padStart(2, '0');
        const bulan = String(now.getMonth() + 1).padStart(2, '0');
        const tahun = String(now.getFullYear()).slice(-2);
        const jam = String(now.getHours()).padStart(2, '0');
        const menit = String(now.getMinutes()).padStart(2, '0');

        // Menyusun Teks Struk
        let struk = "          CLOTHES SHOP         \n";
        struk += "         ~ MURAH DAN BERKAH ~           \n\n";
        struk += "     JL. TAMANGAPA RAYA NO.23 - MAKASSAR    \n";
        struk += "           Hp 083 356 445 980            \n";
        struk += "         BISA DELIVERY LHO...           \n";
        struk += "----------------------------------------\n";
        struk += "TRANS : 002-194709001                   \n";
        struk += `KASIR : 002-KELOMPOK 4      ${hari}.${bulan}.${tahun} [${jam}:${menit}]\n`;
        struk += "----------------------------------------\n";

        keranjang.forEach(item => {
            struk += `${item.nama}\n`;
            struk += `${item.qty.toFixed(2).padStart(6)} X @${item.harga.toString().padStart(7)}   : ${item.subtotal.toString().padStart(10)}\n`;
        });

        struk += "----------------------------------------\n";
        struk += `Item : ${keranjang.length.toString().padEnd(4)} TOTAL    :Rp ${totalBelanja.toString().padStart(10)}\n`;
        struk += `${''.padEnd(21)} TUNAI    :Rp ${bayar.toString().padStart(10)}\n`;
        struk += `Qty  : ${totalQty.toString().padEnd(4)} KEMBALI  :Rp ${kembalian.toString().padStart(10)}\n`;
        struk += "----------------------------------------\n";
        struk += "   == TERIMA KASIH ATAS KUNJUNGAN ANDA ==\n\n";
        struk += "        SELAMAT DATANG KEMBALI         \n";
        struk += " BARANG TELAH DIBELI TIDAK DAPAT DIKEMBALIKAN\n";
        struk += "========================================\n";

        document.getElementById("receipt-output").innerText = struk;

        // Reset transaksi
        keranjang = [];
        totalBelanja = 0;
        totalQty = 0;
    }
</script>

</body>
</html>
