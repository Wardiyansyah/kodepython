###################################### 
# Nama file: input-bilangan-bulat.py #
######################################

def main():
    print('Menghitung luas persegi panjang')
    panjang = int(input('Panjang\t: '))
    lebar = int(input('Lebar\t: '))

    luas = panjang * lebar

    print('\nLuas = %d' % luas)

if __name__ == '__main__':
    main()

