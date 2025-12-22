########################
# Nama file: metode.py #
########################

# mendefinisikan kelas Segitiga
class Segitiga:
	def __init__(self, a, t):
		self.alas = a
		self.tinggi = t
		
	# metode untuk menghitung luas
	def luas(self):
		return (self.alas * self.tinggi) / 2
		
def main():
	# membuat objek dari kelas Segitiga
	obj = Segitiga(5, 3)
	
	# memanggil metode luas
	print('Luas = %.2f' % obj.luas())
	
if __name__ == '__main__':
	main()
