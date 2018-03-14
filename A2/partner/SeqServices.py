## @file SeqServices.py
#  @title Sequence Services Module
#  @author Lucas Matthew Dutton
#  @date February 5, 2018

	##@brief Checks if the sequence is not descending, left to right
	# @param X the sequence to check
	# @return Returns true if the sequence is not descending, false otherwise
def isAscending(X):
	for i in range(len(X)-1):
		if X[i] > X[i+1]:
			return False
	return True

	##@brief Checks if a number is within the range of the sequence
	# @param X the sequence to check
	# @param x the number to check
	# @return Returns true if x is within X, false otherwise
def isInBounds(X,x):
	if X[0] <= x and x <= X[len(X)-1]:
		return True
	return False

	##@brief Given x1,x2,y1,y2 and x, returns y using linear interpolation
	# @param x1 x value of first interpolation point
	# @param y1 y value of first interpolation point
	# @param x2 x value of second interpolation point
	# @param y2 y value of second interpolation point
	# @param x the x value of the point of interest
	# @return y the result of y after interpolation
def interpLin(x1,y1,x2,y2,x):
	return ((y2-y1)/(x2-x1))*(x-x1) + y1

	##@brief Given x0,y0,x1,x2,y1,y2 and x, returns y using quadratic interpolation
	# @param x0 x value of first interpolation point
	# @param y0 y value of first interpolation point
	# @param x1 x value of second interpolation point
	# @param y1 y value of second interpolation point
	# @param x2 x value of third interpolation point
	# @param y2 x value of thid interpolation point
	# @param x the x value of the point of interest
	# @return y the result of y after interpolation
def interpQuad(x0,y0,x1,y1,x2,y2,x):
	return y1 + ((y2-y0)/(x2-x0))*(x-x1) + \
	       ((y2-2*y1+y0)/(2*(x2-x1)**2))*(x-x1)**2

	## @brief Given a number, returns the floor index of the number in the sequence
	#  @param X the sequence 
	#  @param x the number to check in the sequence
	#  @return Returns the index where v is compared between two elements.
def index(X,x):
	for i in range(len(X) - 1):
		if (X[i] <= x) and (x <= X[i+1]):
			return i
