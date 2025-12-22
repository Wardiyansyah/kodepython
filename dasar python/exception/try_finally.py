#############################
# Nama file: try_finally.py #
#############################

f = None

try:
	f = open('data.txt')
	data = f.read()
	print(data)
finally:
	if f is None:
		f.close()
