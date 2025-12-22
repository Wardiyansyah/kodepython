from abc import ABCMeta, abstractmethod
import math

# kelas abstrak
class DuaDimensi(metaclass=ABCMeta):
    # metode abstrak
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

# kelas konkrit, turunan dari kelas DuaDimensi
class PersegiPanjang(DuaDimensi):
    def __init__(self, p, l):
        self.__panjang = p
        self.__lebar = l

    def setPanjang(self, p):
        self.__panjang = p
    
    def getPanjang(self):
        return self.__panjang

    def setLebar(self, l):
        self.__lebar = l
    
    def getLebar(self):
        return self.__lebar

    # implementasi metode luas() milik kelas DuaDimensi 
    def luas(self):
        return self.__panjang * self.__lebar

    # implementasi metode keliling() milik kelas DuaDimensi
    def keliling(self):
        return 2 * (self.__panjang + self.__lebar)

class Lingkaran(DuaDimensi):
    def __init__(self, r):
        self.__radius = r

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def luas(self):
        return math.pi * (self.__radius ** 2)

    def keliling(self):
        return 2 * math.pi * self.__radius

class SegitigaSiku2(DuaDimensi):
    def __init__(self, a, t):
        self.__alas = a
        self.__tinggi = t

    def setAlas(self, a):
        self.__alas = a

    def getAlas(self):
        return self.__alas

    def setTinggi(self, t):
        self.__tinggi = t

    def getTinggi(self):
        return self.__tinggi

    def hipotenusa(self):
        return math.sqrt(
            (self.__alas ** 2) + (self.__tinggi ** 2)
        )

    def luas(self):
        return self.__alas * self.__tinggi / 2

    def keliling(self):
        return self.__alas + self.__tinggi + self.hipotenusa()

# fungsi dengan parameter bersifat polimorfik
def cetakLuasDanKeliling(obj: DuaDimensi, namaObj):
    print('Luas %s = %f' % (namaObj, obj.luas()))
    print('keliling %s = %f' % (namaObj, obj.keliling()))

def main():
    # objek PersegiPanjang
    obj1 = PersegiPanjang(10, 8)

    # fungsi cetakLuasDanKeliling dengan parameter PersegiPanjang
    cetakLuasDanKeliling(obj1, "persegi panjang")

    # objek Lingkaran
    obj2 = Lingkaran(3)
    cetakLuasDanKeliling(obj2, 'lingkaran')

    # objek SegitigaSiku2
    obj3 = SegitigaSiku2(3, 4)
    cetakLuasDanKeliling(obj3, 'segitiga')

if __name__ == "__main__":
    main()
