#######################
# Nama file: write.py #
#######################

def main():
	# membuka file
	f = open('data.txt', 'w')
	
	# menulis data ke dalam file
	f.write('Python\n')
	f.write('C++\n')
	f.write('PHP\n')
	f.write('Ruby\n')
	
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()
