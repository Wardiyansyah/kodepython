#########################
# Nama file: metode1.py #
#########################

# mendefinisikan kelas Segitiga
class Segitiga:
	def __init__(self, a, t):
		self.alas = a
		self.tinggi = t
		
	# metode untuk menghitung luas
	def luas(self):
		return (self.alas * self.tinggi) / 2
		
	# metode untuk mencetak luas
	def cetakLuas(self):
		print('Luas = %.2f' % self.luas())
		
def main():
	# membuat objek dari kelas Segitiga
	obj = Segitiga(5, 3)
	
	# memanggil metode cetakLuas()
	obj.cetakLuas()
	
	
if __name__ == '__main__':
	main()
