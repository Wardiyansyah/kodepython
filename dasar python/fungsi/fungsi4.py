#########################
# Nama file: fungsi4.py #
#########################

def kali(a, b):
	return a * b
	
def echo(s, n):
	for i in range(n):
		print(s)
		
def main():
	
	# memanggil fungsi kali()
	
	# mengalikan nilai 2 dan 3
	print('Pemanggilan pertama fungsi kali():')
	print('2 x 3 = %d' % kali(2, 3))
	
	# mengalikan nilai 10 dan 20
	print('\nPemanggilan kedua fungsi kali():')
	print('2 x 3 = %d' % kali(10, 20))
	
	# memanggil fungsi echo()
	
	# mencetak teks 'Python' sebanyak 5 kali
	print('\nPemanggilan pertama fungsi echo():')
	echo('Python', 5)
	
	# mencetak teks 'Pemrograman Python' sebanyak 3 kali
	print('\nPemanggilan kedua fungsi echo():')
	echo('Pemrograman Python', 3)


if __name__ == '__main__':
	main()
