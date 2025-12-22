class A:
    def __init__(self, a):
        self.__a = a

    def cetakA(self):
        print('Nilai a: %d' % self.__a)

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.__b = b

    def cetakB(self):
        print('Nilai b: %d' % self.__b)

class C(B):
    def __init__(self, a, b,c):
        super().__init__(a, b)
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
