def b():
    """
    Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    MASUKAN
    data = [4, 8, 15, 16, 23, 42] 

    KELUARAN
    15 16
    """


    user_input = input("Masukkan daftar angka yang dipisahkan oleh spasi: ")
    

    data = list(map(int, user_input.split()))


    data.sort()


    min_diff = float('inf')
    min_diff_pair = (None, None)


    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]
        if diff < min_diff:
            min_diff = diff
            min_diff_pair = (data[i], data[i + 1])

    # Menampilkan pasangan dengan selisih terkecil
    print("Pasangan angka dengan selisih terkecil:", min_diff_pair[0], min_diff_pair[1])