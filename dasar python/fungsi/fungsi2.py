#########################
# Nama file: fungsi2.py #
#########################

def kali(a, b):
	return a * b

def main():
	x = 10
	y = 20
	
	#memanggil fungsi kali()
	z = kali(x, y)
	
	print('%d x %d = %d' % (x, y, z))
	
if __name__ == '__main__':
	main()
