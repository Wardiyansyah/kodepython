########################
# Nama file: while1.py #
########################

import time

def main():
	i = 0
	while i < 5:
		print('i=%d: Python' % i, end = ', ')
		i += 1
		print('Nilai i berubah menjadi %d' % i)
		
		time.sleep(1) # memberi jeda 1 detik

if __name__ == '__main__':
	main()
