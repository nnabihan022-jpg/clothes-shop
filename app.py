#include <iostream>
#include <iomanip>
#include <string>
#include <ctime> // Library untuk mengambil waktu sistem

using namespace std;

// Struktur untuk katalog barang toko
struct Produk {
    string nama;
    long harga;
};

// Struktur untuk item yang dibeli (transaksi)
struct ItemBelanja {
    string nama;
    int jumlah;
    long hargaSatuan;
    long subtotal;
};

int main() {
    // Mengambil waktu sistem dan menyesuaikannya dengan WITA (UTC+8)
    time_t now = time(0);
    now += 8 * 3600; // Offset 8 jam agar akurat di zona waktu WITA
    tm *ltm = localtime(&now);

    int tahun = 1900 + ltm->tm_year;
    int bulan = 1 + ltm->tm_mon;
    int hari = ltm->tm_mday;
    int jam = ltm->tm_hour;
    int menit = ltm->tm_min;

    // Daftar Katalog Barang (15 Pilihan Produk Toko Pakaian)
    Produk katalog[15] = {
        {"KAOS LENGAN PANJANG", 34500},                  // 1
        {"KAOS LENGAN PENDEK", 25000},                  // 2
        {"CELANA PANJANG", 56000},                 // 3
        {"CELANA PENDEK", 49000},          // 4
        {"ROK PLISKET", 37000},        // 5
        {"ROK KAIN", 35000},           // 6
        {"DALEMAN JILBAB", 12000},             // 7
        {"JILBAB PASANG BERGO", 17000},              // 8
        {"JILBAB SEGIEMPAT", 29000},    // 9
        {"JAKET", 39000},             // 10
        {"HOODIE", 4500},           // 11
        {"KEMEJA", 43000},        // 12
        {"JAS KERJA", 74000},          // 13
        {"TAS SEKOLAH", 134000},                    // 14
        {"DASI", 27600}            // 15
    };

    ItemBelanja keranjang[10]; // Keranjang maksimal 10 jenis barang belanjaan
    int n = 0; 
    int pilihanMenu, qty;
    char lanjut;
    long totalBelanja = 0;
    long bayar = 0, kembalian = 0;
    int totalQty = 0;

    cout << "========================================\n";
    cout << "      APLIKASI KASIR MINI - TOKO        \n";
    cout << "========================================\n";

    // Proses Memilih Barang dari Katalog
    do {
        if (n >= 10) {
            cout << "\n[!] Keranjang sudah penuh (Maksimal 10 jenis barang)!\n";
            break;
        }

        // Tampilkan Daftar Menu Barang (1 sampai 15)
        cout << "\n--- DAFTAR PRODUK TOKO ---\n";
        for (int i = 0; i < 15; i++) {
            cout << (i + 1) << ". " << katalog[i].nama << " - Rp " << katalog[i].harga << endl;
        }

        cout << "\nPilih nomor barang (1-15) : ";
        cin >> pilihanMenu;

        // Validasi pilihan menu
        if (pilihanMenu < 1 || pilihanMenu > 15) {
            cout << "[!] Pilihan tidak valid (1-15). Silakan coba lagi.\n";
            continue;
        }

        cout << "Masukkan Jumlah (Qty)     : ";
        cin >> qty;

        int indexBarang = pilihanMenu - 1;

        // Masukkan data ke keranjang belanja
        keranjang[n].nama = katalog[indexBarang].nama;
        keranjang[n].jumlah = qty;
        keranjang[n].hargaSatuan = katalog[indexBarang].harga;
        keranjang[n].subtotal = qty * katalog[indexBarang].harga;

        totalBelanja += keranjang[n].subtotal;
        totalQty += qty;
        n++;

        if (n < 10) {
            cout << "Tambah barang lain? (y/n): ";
            cin >> lanjut;
        } else {
            lanjut = 'n';
        }

    } while (lanjut == 'y' || lanjut == 'Y');

    // Input Pembayaran Tunai
    cout << "\n----------------------------------------\n";
    cout << "Total Belanja : Rp " << totalBelanja << endl;
    do {
        cout << "Uang Tunai    : Rp ";
        cin >> bayar;
        if (bayar < totalBelanja) {
            cout << "[!] Uang tunai kurang! Masukkan ulang.\n";
        }
    } while (bayar < totalBelanja);

    kembalian = bayar - totalBelanja;

    // Cetak Struk Belanja dengan Waktu & Tanggal Otomatis WITA
    cout << "\n\n";
    cout << "          CLOTHES SHOP         \n";
    cout << "         ~ MURAH DAN BERKAH ~           \n\n";
    cout << "     JL. TAMANGAPA RAYA NO.23 - MAKASSAR    \n";
    cout << "           Hp 083 356 445 980            \n";
    cout << "         BISA DELIVERY LHO...           \n";
    cout << "----------------------------------------\n";
    cout << "TRANS : 002-194709001                   \n";
    
    // Menampilkan Tanggal dan Jam secara otomatis dengan format dua digit
    cout << "KASIR : 002-KELOMPOK 4      " 
         << (hari < 10 ? "0" : "") << hari << "." 
         << (bulan < 10 ? "0" : "") << bulan << "." 
         << (tahun % 100) << " [" 
         << (jam < 10 ? "0" : "") << jam << ":" 
         << (menit < 10 ? "0" : "") << menit << "]\n";

    cout << "----------------------------------------\n";

    // Perulangan untuk menampilkan daftar barang di struk
    for (int i = 0; i < n; i++) {
        cout << keranjang[i].nama << endl;
        cout << fixed << setprecision(2);
        cout << setw(6) << (float)keranjang[i].jumlah << " X @" 
             << setw(7) << keranjang[i].hargaSatuan 
             << "   : " << right << setw(10) << keranjang[i].subtotal << endl;
    }

    cout << "----------------------------------------\n";
    cout << left << setw(8) << "Item : " << setw(4) << n 
         << setw(9) << "TOTAL" << ":Rp " << right << setw(10) << totalBelanja << endl;
    cout << left << setw(21) << "" 
         << setw(9) << "TUNAI" << ":Rp " << right << setw(10) << bayar << endl;
    cout << left << setw(8) << "Qty  : " << setw(4) << totalQty 
         << setw(9) << "KEMBALI" << ":Rp " << right << setw(10) << kembalian << endl;
    cout << "----------------------------------------\n";
    cout << "   == TERIMA KASIH ATAS KUNJUNGAN ANDA ==--\n\n";
    cout << "        SELAMAT DATANG KEMBALI         \n";
    cout << "       BARANG TELAH DI BELI TIDAK DAPAT DI KEMBALIKAN   \n";
    cout << "========================================\n";

    return 0;
}
