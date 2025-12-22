#########################
# Nama file: fungsi9.py #
#########################

import math

# fungsi bagian luar
def luasLingkaran(r):
	
	# fungsi lokal
	def kuadrat(x):
		return x ** 2
		
	# memanggil fungsi lokal dari fungsi bagian luar
	return math.pi * kuadrat(r)
	
def main():
	r = float(input('Masukkan jari-jari lingkaran: '))
	# memanggil fungsi bagian luar
	luas = luasLingkaran(r)
	
	print('Luas lingkaran = %.3f' % luas)
	
if __name__ == '__main__':
	main()
