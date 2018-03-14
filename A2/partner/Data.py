## @file Data.py
#  @title Data Module
#  @author Lucas Matthew Dutton
#  @date February 6, 2018

from SeqServices import *
from CurveADT import *
from Exceptions import *

class Data:
	# constants
        MAX_SIZE = 10

	# object variables
	S = None
        Z = None

	##@brief Data initializer
	# @details Creates the abstract Data object for holding multiple CurveT objects
        @staticmethod
        def init():
                Data.S = []
		Data.Z = []

	##@brief adds a CurveT object to be stored
	# @param s The CurveT object
	# @param z The independent variable
	# @throws Full The sequence sizes are at maximum capacity
	# @throws IndepVarNotAscending The independent variable is not ascending
        @staticmethod
	def add(s,z):
		# check exceptions
		if len(Data.S) == Data.MAX_SIZE:
			raise Full("Max data size attained")
		if len(Data.Z) > 0 and z <= Data.Z[len(Data.Z)-1]:
			raise IndepVarNotAscending("Independent var not ascending")

		Data.S.append(s)
		Data.Z.append(z)

	##@brief gets the curve specified at index i
	# @param i The index to get the curve from
	# @throws InvalidIndex The index given is not valid
	# @return A CurveT object reference	
        @staticmethod
	def getC(i):
		if i <= 0 or i > len(Data.S):
			raise InvalidIndex("Index given is invalid/out of bounds")
		return Data.S[i]

	##@brief Evaluates the curves closest to the specified z value
	# @details Given z, finds the curves closest to the index at z and interpolate at z
	# @param x The x-coordinate (vertical line) to interpolate on
	# @param z The index closest to the curves of interest
	# @throws OutOfDomain The given index is out of domain
	# @return the y-value after interpolation of two curves
        @staticmethod
	def eval(x,z):
		if not isInBounds(Data.Z,z):
			raise OutOfDomain("Given index is out of domain")
		j = index(Data.Z,z)
		return interpLin(Data.Z[j],Data.S[j].eval(x),Data.Z[j+1],Data.S[j+1].eval(x),z)

	##@brief Slices the collection of curves at the indicated vertical (x-axis) line
	# @param x The vertical line of interest
	# @param i The order of interpolation
	# @return A new CurveADT representing the points of interest on the vertical line
        @staticmethod
	def slice(x,i):
		Y = list(map(lambda self: eval(self,x),Data.S))
		newCurve = CurveT(Data.Z,Y,i)
		return newCurve
