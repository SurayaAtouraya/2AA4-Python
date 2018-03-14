## @file CurveADT.py
#  @title Curve ADT Module
#  @author Lucas Matthew Dutton
#  @date February 6, 2018

from SeqServices import *
from Exceptions import *

##@brief an ADT representing curves
class CurveT:
	# constants
	MAX_ORDER = 2
	DX = 1 * 10**-3

	##@brief Curve constructor
	# @details Initializes a curve with X and Y values with interpolation order i
	# @param X The sequence of x values
	# @param Y The corresponding sequence of y values
	# @param i The order of interpolation
	# @throws IndepVarNotAscending Independent sequence of values not ascending
	# @throws SeqSizeMismatch Sequences have different length
	# @throws InvalidInterpOrder Order of interpolation is invalid
	def __init__(self,X,Y,i):
		if not isAscending(X):
			raise IndepVarNotAscending("Independent x value is not ascending")
		if not len(X) == len(Y):
			raise SeqSizeMismatch("Mismatched sequence size")
		if i != 1 and i != CurveT.MAX_ORDER:
			raise InvalidInterpOrder("Invalid interpolation order") 
		self.minx = X[0]
		self.maxx = X[len(X)-1]
		self.o = i
		self.f = lambda v: interp(X,Y,self.o,v)

	##@brief Gets the first point from the left
	# @return The first x-coordinate from the left
	def minD(self):
		return self.minx

	##@brief Gets the furthest point from the left
	# @return The furthest x-coordinatae from the left
	def maxD(self):
		return self.maxx

	##@brief Gets the order of interpolation
	# @return The order of interpolation
	def order(self):
		return self.o

	##@brief Evaluates the point of interest
	# @details Using interpolation, find the y-coordinate of the point given x-coordinate
	# @param x The x-coordinate of the point of interest
	# @throws OutOfDomain The domain to evaluate on is out of bounds
	# @return The y-coordinate of the point of interest
	def eval(self,x):
		if not (self.minx <= x and x <= self.maxx):
			raise OutOfDomain("Out of domain bounds")
		return self.f(x)

	##@brief Evaluates the slope at a given point
	# @details Using the first derivative, evaluates the slope for a given x-coordinate
	# @return The slope of the given point
	# @throws OutOfDomain The domain to evaluate on is out of bounds
	def dfdx(self,x):
		if not (self.minx <= x and x <= self.maxx):
			raise OutOfDomain("Out of domain bounds")
		return (self.eval(x+CurveT.DX) - self.eval(x)) / CurveT.DX

	##@brief Evaluates the second derivative
	# @return The second derivative of the given point
	# @throws OutOfDomain The domain to evaluate on is out of bounds
	def d2fdx2(self,x):
		if not (self.minx <= x and x <= self.maxx):
			raise OutOfDomain("Out of domain bounds")
		return (self.eval(x+2*CurveT.DX)-2*self.eval(x+CurveT.DX)+self.eval(x)) / CurveT.DX**2

##@brief An interpolation helper function
# @details Given order of interpolation and a x-coordinate, interpolate to find the y-coordinate
# @param X The sequence of x-values
# @param Y The sequence of y-values
# @param o The order of interpolation
# @param v The x-coordinate of the point of interest
def interp(X,Y,o,v):
	i = index(X,v)
	if o == 1:
		return interpLin(X[i],Y[i],X[i+1],Y[i+1],v)
	else:
		return interpQuad(X[i-1],Y[i-1],X[i],Y[i],X[i+1],Y[i+1],v)


