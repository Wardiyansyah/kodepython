#######################
# Nama file: paket.py #
#######################

from pkg.m1 import *
from pkg.m2 import *

def main():
	# memanggil fungsi-fungsi di dalam modul m1
	f1()
	f2()
	
	# memanggil fungsi-fungsi di dalam modul m2
	f3()
	f4()
	
if __name__ == '__main__':
	main()
