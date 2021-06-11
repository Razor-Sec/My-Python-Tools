import time
file = open('file.enc', 'r').read()
flag = ''
key = 'testing_key_123'
for i in range(len(file)):
	flag += chr(ord(file[i])^ord(key[i%len(key)]))
out = open('fileout.txt', 'w').write(flag)
