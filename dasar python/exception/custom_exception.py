##################################
# Nama file: custom_exception.py #
##################################

class ZeroOrNegativeEror(RuntimeError):
	def __init__(self, message):
		self.message = message
		
	def printMessage(self):
		print(self.message)
		
def main():
	print('LUAS DAN KELILING LIGKARAN')
	r = float(input('Masukkan jar-jari: '))
	
	try:
		if r <= 0:
			msg = 'Jari-jari tidak boleh bernilai 0 atau negatf'
			raise ZeroOrNegativeEror(msg)
			
	except ZeroOrNegativeEror as e:
		e.printMessage()
		
	else:
		import math
		luas = math.pi * (r ** 2)
		keliling = 2 * math.pi * r
		print('\nLuas = %.3f' % luas)
		print('\nKeliling = %.3f' % keliling)
		
		
	
if __name__ == '__main__':
	main()
