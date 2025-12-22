#####################################
# Nama file: input-bilsngsn-riil.py #
#####################################

import math

def main():
	print('Menghitung luas lingkaran')
	radius = float(input('Jari-jari\t: '))
	
	luas = math.pi * (radius ** 2)
	
	print('\nLuas = %.2f' % luas)

if __name__ == '__main__':
	main()
