#########################
# Nama file: fungsi3.py #
#########################

def kali():
	return 10 * 20
	
def echo():
	for i in range(3):
		print('Python')
		
def main():
	# memanggil fungsi kali()
	print('Memanggil fungsi kali():')
	print('10 x 20 = %d' % kali())
	
	# memanggil fungsi echo
	print('\nmemsnggil fungdi echo():')
	echo()
	
if __name__ == '__main__':
	main()
