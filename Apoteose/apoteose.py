#!/usr/bin/python3
import time
import hashlib

def simpleRandomList():
	controller('00', 0, 0, 0, 0)

def randomList(qt):
	#print(qt)
	controller('A0', qt, 0, 0, 0)
	
def randomWord(file, qt):
	controller('B0', qt, file, 0, 0)		

def controller(code, qt, file, key, num):
	if(code == '00'):
		a = process(code)
		x = intoNum(a)
		s = intoList(x)
		res = multiList(len(s), s, code, 0)	

		return res

	if(code == 'A0'):	
		a = process(code)
		x = intoNum(a)
		s = intoList(x, qt, 0)
		res = multiList(len(s), s, code, qt)
		return res

	if(code == 'B0'):
		numLines = readFile(file, 1, qt, 0)
		a = process(code)
		x = intoNum(a)
		s = intoList(x, qt, 0)
		lista = multiList(len(s), s, code, 0)
		res = readFile(file, 0, qt, lista)

		return res 
	
def readFile(file, flag, qt, lista):
	plista = []
	print(lista)

	f = str(file)+".txt"
	with open(f) as wordlist:

		if(flag > 0):
			#print(f)
			if (qt > file_len(f)):
				print("[-] ERROR 0x02A\n")
				print("[-] A quantidade passada eh maior que o numero de linhas")
			else:
				numLines = file_len(f)
				return numLines

		else:
			numLines = file_len(f)
			cont = 0
			while cont != numLines:
				plista.append(linecache.getline(f, lista[cont]))
				cont = cont + 1

		return plista		


		#return numLines
		
def file_len(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
		
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


def process(code):

	stringList = []

	t0 = time.process_time()
	procedure()
	string1 = str(time.process_time() - t0)

	t0 = time.time()
	procedure()
	string2 = str(time.time() - t0)

	stringList.append(string1)
	stringList.append(string2)

	#print(stringList)

	return stringList

#By: Vernieri
