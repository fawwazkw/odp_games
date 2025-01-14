
def b():
    """
    Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    MASUKAN
    data = [4, 8, 15, 16, 23, 42] 

    KELUARAN
    15 16
    """

    # Meminta input dari pengguna
    user_input = input("Masukkan daftar angka yang dipisahkan oleh spasi: ")
    
    # Mengubah input string menjadi daftar angka
    data = list(map(int, user_input.split()))

    # Mengurutkan data
    data.sort()

    # Mencari pasangan dengan selisih terkecil
    min_diff_pair = min(zip(data, data[1:]), key=lambda x: x[1] - x[0])

    # Menampilkan pasangan dengan selisih terkecil
    print("Pasangan angka dengan selisih terkecil:", *min_diff_pair)