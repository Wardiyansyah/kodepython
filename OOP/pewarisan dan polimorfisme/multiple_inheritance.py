# kelas induk pertama
class A:
    def __init__(self, a):
        self.__a = a
    
    def cetakA(self):
        print('Nilai a: %d' % self.__a)

# kelas induk kedua
class B():
    def __init__(self, b):
        self.__b = b

    def cetakB(self):
        print('Nilai b: %d' % self.__b)

# kelas anak, turunan dari kelas induk pertama dan kedua
class C(A, B):
    def __init__(self, a, b, c):
        
        A.__init__(self, a)
        B.__init__(self, b)
        
        self.__c = c

    def cetakC(self):
        print('Nilai c: %d' % self.__c)

def main():
    obj = C(1000, 2000, 3000)

    obj.cetakA()
    obj.cetakB()
    obj.cetakC()

if __name__ == "__main__":
    main()
