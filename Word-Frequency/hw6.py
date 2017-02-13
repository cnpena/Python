#HW6
#by Christopher Smith: chshsmit and Celine Pena: cnpena
#This program takes in a file of words, cleans it up a bit and 
#inserts each word into a binary tree (sorted lexographically) 

import heapq
#----------------------------------------------
#binary tree class
class BSTree:

	def __init__(self):
		self.root = None

#insert into the binary tree
	def insert(self, key, value):
		newNode = Node(key, value) #new node to be inserted

		parent = None #initially, the parent is None
		node = self.root


		while node != None: #goes through tree and compares it to the existing values to place it
			parent = node

			if newNode.key == node.key: #if the key already exists, adds one to total value
				node.value += 1
				return

			elif newNode.key < node.key: #if its less than the current node, moves left
				node = node.left
			else: #if its greater than, moves right
				node = node.right

		newNode.parent = parent

		if self.root is None: #updates values of parent
			self.root = newNode
		elif newNode.key < parent.key:
			parent.left = newNode
		else:
			parent.right = newNode
#----------------------------------------------
#finds a node in the tree given the key
	def find(self, key):
		node = self.root #start at the root

		while node != None: #travels down the tree
			if node.key == key: #if they match, we found it!
				print("It appears: ", node.value)
				return node
			elif key < node.key: #if key is before the current key, move left
				x = node
				node = node.left
			else: #if key is after the current key, move right
				x = node
				node = node.right

		print("Not Found: ",key) #if it is not found, returns the parent for later use in finding successor
		return x
#----------------------------------------------
#performs an in-order traversal of the tree (uses a helper function)
	def inOrderTraversal(self):
		inOrderTraversalHelper(self.root)
		return
#----------------------------------------------
#finds the successor of a node given the key. If the key is not actually in the tree, returns the successor of the node
	def successor(self, key):
		node = self.find(key) #starts by finding the node within the tree. (if not found, find returns the parent.)

		if node.parent.left == node: #if our node is the left child of its parent
			if node.key > key:
				print(node.key, node.value)
				return node #returns the node itself
			else:
				print(node.parent.key, node.parent.value)
				return node.parent #returns the parent
		elif node.parent.right == node: #if our node is the right child of its parent
			if node.key > key:
				print(node.key,node.value)
				return node #returns the node itself
			else:
				print(node.parent.parent.key, node.parent.parent.value)
				return node.parent.parent #returns the grandparent
		else:
			return successorHelper(node) #makes a call to successorHelper
#----------------------------------------------
#deletes a node from the binary tree given the key
#this function was adapted from the basic example delete function given in 
#Introduction to Algorithms, Third Edition by Cormen, Leiserson, Rivest and Stein (chapter 12.3)

	def delete(self, key):

		node = self.find(key) #first finds the node in the tree

		if node.key != key: #checks to make sure we've actually found it
			print("Node does not exist")
			return False

		if node.left == None: #case 1, node has only right child. 
			transplant(self, node, node.right)
		elif node.right == None: #case 2, node has only left child
			transplant(self, node, node.left)
		else: #case 3, node has 2 children
			y = minimum(node.right) #finds the successor of our node
			if y.parent != node: #if y is not node's left child, replace y as a child of its parent by y's right child
				transplant(self, y, y.right) #and turn node's right child into y's right child.
				y.right = node.right
				y.right.parent = y
			transplant(self, node, y) #if y is node's right child, replace node as a child of its parent by 
			y.left = node.left #y and replace y's left child by node's left child
			y.left.parent = y

#helper function in deletion
def transplant(tree, old, replacement):

	if old.parent == None: #handles case in which 'old' is the root
		tree.root = replacement
	elif old == old.parent.left: #updates old.parent.left if old is a left child
		old.parent.left = replacement
	else:
		old.parent.right = replacement #update old.parent.right if old is a right child
	if replacement != None: #if replacement is non-None, update replacement.parent
		replacement.parent = old.parent
#----------------------------------------------
#Node class
class Node:

#has 5 attributes: key, value, left, right and parent
	def __init__(self, key, value):
		self.key = key 
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
#----------------------------------------------
#helps perform the inOrderTraversal of the binary tree, does so recursively
def inOrderTraversalHelper(node):
	if node != None:
		inOrderTraversalHelper(node.left)
		print(node.key, node.value)
		inOrderTraversalHelper(node.right)
#----------------------------------------------
#helper for building the heap
def buildArray(node, array):
	if node != None:
		buildArray(node.left, array)
		array.append(node.key)
		buildArray(node.right, array)
#----------------------------------------------
def buildheap(node, heap):

	if node != None: #builds heap for Q4
		buildheap(node.left, heap)
		heapq.heappush(heap, (node.value, node.key))
		buildheap(node.right, heap)
#----------------------------------------------
#helper function for the successor
def successorHelper(node):

	if node.right != None: #if our node has a right child
		node = minimum(node.right) #finds the minimum in the right child subtree, this is our sucessor
		print(node.key, node.value)
		return node
	y = node.parent 
	while y != None and node == y.right: #if our node doesn't have a right child, then y is the lowest ancestor of x whose left child is also an ancestor of x
		node = y
		y = y.parent
	print(y.key, y.value)
	return y
#----------------------------------------------
#simply finds the minimum by moving left until it can no longer go left
def minimum(node):
	while node.left != None:
		node = node.left
	return node
#----------------------------------------------
#file processing stuff!

# file_p = open("stopwords.txt", "r") #opens stopwords
# stopwords = set() #puts them into a set

# for line in file_p:
# 	stopwords.add(line.rstrip('\n')) #cleans up the stopwords file, removes the new line

# def processFile(lowTree, highTree):
# 	file_p = open("finefoods_cleaned.txt", "r") #opens up the finefoods file

# 	for line in file_p:

# 		rating = int(line[0]) #rating is the first number of each line
# 		words = line.rstrip('\n').split(" ") #more cleaning up, strips the \n again
# 		if rating < 4: #if the rating is below 4, goes into low rating tree
# 			insert(lowTree, words) #inserts each word
# 		else: #if the rating is 4 or 5, goes into the high rating tree
# 			insert(highTree, words) #inserts each word

# #inserts into the tree
# def insert(tree,line): 
# 	for word in line:
# 		if word in stopwords: #if the word is in stopwords, skips the word
# 			continue
# 		else:
# 			tree.insert(word, 1) #otherwise, insert into tree
	








