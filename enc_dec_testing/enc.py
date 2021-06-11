file = open('file.txt','r').read()
key = 'testing_key_123'
chall = ''
for i in range(len(file)):
	chall += chr(ord(file[i])^ord(key[i%len(key)]))
	print(chall)
out = open('file.enc','w').write(chall)
