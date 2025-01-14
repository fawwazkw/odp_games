
def c():
    """
    Buat program untuk memeriksa apakah sebuah angka merupakan bilangan Armstrong.
    Bilangan Armstrong adalah angka yang sama dengan jumlah pangkat 𝑛-nya, di mana 𝑛 adalah jumlah digit angka tersebut.

    MASUKAN
    n = 153

    KELUARAN
    153 adalah bilangan Armstrong
    """
    # contoh bilangan armstrong (0, 1, 153, 370, 371, dan 407)

    n = 153
    # rubah angka menjadi string baut hitung jumlah digit
    angka_str = str(n)
    jumlah_digit = len(angka_str)
    # julmah setiap digit yang dipangkatkan dengan jumlah digit
    jumlah = sum(int(digit_angka) ** jumlah_digit for digit_angka in angka_str)
    # meriksa apa jumlah sama dengan input
    if jumlah == n:
        print(f"{n} adalah bilangan Armstrong")
    else:
        print(f"{n} bukan bilangan Armstrong")

    # write the code solution here
    # print("Mohon maaf, permainan C belum tersedia!")
