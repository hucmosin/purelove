#十六进制转化，shellcode生成器

import sys
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "usage: %s file.xxx\n" % (sys.argv[0],)
		sys.exit(0)

	shellcode = "\""
	ctr = 1
	maxlen = 15 #to create rows
	#read file
	for b in open(sys.argv[1], "rb").read():
		shellcode += "\\x" + b.encode("hex")
		if ctr == maxlen:
			shellcode += "\" \n\""
			ctr = 0
		ctr += 1
	shellcode += "\""
	print "Code length: " + str(len(shellcode))
	#search null bytes
	print "Null byte found: " + str(len([n for n in xrange(len(shellcode)) if shellcode.find('\\x00', n) == n]))
	print
	print shellcode
