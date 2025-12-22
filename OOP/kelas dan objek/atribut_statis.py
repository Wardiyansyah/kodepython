################################
# Nama file: atribut_statis.py #
################################

class Segitiga:
	# atribut statis
	objectCount = 0
	
	def __init__(self, a, t):
		self.alas = a
		self.tinggi = t
		
		# menaikkan nilai atribut statis
		Segitiga.objectCount += 1
		
	def luas(self):
		return (self.alas * self.tinggi) / 2
		
	def cetakLuas(self):
		print('Luas segitiga = %.2f' % self.luas())
		
def main():
	# membuat tiga objek dari keals segitiga
	obj1 = Segitiga(6, 5)
	print('Jumlah objek saat ini: %d' % obj1.objectCount)
	obj2 = Segitiga(5, 4)
	print('Jumlah objek saat ini: %d' % obj2.objectCount)
	obj3 = Segitiga(4, 3)
	print('Jumlah objek saat ini: %d\n' % obj3.objectCount)
	
	# memanggil atribut segitiga.objectCount
	print('Jumlah objek dari kelas segtiga: %d' % Segitiga.objectCount)

if __name__ == '__main__':
	main()
