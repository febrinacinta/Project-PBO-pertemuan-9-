from burung import Burung, emprit, ostrich, penguin, elang, burunghantu, itik, merpati

while(True):
    print("=========================Info Burung============================")
    print("1. Emprit")
    print("2. Ostrich")
    print("3. Penguin")
    print("4. Elang")
    print("5. Burung Hantu")
    print("6. Itik")
    print("7. Merpati")
    print("0. Exit")

    ketik = int(input("Masukkan angka burung yang ingin Anda ketahui infonya = "))
    if ketik== 1 :
        emprit().terbang()
        emprit().tipe()
        emprit().habitat()
        emprit().keaktifan()
        emprit().paruh()
        emprit().kaki()
    if ketik== 2 :
        ostrich().terbang()
        ostrich().tipe()
        ostrich().habitat()
        ostrich().keaktifan()
        ostrich().paruh()
        ostrich().kaki()
    if ketik== 3 :
        penguin().terbang()
        penguin().tipe()
        penguin().habitat()
        penguin().keaktifan()
        penguin().paruh()
        penguin().kaki()
    if ketik== 4 :
        elang().terbang()
        elang().tipe()
        elang().habitat()
        elang().keaktifan()
        elang().paruh()
        elang().kaki()
    if ketik== 5 :
        burunghantu().terbang()
        burunghantu().tipe()
        burunghantu().habitat()
        burunghantu().keaktifan()
        burunghantu().paruh()
        burunghantu().kaki()
    if ketik== 6 :
        itik().terbang()
        itik().tipe()
        itik().habitat()
        itik().keaktifan()
        itik().paruh()
        itik().kaki()
    if ketik== 7 :
        merpati().terbang()
        merpati().tipe()
        merpati().habitat()
        merpati().keaktifan()
        merpati().paruh()
        merpati().kaki()

    elif ketik== 0 :
        SystemExit
        print("EXIT")
        break

    else : 
        print("Masukkan angka yang valid")