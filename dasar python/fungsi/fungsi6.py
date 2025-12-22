#########################
# Nama file: fungsi6.py #
#########################

# variabel global
g = 10

def f1():
	print('Nilai variabel g di dalam fungsi f1(): %d' % g)
	
def f2():
	print('Nilai variabel g di dalam fungsi f2(): %d' % g)

def main():
	# memanggil fungsi f1() dan f2()
	f1()
	f2()
	
if __name__ == '__main__':
	main()
