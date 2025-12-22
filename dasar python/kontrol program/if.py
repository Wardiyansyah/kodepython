####################
# Nama file: if.py #
####################

def main():
	c = input('Masukkan huruf: ')[0].lower()
	
	if c in ['a', 'e', 'i', 'o', 'u']:
		print('%c adalah huruf vokal' % c)

if __name__ == '__main__':
	main()
