###########################
# Nama file: readline1.py #
###########################

def main():
	# membuka file
	f = open('data.txt', 'r')
	
	# membaca baris pertama
	baris = f.readline()
	
	while baris:
		# menampilkan data
		print(baris, end='')
		
		# membaca baris data berikutnya
		baris = f.readline()
		
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()
		
