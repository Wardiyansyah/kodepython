#########################
# Nama file: import5.py #
#########################

import constans
import writer

def kali(a, b):
	return a * b
	
def main():
	writer.printA()
	writer.printB()
	print('A x B = %d' % kali(constans.A, constans.B))
	
if __name__ == '__main__':
	main()

