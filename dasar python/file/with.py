######################
# Nama file: with.py #
######################

def main():
	# membuka file
	with open('data.txt', 'r') as f:
		
		# membaca data dari dalam file
		data = f.read()
		
		# menampilkan isi data ke layar
		print(data)
		
		# menutup file
		f.close()
		
if __name__ == '__main__':
	main()
