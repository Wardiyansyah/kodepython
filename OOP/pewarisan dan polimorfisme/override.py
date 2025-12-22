# kelas induk
class A:
    def __init__(self, a):
        self.__a = a

    def cetakNilai(self):
        print('Nilai a: %d' % self.__a)

# kelas kelas
class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.__b = b

    # memodifikasi metode cetakNilai() milik kelas A
    def cetakNilai(self):
        # memanggil metode cetakNilai() milik kelas A
        super().cetakNilai()

        # aksi tambahan
        print('Nilai b = %d' % self.__b)

def main():
    # membuat objek dari kelas induk
    obj1 = A(100)
    print('memanggil cetakNilai() dari kelas induk')
    obj1.cetakNilai()

    # membuat objek dari kelas anak
    obj2 = B(1000, 2000)
    print('\nMemanggil cetakNilai() dari kelas anak')
    obj2.cetakNilai()

if __name__ == '__main__':
    main()
