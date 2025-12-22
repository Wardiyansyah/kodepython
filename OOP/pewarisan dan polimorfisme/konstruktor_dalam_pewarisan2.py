# kelas induk
class A:
    def __init__(self, a):
        print('A.__init__()')
        self.__a = a

    def cetakA(self):
        print('Nilai a: %d' % self.__a)

# kelas anak
class B(A):
    def __init__(self, a, b):
        super().__init__(a)

        print('B.__init__()')
        self.__b = b

    def cetakB(self):
        print('Nilai b: %d' % self.__b)

def main():
    obj = B(100, 200)

    obj.cetakA()
    obj.cetakB()

if __name__ == "__main__":
    main()
