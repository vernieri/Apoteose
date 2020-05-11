


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
