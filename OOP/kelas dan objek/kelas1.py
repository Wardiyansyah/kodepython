########################
# Nama file: kelas1.py #
########################

# mendefinisikan kelas Segitiga
class Segitiga:
	def __init__(self, a, t):
		self.alas = a
		self.tinggi = t
		
def main():
	# membuat objek dari kelas Segitiga
	obj = Segitiga(5, 3)
	
	# menggunakan atribut untuk perhitungan
	luas = (obj.alas * obj.tinggi) / 2
	
	print('Luas = %.2f' % luas)
	
if __name__ == '__main__':
	main()
