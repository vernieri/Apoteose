#!/usr/bin/python3
import time
import hashlib


def call():
	process()

def shaFunc(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()	

def intoNum(s1, s2):
	sha1 = shaFunc(s1)
	sha2 = shaFunc(s2)

	n15 = 0
	str1 = 'a'
	str2 = 'b'
	str3 = 'c'
	str4 = 'd'
	str5 = 'e'
	str6 = 'f'

	#print("Antes:")
	#print(shaFunc(s1))
	#print(shaFunc(s2))
	if sha1.find(str1 or str2 or str3 or str4 or str5 or str6):
		n10 = sha1.replace('a', '4')
		n11 = n10.replace('b', '3')
		n12 = n11.replace('c', '2')
		n13 = n12.replace('d', '5')
		n14 = n13.replace('e', '6')
		n15 = n14.replace('f', '7')


	#print("depois:")
	#print(n15)
	#print(int(n15))

	if sha2.find(str1 or str2 or str3 or str4 or str5 or str6):
		n20 = sha1.replace('a', '4')
		n21 = n20.replace('b', '3')
		n22 = n21.replace('c', '2')
		n23 = n22.replace('d', '5')
		n24 = n23.replace('e', '6')
		n25 = n24.replace('f', '7')


	#print("depois:")
	#print(n15)
	bigNum = (int(n15)*int(n25))	
	#bigNum = int(n15)*int(n25)
	#bigString = str(bigNum).replace('2', '0\n')
	#print(bigString)
	return bigNum

def intoList(bigNum):
	bigString = str(bigNum)
	#print(bigString)
	#print(bigNum)
	#bigString = str(bigNum)
	n = 3
	#print(bigString)
	out = [(bigString[i:i+n]) for i in range(0, len(bigString), n)]

	return out

def multiList(numList, lista):
	local_num = numList
	local_list = lista
	print(type(local_num))
	
	i = 0
	for i in local_num:
		print('oi')
		i=i+1
