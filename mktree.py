import binascii
from struct import *
from UserString import MutableString

p = lambda x:pack("<L",x)

db = open("top-1m.csv","rb").readlines()
strings = []


for i in db:
	strings.append(i.split(",")[1].replace("\n",""))

print strings[1]
# FILE format = [node][node][node][node]....
# hash is 4byte hex
# node : [hash][left][right]

stream = []
tree = []

def append(r,node,addr):
	global stream
	root = stream[r] #root
	root_val = root[0]
	node_val = node[0]
	if node_val > root_val:
		if root[2] == 0:
			stream[r][2] = addr
		else:
			append(root[2],node,addr)
	elif node_val < root_val:
		if root[1] == 0:
			stream[r][1] = addr
		else:
			append(root[1],node,addr)
	else:
		return
	

	
addr = 0
idx = 0
flag = 0
for i in strings:
	node = []
	node.append(binascii.crc32(i) & 0xffffffff)
	node.append(0)
	node.append(0)
	stream.append(node)
	append(0,node,addr)
	addr += 1
	idx += 1
	if idx % 10000 == 0:
		print idx / 10000 , "%"



f = open("result","wb")
for i in stream:
	string = p(i[0]) + p(i[1] * 12) + p(i[2] * 12)
	f.write(string)
print "done!"
f.close()
