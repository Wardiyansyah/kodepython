##########################
# Nama file: properti.py #
##########################

class Segitiga:
	def __init__(self, a, t):
		self.alas = a
		self.tinggi = t
		
	# properti luas
	@property
	def luas(self):
		return (self.alas * self.tinggi) / 2
		
def main():
	# membuat objek dari keals Segitiga
	obj = Segitiga(6, 5)
	
	# mengakses properti luas
	print('Luas = %.2f' % obj.luas)
	
if __name__ == '__main__':
	main()
