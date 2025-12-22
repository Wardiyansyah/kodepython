############################
# Nama file: kelas_anak.py #
############################

# mendefinisikan kelas induk
class A:
    def __init__(self):
        self.__a = 0

    def setA(self, a):
        self.__a = a

    def getA(self):
        return self.__a

# mendefinisikan kelas anak (B turunan dari A)
class B(A):
    def __init__(self):
        self.__b = 0

    def setB(self, b):
        self.__b = b

    def getB(self):
        return self.__b

def main():
    # membuat objek dari kelas anak
    obj = B()

    # memanggil metode milik kelas induk
    obj.setA(10)
    print('Nilai a: %d' % obj.getA())

    # memanggil metode milik dirinya sendiri
    obj.setB(20)
    print('Nilai b: %d' % obj.getB())

if __name__ == '__main__':
    main()
