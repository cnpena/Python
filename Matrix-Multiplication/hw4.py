import numpy as np
import math
import timeit
import matplotlib.pyplot as plt

#QUESTION 1:
#Brute force algorithm to multiply two matrices
def matmult(my_arr, my_vec):
	arr_len = len(my_arr) #Set array length

	fin_array = np.array([])	#Initialize empty array

	for i in range(arr_len):
		s = 0					#Set sum of row i equal to 0

		for j in range(arr_len):			#Multiply the correct corresponding parts of the matrices and add them to the sum
			s += my_arr[i][j] * my_vec[j]

		fin_array = np.append(fin_array, s)		#Add the sum to the final array

	return fin_array
#--------------------------------------------------------------------
#QUESTION 2
#Generate Hadamard matrix of size 2^k x 2^k
def hadmat(k):

	if k ==1 :					#Base case, return 2x2 Hadamard matrix
		return [[1,1],[1,-1]]

	top = np.concatenate((hadmat(k-1), hadmat(k-1)), axis=1)	#Recursively build top and bottom portions of matrix
	bottom = np.concatenate((hadmat(k-1), np.multiply(hadmat(k-1), -1)), axis=1)

	new = np.concatenate((top, bottom), axis=0)			#Put the top and bottom parts together

	return new
#--------------------------------------------------------------------
#QUESTION4
#Multiply a Hadamard matrix of size 2^k x 2^k and an vector of size 2^k
def hadmatmult(had_arr, my_vec):
	n = len(had_arr)			#Set array length

	if n == 2:			#Base case, return the product of 2x2 Hadamard matrix and the sub array of my_vec
		my_mat = np.array([had_arr[0][0]*my_vec[0] + had_arr[0][1]*my_vec[1], had_arr[1][0]*my_vec[0] + had_arr[1][1]*my_vec[1]])
		return my_mat
   
	matrix = np.empty([n//2,n//2]) #we only need the top left corner of the matrix
	for i in range(0,n//2): #copies half into the new array
		for j in range(0,n//2):
			matrix[i][j] = had_arr[i][j]

	left = hadmatmult(matrix, my_vec[0:n//2])
	right = hadmatmult(matrix, my_vec[n//2:n])

	top = left + right
	bottom = left - right
	new = np.concatenate((top, bottom), axis=0)		#Combine top and bottom parts
	return new
#--------------------------------------------------------------------
#gets the time to compute hadamard matrix multiplication
# def hadmatmulttime():
# 	hadmattime = []
# 	for i in range(1,13):
# 		my_vec = np.random.permutation(2**i)
# 		had_arr = hadmat(i)
# 		t = timeit.Timer(lambda: hadmatmult(had_arr, my_vec))
# 		hadmattime = np.append(hadmattime, t.timeit(number=1))
# 	print(hadmattime)
# 	return hadmattime
#--------------------------------------------------------------------
#gets the time to compute brute force matrix multiplication
# def matmulttime():
# 	print("Getting matmult times...")
# 	matmulttime = []
# 	for i in range(1,13):
# 		my_vec = np.random.permutation(2**i)
# 		had_arr = hadmat(i)
# 		t = timeit.Timer(lambda: matmult(had_arr, my_vec))
# 		matmulttime = np.append(matmulttime, t.timeit(number=1))
# 	print(matmulttime)
# 	return matmulttime
#--------------------------------------------------------------------
#graphs the hadamard matrix multiplication vs the brute force multiplication
# def plottimes():
# 	print("Plotting times")

# 	had_mat_mult = hadmatmulttime() #gets the hadamard matrix multiplication times
# 	mat_mult = matmulttime() #gets the matrix multiplication times

# 	x_coor = [2**x for x in range(1,13)]
# 	plt.plot(x_coor, had_mat_mult, label="Hadmatmult")
# 	plt.plot(x_coor, mat_mult, label="Matmult")
# 	plt.legend()
# 	plt.axis([0,4096,0,12])
# 	plt.ylabel("Running Time (s)")
# 	plt.xlabel("Array size 'n'")
# 	plt.title("Matrix Multiplication vs. Hadamard Matrix Multiplication")
# 	plt.show()

