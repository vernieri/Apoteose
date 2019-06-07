#!/usr/bin/python3
import time
import hashlib

def simpleRandomList():
	controller('00', 0, 0, 0, 0)

def randomList(qt):
	#print(qt)
	controller('A0', qt, 0, 0, 0)


def controller(code, qt, wlist, key, num):
	if(code == '00'):
		a = process(code)
		x = intoNum(a)
		s = intoList(x)
		res = multiList(len(s), s, code)
		
	if(code == 'A0'):	
		a = process(code)
		x = intoNum(a)
		s = intoList(x, qt, 0)
		res = multiList(len(s), s, code)
		
def shaFunc(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()	
def intoNum(stringList):
	sha1 = shaFunc(stringList[0])
	sha2 = shaFunc(stringList[1])

	n15 = 0
	n25 = 0

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

	else:
		print("[-] ERROR 0x01A")

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

	else:
		print("[-] ERRO 0x01B")

	#print("depois:")
	#print(n15)
	bigNum = (int(n15)*int(n25))	
	#bigNum = int(n15)*int(n25)
	#bigString = str(bigNum).replace('2', '0\n')
	#print(bigString)

	return bigNum

def intoList(bigNum, qt, num):
	if num != 0:
		print('Todo')

	else:

		bigString = str(bigNum)
		#print(bigString)
		#print(bigNum)
		#bigString = str(bigNum)
		n = 3
		#print(bigString)
		out = [(bigString[i:i+n]) for i in range(0, len(bigString), n)]
		lenList = len(out)
		print(lenList)
		print(qt)
		if(lenList != qt):
			checkSize(lenList, qt)

		return out

def checkSize(lenList, qt):
	if(lenList < qt):
		missingSize(lenList, qt)
	else:
		overSize(lenList qt)	

def missingSize(lenList, qt):
	print('TODO')
	
def multiList(numList, lista):
	local_num = numList
	local_list = lista
	#print(type(local_num))
	#print(lista[1])
	
	for i in local_list:
		print(i)
		


def procedure():
   time.sleep(2.5)


def process():

	t0 = time.process_time()
	procedure()
	string1 = str(time.process_time() - t0)
	#print(string1)
	#print(shaFunc(string1))
	#print (time.clock() - t0, "seconds process time")


	# measure wall time
	t0 = time.time()
	procedure()
	string2 = str(time.time() - t0)
	#print(string2)
	#print(shaFunc(string2))
	x = intoNum(string1, string2)
	s = intoList(x)
	#print(len(s))
	multiList(len(s), s)

	
	#print('cheguei aqui')


#call()

#By: Vernieri		
