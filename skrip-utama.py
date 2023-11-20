from luas.segitiga import luas_segitiga
from luas import lingkaran, persegi, segitiga
from volume.kubus import volume_kubus
import volume.bola
from volume.prisma import *

print("luas segitiga :", luas_segitiga(9,6))
print("luas lingkaran :", lingkaran.luas_lingkaran(7))
print("luas persegi :", persegi.luas_persegi(9))
print("volume kubus :", volume_kubus(6))
print("volume bola :", volume.bola.volume_bola(8))
print("volume prisma :", volume_prisma(6,3,5))

# panggil fungsi masing-masing