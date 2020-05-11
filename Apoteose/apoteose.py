import time
import re
import hashlib

def shaFunc(v1, v2):

    x = int(v1[9:12])**int(v2[9:12])
    y = int(v2[8:11])**int(v1[8:11])
    #print(x)

    string = v1+v2+str(x)+str(y)
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def apoteose():
	values = process()
	hash1 = shaFunc(values[0], values[1])
	hash2 = shaFunc(values[1], values[0])

	#print(hash1, hash2)

	n1 = re.findall(r'\d+', str(hash1))
	n2 = re.findall(r'\d+', str(hash2))

	number = int(n1[0])+int(n2[1])
	return number

def apoteoseList(value):
	lista = []

	i = 0
	while(i < int(value)):
		number = apoteose()
		lista.append(number)
		i = i + 1

	return lista


def procedure():
   time.sleep(0.0005)


def process():

	stringList = []

	t0 = time.process_time()
	procedure()
	value1 = str(time.process_time() - t0)

	t0 = time.time()
	procedure()
	value2 = str(time.time() - t0)

	valuesList = [value1, value2]
	#print(valuesList)

	return valuesList




#By: Vernieri
