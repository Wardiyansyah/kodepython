#####################
# Nama file: if1.py #
#####################

import sys

def main():
	a = float(input('Masukkan nilai a: '))
	b = float(input('Masukkan nilai b: '))
	
	if b == 0:
		print('Salah: nilai b tidak boleh 0.')
		sys.exit(1)		#menghentikan program
		
	c = a / b
	print('\n{} / {} = {}'.format(a, b, c))
	
if __name__ == '__main__':
	main()
