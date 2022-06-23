class Pegawai:
    def __init__(self, nama, umur, jabatan):
        self.nama = nama 
        self.umur = umur
        self.jabatan = jabatan
    
    def info(self):
        print ("Pegawai %s berusia %s, dengan jabatan %s." %(self.nama, self.umur, self.jabatan)) 

class Gaji:
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan
    
    def total(self):
        return int(self.gaji_bulanan*12)

    def total1(self):
        return int(self.gaji_bulanan/4)

class Tahunan(Gaji):
    def __init__(self, gaji_bulanan, bonus, denda):
        super().__init__(gaji_bulanan)
        self.bonus = bonus
        self.denda = denda
        self.obj_gaji = Gaji (self.gaji_bulanan)

    def hasil(self):
        print("Total gaji tahunan yang didapat : "+ str(self.obj_gaji.total() + self.bonus - self.denda) + ' ' +'rupiah')

class Mingguan(Gaji): 
    def __init__(self, gaji_bulanan):
        super().__init__(gaji_bulanan)
        self.obj_gaji = Gaji (self.gaji_bulanan)

    def hasil(self):
        print("Total gaji mingguan yang didapat: " + str(self.obj_gaji.total1()) + ' ' + 'rupiah')

class Tunjangan:
    def __init__(self, golongan):
        self.golongan = golongan

    def info(self, low = None, high = None):
        if low != None:
            dapat = 1500000
            dapatotal = low + dapat
            print("Mendapat tunjangan sebanyak Rp%i untuk bulan ini" %(dapatotal))

        elif high != None:
            dapat = 3000000
            dapatotal = high + dapat
            print("Mendapat Tunjangan sebanyak Rp%i untuk bulan ini" %(dapatotal))

        else : 
            print("Mohon maaf tidak termasuk golongan yang mendapat tunjangan")
