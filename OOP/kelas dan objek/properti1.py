###########################
# Nama file: properti1.py #
###########################

class Segitiga:
    def __init__(self, a, t):
        self.__alas = a
        self.__tinggi = t

    @property
    def alas(self):
        return self.__alas

    @alas.setter
    def alas(self, a):
        self.__alas = a
    @property
    def tinggi(self):
        return self.__tinggi

    @tinggi.setter
    def tinggi(self, t):
        self.__tinggi = t

    @property
    def luas(self):
        return (self.alas * self.tinggi) / 2

def main():
    # membuat objek dari kelas Segtiga
    obj = Segitiga(6, 5)

    print('Sebelum diubah:')
    print('Alas = %.2f' % obj.alas)
    print('Tinggi = %.2f' % obj.tinggi)
    print('Luas segitiga = %.2f' % obj.luas)

    # mengubah nila atribut melalui properti
    obj.alas = 8
    obj.tinggi = 6

    print('\nSetelah diubah:')
    print('Alas = %.2f' % obj.alas)
    print('Tinggi = %.2f' % obj.tinggi)
    print('Luas segitiga = %.2f' % obj.luas)

if __name__ == '__main__':
    main()
