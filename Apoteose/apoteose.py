import time
import re
import hashlib

def shaFunc(v1, v2):

    x = int(v1[9:12])**int(v2[9:12])
    y = int(v2[8:11])**int(v1[8:11])
    #print(x)

    string = v1+v2+str(x)+str(y)
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


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
