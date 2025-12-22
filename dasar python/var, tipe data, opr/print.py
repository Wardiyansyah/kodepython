#######################
# Nama file: print.py #
#######################

def main():
	bahasa = 'Python'
	versi = 3
	a = 13
	b = 26
	
	print(bahasa, versi)	#tidak membutuhkan spasi
	print(bahasa + ' ' + str(versi))		#membutuhkan spasi
	print('%s %d' % (bahasa, versi))
	print('{} {}'.format(bahasa, versi))
	print('{0} {1}'.format(bahasa, versi))
	print('%d dan %d' % (a, b))

if __name__ == '__main__':
	main()
