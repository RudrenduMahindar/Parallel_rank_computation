import logging
import threading

numbers_list = []
threads_list = []
result_list = []
threadLock = threading.Lock()

def read_from_file():
	print("reading numbers from file......")
	f = open('number.txt', 'r') 
  
	# Reading from the file 
	content = f.readlines() 
  
	# Varaible for storing the sum 
	a = 0
	
	# Iterating through the content of the file
	# each line has multiple numbers, take each number from each line 
	for line in content: 
		numbers = line.split()
		for number in numbers: 
			a = int(number)
			numbers_list.append(a)
			print("The current number is:", a) 

	print("all numbers have been read from file......")

	print("printing numbers from list......")
	for i in numbers_list:
		print(i)
	print("numbers have been printed from list......")		

def init_result_list():
	for i in range(len(numbers_list)):
		result_list.append(0)

def start_multithreading():
	for i in range(len(numbers_list)):
		thread = threading.Thread(target=rank_compute, args=(i,))
		threads_list.append(thread)
		thread.start()
	for thread in threads_list:  # iterates over the list of threads
		thread.join()       # waits until the thread has finished work    	



def rank_compute(thread_id):
	#logging.info("thread %s: here", name)
	number_val = numbers_list[thread_id]
	for i in range(len(numbers_list)):
		if numbers_list[i] > number_val:
			threadLock.acquire()
			result_list[i] += 1   # shared list access synchronized
			threadLock.release()			

def show_result_ranks():
	print("Results below......")
	for i in range(len(numbers_list)):
		logging.info("Number %s : Rank %s", numbers_list[i], result_list[i])		


if __name__ == "__main__": 
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
	read_from_file()
	init_result_list()
	print("starting rank computation in multithreading......")
	start_multithreading()
	print("ending rank computation now......")
	print("showing results of rank computation......")
	show_result_ranks()
	print("finished rank_compute, results displayed......")
	print("program ends......")