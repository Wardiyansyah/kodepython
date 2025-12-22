class A:
    def __init__(self):
        print('A.__init__()')

class B(A):
    def __init__(self):
        super().__init__()

        print('B.__init__()')

def main():
    obj = B()

if __name__ == "__main__":
    main()
