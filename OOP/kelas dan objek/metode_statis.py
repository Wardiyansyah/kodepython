###############################
# Nama file: metode_statis.py #
###############################

class Segitiga:
	def __init__(self, a, t):
		self.alas = a
		self.tinggi = t
		
	def luas(self):
		return (self.luas * self.tinggi) / 2
	
	def cetakLuas(self):
		print('Luas segitiga = %.2f' % self.luas())
		
	# metode statis
	@staticmethod
	def daftarAtribut():
		return ('alas','tinggi')
		
def main():
	# memanggil metode statis
	print('Daftar atribut dari kelas segitiga: %s' % repr(Segitiga.daftarAtribut()))
	
if __name__ == '__main__':
	main()
