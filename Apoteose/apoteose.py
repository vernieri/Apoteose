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
	#print(sha1)
	#print(sha2)

	n15 = 0 #i'm getting some errors, dats why i'm initializing these vars.
	n25 = 0 #var2

	str1 = 'a'
	str2 = 'b'
	str3 = 'c'
	str4 = 'd'
	str5 = 'e'
	str6 = 'f'

	if sha1.find(str1 or str2 or str3 or str4 or str5 or str6):
		n10 = sha1.replace('a', '4')
		n11 = n10.replace('b', '5')
		n12 = n11.replace('c', '1')
		n13 = n12.replace('d', '3')
		n14 = n13.replace('e', '6')
		n15 = n14.replace('f', '8')

	else:
		print("[-] ERROR 0x01A")
		exit()


	if sha2.find(str1 or str2 or str3 or str4 or str5 or str6):
		n20 = sha1.replace('a', '2')
		n21 = n20.replace('b', '4')
		n22 = n21.replace('c', '7')
		n23 = n22.replace('d', '9')
		n24 = n23.replace('e', '0')
		n25 = n24.replace('f', '6')

	else:
		print("[-] ERRO 0x01B")
		exit()

	bigNum = (int(n15)*int(n25))	

	return bigNum

def intoList(bigNum, qt, num):
	if num != 0:
		print('Todo, num')

	else:

		bigString = str(bigNum)
		n = 3
		out = toStringList(bigString)
		lenList = len(out)

		while (lenList < qt):
			check = checkSize(lenList, qt)
			#print(qt, check)
			if(qt == check):
				flag = 0

			else: 
				flag = 1	

			local_list = addSize(flag, bigNum, qt, lenList)
			out = local_list[0]
			lenList = local_list[1]
			bigNum = local_list[2]

		return out

def toStringList(bigString):
	n = 3
	out = [(bigString[i:i+n]) for i in range(0, len(bigString), n)]
	return out	

def checkSize(lenList, qt):

	if(lenList < qt):

		x = (qt - lenList)
		return x
		
	else:
		return qt	

def addSize(flag, bigNum, qt, lenList):
	lista = []
	if(flag == 0):
		
		bigString = str(bigNum)
		out = toStringList(bigString)
		lista.append(out)
		lista.append(lenList)
		lista.append(bigNum)
		return lista


	else:	
		
		newNum = ((bigNum * bigNum) * (bigNum * bigNum)) * bigNum
		bigString = str(newNum)
		out = toStringList(bigString)
		lenList = len(out)
		lista.append(out)
		lista.append(lenList)
		lista.append(newNum)
		return lista
	

def multiList(numList, lista, code, qt):
	local_num = numList
	local_list = lista
	local_qt = qt
	cont = 0
	listao = []
	
	for i in local_list:
		x = int(i)+int(i)
		#print(x)
		listao.append(x)
		cont = cont + 1
		if(cont == local_qt):
			break

	return listao



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

	return stringList


#By: Vernieri
