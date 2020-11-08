

def read_from_file():
	print("reading numbers from file")
	f = open('number.txt', 'r') 
  
	# Reading from the file 
	content = f.readlines() 
  
	# Varaible for storing the sum 
	a = 0
	numbers_list = []
	# Iterating through the content of the file
	# each line has multiple numbers, take each number from each line 
	for line in content: 
		numbers = line.split()
		for number in numbers: 
			a = int(number)
			numbers_list.append(a)
			print("The number is:", a) 

	print("numbers have been read from file")

	print("numbers from list")
	for i in numbers_list:
		print(i)


def rank_compute():
	print("starting rank computation in multithreading")



if __name__ == "__main__": 
	read_from_file()
	rank_compute()