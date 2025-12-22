#####################################################
# Nama file program   : absolute.py                 #
# Dibuat oleh         : Iyan                        #
# Tanggal pembuatan   : 19 April 2025               #
# Deskripsi           : program untuk menentukan    #
#						harga mutlak suatu bilangan #
#####################################################

def absval(x):
	# jika x > 0, kembalikan x
	# jika tidak, kembalikan -x
	return x if x > 0 else -x
	
# fungsi utama
def main():
	# meminta user untuk memasukkan bilangan
	val = float(input('Masukkan bilangan: '))
	
	# menampilkan hasil
	print('Harga mutlak dari {} adalah {}'.format(
		  val, absval(val)))
		  
if __name__ == '__main__':
	# memanggil fungsi main()
	main()
