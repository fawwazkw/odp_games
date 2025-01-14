
def a():
    """
    Buatlah fungsi Python yang mengonversi angka menjadi format teks
    bahasa Indonesia untuk angka 1 hingga 1.000

    MASUKAN
    n = 345

    KELUARAN
    Tiga ratus empat puluh lima
    """
    # write the code solution here
    def number_to_text(n):
        angka = {
            0: "",
            1: "Satu",
            2: "Dua",
            3: "Tiga",
            4: "Empat",
            5: "Lima",
            6: "Enam",
            7: "Tujuh",
            8: "Delapan",
            9: "Sembilan",
        }
        belasan = {
            10: "Sepuluh",
            11: "Sebelas",
            12: "Dua belas",
            13: "Tiga belas",
            14: "Empat belas",
            15: "Lima belas",
            16: "Enam belas",
            17: "Tujuh belas",
            18: "Delapan belas",
            19: "Sembilan belas",
        }
        puluhan = {
            20: "Dua puluh",
            30: "Tiga puluh",
            40: "Empat puluh",
            50: "Lima puluh",
            60: "Enam puluh",
            70: "Tujuh puluh",
            80: "Delapan puluh",
            90: "Sembilan puluh",
        }

        def convert_hundreds(n):
            if n == 0:
                return "Nol"
            elif n > 0 and n < 10:
                return angka[n]
            elif n < 20:
                return belasan[n]
            elif n < 100:
                return puluhan[n // 10 * 10] + " " + angka[n % 10]
            else:
                if n // 100 == 1:
                    return "Seratus " + convert_hundreds(n % 100)
                else:
                    return angka[n // 100] + " ratus " + convert_hundreds(n % 100)

        def convert_thousands(n):
            if n < 1000:
                return convert_hundreds(n)
            elif n < 1000000:
                if n // 1000 == 1:
                    return "Seribu " + convert_hundreds(n % 1000)
                else:
                    return convert_hundreds(n // 1000) + " ribu " + convert_hundreds(n % 1000)

        def convert_millions(n):
            if n < 1000000:
                return convert_thousands(n)
            else:
                return convert_hundreds(n // 1000000) + " juta " + convert_thousands(n % 1000000)

        return convert_millions(n).strip()

    n = int(input("Enter a number: "))
    print(number_to_text(n))

    # print("Mohon maaf, permainan A belum tersedia!")