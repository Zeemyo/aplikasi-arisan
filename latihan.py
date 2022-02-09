import part4

while True:
    try:
        obj = part4.part4("INI EXCEPTION")
        int_angka = int(input("MASUKAN ANGKA BERAPAPUN KUMAHA ANDA : "))
        obj.get_angka(int_angka)
        obj.get_output()
        break
    except:
            print("CIK ATU NU BENER")