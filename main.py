from gaji import Pegawai, Tahunan, Mingguan, Tunjangan

a = 1500000
b = 3000000

print("=========================Penggajian Pegawai============================")
x = Pegawai("Mawarti Andriyanti", 35, "Kepala Tim")
x.info()
Tahunan(2500000, 200000, 45000).hasil()
Mingguan(2500000).hasil()
y = Tunjangan(a)
y.info(1500000)
print("========================================================================")
z = Pegawai("Sushilo Andriyanto", 40, "Manager")
z.info()
Tahunan(3500000, 100000, 100000).hasil()
Mingguan(3500000).hasil()
c = Tunjangan(a)
c.info(3000000)