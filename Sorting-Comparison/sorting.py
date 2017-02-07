#Hw2
#Celine Pena : cnpena 
#Christopher Smith : chshsmit
#This program implememt selection sort, insertion sort and merge sort on various arrays.

import numpy as np
import matplotlib.pyplot as plt
import timeit
import scipy

#----------------------------------------------------------
#Selection sort effectively finds the smallest value each iteration and swaps it to the front.
def selectionsort(A):
	n = len(A) #n is the length of the array

	for i in range(0, n): #loops n times
		min = A[i] #value of min is set equal to A[i]
		minInd = i #index set equal to i
		for j in range(i+1, n): #Loop runs for n-1 steps
			if A[j] < min: #checks if the element is less than the mininmum
				min = A[j] #if so, this is the new minimum
				minInd = j 
		A[minInd] = A[i] #Finally when the minimum has been found, swaps the minimum and A[i]
		A[i] = min
	return(A)
#-----------------------------------------------------------
#Insertion sort effectively swaps pairs until the array is sorted.
def insertionsort(A):
	n = len(A) #n is the length of the array

	for i in range(1, n): #loops n-1 times
		j = i 
		while (j>0 and A[j-1] > A[j]): #checks if an element is greater than the one after it.
			temp = A[j] #if so, swaps these elements
			A[j] = A[j-1]
			A[j-1] = temp
			j -= 1
	return(A)
#-----------------------------------------------------------
#merge sort splits the array by half until it is down to 1 element. Then, each element
#is merged back to the array in sorted order
def mergesort(A):

	if len(A) == 1: #if this is an array of 1, already sorted
		return A

	sorted_array=np.array([]) #sorted_array holds the new, sorted array

	if len(A)>1:
		mid = len(A)//2 # divides the array in half
		lefthalf = A[:mid] #left array holds half
		righthalf = A[mid:] #right array holds the other half

		lefthalf = mergesort(lefthalf) #recursions, calls mergesort on both the left and right halves until they're down to a single element
		righthalf = mergesort(righthalf) 

#merging back into a single array
		i=0 #i keeps track of where we are in the left array
		j=0 #j keeps track of where we are in the right array

		while i < len(lefthalf) and j < len(righthalf): #if both the left and right have elements left
			if lefthalf[i] < righthalf[j]: #if the value on the right is larger,
				sorted_array = np.append(sorted_array, lefthalf[i]) #the left is added to the array
				i=i+1 
			else:
				sorted_array = np.append(sorted_array, righthalf[j]) #if the left is larger, the right is added
				j=j+1

		while i < len(lefthalf): #if the right is out of elements
			sorted_array = np.append(sorted_array, lefthalf[i]) #adds from left to the sorted array
			i=i+1

		while j < len(righthalf): #if the left is out of elements
			sorted_array = np.append(sorted_array, righthalf[j]) #adds from right to the sorted array
			j=j+1

	return sorted_array
#-----------------------------------------------------------
#Creates array of times for Selection sort on a sorted array
def sortedSelectionSortTime():
	print("Timing Selection sort on sorted array") #debugging
	selectionSortOnSorted = [] #array that holds the times

	for i in range(100): #calls 100 times
		x = np.arange(1,(i+1)*100,1) #x is the sorted array holding 100 to 10000 elements. .arange makes it sorted
		t = timeit.Timer(lambda: selectionsort(x)) 
		selectionSortOnSorted = np.append(selectionSortOnSorted, t.timeit(number=1)) #adds the time to the time array
	print(selectionSortOnSorted) #debugging, prints the array of times
	return selectionSortOnSorted
#-----------------------------------------------------------
#Creates array of times for Selection sort on a reverse sorted array
def unSortedSelectionSortTime():
	print("Timing Selection sort on reverse sorted array") #debugging
	selectionSortOnUnsorted = [] #array that holds the times

	for i in range(100): #calls 100 times
		x = np.arange((i+1)*100,1,-1) #creates the array reversely sorted from 100 to 10000 elements
		t = timeit.Timer(lambda: selectionsort(x))
		selectionSortOnUnsorted = np.append(selectionSortOnUnsorted, t.timeit(number=1)) #adds the time to the time array
	print(selectionSortOnUnsorted) #debugging, prints the array of times
	return selectionSortOnUnsorted
#-----------------------------------------------------------
#Creates array of times for Selection sort on a random array
def randomSelectionSort():
	print("Timing selection sort on random array") #debugging
	randomSelectionSortTime = [] #array that holds the times

	for i in range(1,101, 5): # calls 20 times
		x = np.random.permutation(i*100) #generates a random array of size 100 to 10000
		t = timeit.Timer(lambda: selectionsort(x))
		randomSelectionSortTime = np.append(randomSelectionSortTime, t.repeat(repeat=50, number = 1)) #adds the time to the time array
	print(randomSelectionSortTime) #debugging, prints the array of times
	return randomSelectionSortTime
#-----------------------------------------------------------
#plots Selection sort for two cases: a completely sorted array and a reverse sorted array
#GRAPH 1 
def selectionSortPlot():
	sorted_time = sortedSelectionSortTime() #gets the time array for a sorted array up to size 10000
	unsorted_time = unSortedSelectionSortTime() #gets the time array for a reverse sorted array up to size 10000

	x_coor = np.arange(100,10001, 100) #creates an array holding 'n', the sizes of the arrays tested- 100 to 10000
	plt.plot(x_coor, sorted_time, 'ro', x_coor, unsorted_time, 'g^') #sorted array time is RED, reverse sorted array time is GREEN
	plt.axis([0,10000,0,16]) #x-axis shows up to 10000, y-axis shows up to 16 seconds
	plt.ylabel("Running Time (s)")
	plt.xlabel("Input Size")
	plt.title("Selection Sort")
	plt.show()
#-----------------------------------------------------------
#Creates array of times for Insertion sort on a sorted array
def sortedInsertionSortTime():
	print("Timing sorted insertion sort") #debugging
	insertionSortOnSorted = [] #array that holds the times
	for i in range(100): #calls 100 times
		x = np.arange(1,(i+1)*100,1) #creates the sorted array holding 100 to 10000 elements
		t = timeit.Timer(lambda: insertionsort(x))
		insertionSortOnSorted = np.append(insertionSortOnSorted, t.timeit(number=1)) #adds the time to the time array
	print(insertionSortOnSorted) #debugging, prints the array of times
	return insertionSortOnSorted
#-----------------------------------------------------------
#Creates array of times for Insertion sort on a reverse sorted array
def unSortedInsertionSortTime():
	print("Timing Insertion sort on a reverse sorted array") #debugging
	insertionSortOnUnsorted = [] #array that holds the times
	for i in range(100): #calls 100 times
		x = np.arange((i+1)*100,1,-1) #creates the array reversely sorted from 100 to 10000 elements
		t = timeit.Timer(lambda: insertionsort(x))
		insertionSortOnUnsorted = np.append(insertionSortOnUnsorted, t.timeit(number=1)) #adds the time to the time array
	print(insertionSortOnUnsorted) #debugging, prints the array of times
	return insertionSortOnUnsorted
#-----------------------------------------------------------
#Creates array of times for Insertion sort on a random array
def randomInsertionSort():
	print("Insertion sort") #debugging
	randomInsertionSortTime = [] #array that holds the times

	for i in range(1,101,5): # calls 20 times because it takes way too long with 100
		tot_time = 0	#sets total time for loop
		for j in range(50):
			x = np.random.permutation(i*100) #creates a random array from size 100 to 10000
			t = timeit.Timer(lambda: insertionsort(x))
			tot_time += t.timeit(number=1) #adds each run to total time
		avg_time = tot_time/50 #sets average time
		randomInsertionSortTime = np.append(randomInsertionSortTime, avg_time) #adds the time to the time array
		print(i) #debugging
	print(randomInsertionSortTime) #debugging, prints the array of times
	return randomInsertionSortTime
#-----------------------------------------------------------
#plots insertion sort for two cases: a completely sorted array and a reverse sorted array
#GRAPH 2
def insertionSortPlot():
	sorted_time = sortedInsertionSortTime() #gets the time array for a sorted array up to size 10000
	unsorted_time = unSortedInsertionSortTime() #gets the time array for a reverse sorted array up to size 10000

	x_coor = np.arange(100,10001, 100) #creates an array holding 'n', the sizes of the arrays tested 100 to 10000
	plt.plot(x_coor, sorted_time, 'ro', x_coor, unsorted_time, 'g^') #sorted array time is RED, reverse sorted array is GREEN
	plt.axis([0,10000,0,50]) #x-axis shows up to 10000, y-axis shows up to 20 seconds
	plt.ylabel("Running Time (s)")
	plt.xlabel("Input Size")
	plt.title("Insertion Sort")
	plt.show()
#-----------------------------------------------------------
#Creates array of times for Mergesort on a sorted array
def sortedMergesortTime():
	print("Timing Sorted Mergesort") #debugging
	mergeSortOnSorted = [] #array that holds the times
	for i in range(100): #calls 100 times
		x = np.arange(1,(i+1)*100,1) #x is the sorted array holding 100 to 10000 elements
		t = timeit.Timer(lambda: mergeSort(x))
		mergeSortOnSorted = np.append(mergeSortOnSorted, t.timeit(number=1)) #adds the time to the time array
	print(mergeSortOnSorted) #debugging, prints the array of times
	return mergeSortOnSorted
#-----------------------------------------------------------
#Creates array of times for Mergesort on a reverse sorted array
def unSortedMergesortTime():
	print("Timing Mergesort on a reverse sorted array") #debugging
	mergeSortOnUnsorted = [] #array that holds the times
	for i in range(100): #calls 100 times
		x = np.arange((i+1)*100,1,-1) #creates the array reversely sorted from 100 to 10000 elements
		t = timeit.Timer(lambda: mergeSort(x))
		mergeSortOnUnsorted = np.append(mergeSortOnUnsorted, t.timeit(number=1)) #adds the time to the time array
	print(mergeSortOnUnsorted) #debugging, prints the array of times
	return mergeSortOnUnsorted
#-----------------------------------------------------------
#Creates array of times for Mergesort on a random array
def randomMergeSort():
	print('Timing mergesort on a random array')
	randomMergeSortTime = [] #array that holds the times

	for i in range(1,101,5): # calls 20 times
		x = np.random.permutation(i*100) # creates random arrays from size 100 to 10000
		t = timeit.Timer(lambda: mergeSort(x))
		randomMergeSortTime = np.append(randomMergeSortTime, scipy.mean(t.repeat(repeat=50, number = 1))) #adds the time to the time array
	print(randomMergeSortTime) #debugging, prints the entire time array
	return randomMergeSortTime
#-----------------------------------------------------------
#plots mergesort for two cases: a completely sorted array and a reverse sorted array
#GRAPH 3
def mergesortPlot():
	sorted_time = sortedMergesortTime() #gets the times for the sorted array case
	unsorted_time = unSortedMergesortTime() #gets the times for the reverse sorted array case

	x_coor = np.arange(100,10001, 100) #x coordinates are 'n' - the sizes of the arrays from 100 to 10000
	plt.plot(x_coor, sorted_time, 'ro', x_coor, unsorted_time, 'g^') #sorted array time is RED, reverse sorted array is GREEN
	plt.axis([0,10000,0,1.8]) #x-axis shows up to 10000, y-axis shows up to 1.8 seconds
	plt.ylabel("Running Time (s)")
	plt.xlabel("Input Size")
	plt.title("Merge Sort")
	plt.show()
#-----------------------------------------------------------
#plots the running times of all three algorithms on a SORTED array
#GRAPH 4
def threeSortedPlot():
	x_coor = np.arange(100,10001,100) #creates an array from 100 to 10000 to hold the x coordinates
	plt.plot(x_coor, sortedMergesortTime(), 'r--', x_coor, sortedInsertionSortTime(), 'bs', x_coor, sortedSelectionSortTime(), 'g^') 
	#merge sort is RED, insertion sort is BLUE, selection sort is GREEN
	plt.ylabel("Running Time (s)")
	plt.xlabel("Input Size")
	plt.title("Selection Sort, Insertion Sort & Merge Sort on sorted arrays")
	plt.axis([0,10000,0,12]) #x-axis goes to 10000, y-axis goes to 12 seconds
	plt.show()
#-----------------------------------------------------------
#plots the running times of all three algorithms on a reverse sorted array
#GRAPH 5
def threeUnsortedPlot():
	x_coor = np.arange(100,10001,100) #creates an array from 100 to 10000 elements to hold the x coordinates
	plt.plot(x_coor, unSortedMergesortTime(), 'r--', x_coor, unSortedInsertionSortTime(), 'bs', x_coor, unSortedSelectionSortTime(), 'g^')
	#mergesort is RED, insertion sort is BLUE, selection sort is GREEN
	plt.ylabel("Running Time (s)")
	plt.xlabel("Input Size")
	plt.title("Selection Sort, Insertion Sort & Merge Sort on reverse sorted arrays")
	plt.axis([0,10000,0,50]) #x-axis goes to 10000, y-axis goes to 50 seconds
	plt.show()
#-----------------------------------------------------------
#plots the running times of all three algorithms on random arrays 
#GRAPH 6
def threeRandomPlot():
	x_coor = np.arange(1,10001,500)
	plt.plot(x_coor, randomMergeSort(), 'r--', x_coor, randomInsertionSort(), 'bs', x_coor, randomSelectionSort(), 'g^')
	plt.ylabel("Running Time (s)")
	plt.xlabel("Input Size")
	plt.title("Average run time for Insertion, Selection and Merge Sort")
	plt.axis([0,10000,0,12])
	plt.show()
#-----------------------------------------------------------	
#tests each algorithm on array of size one million
def million():
	test1 = np.random.permutation(1000000)
	# test2 = np.random.random_integers(1,10000,100000)
	# test3 = np.random.random_integers(1,100000,100000)

	a = timeit.Timer(lambda: insertionsort(test1))
	print("insertion sort took: ")
	print(a.timeit(number = 1))

	#b = timeit.Timer(lambda: selectionsort(test2))
	#print("selection sort took: ")
	#print(b.timeit(number = 1))

	#c = timeit.Timer(lambda: mergeSort(test3))
	#print("merge sort took: ")
	#print(c.timeit(number = 1))

