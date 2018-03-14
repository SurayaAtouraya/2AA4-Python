## @file Data.py
# @title Data
# @author Ninos Yomo
# @date 02/22/2018

from Exceptions import *
from CurveADT import *
from SeqServices import *

## @brief An abstract object data that stores curves.
# @details An abstract object data that stores curves in a sequence. Along with the curves,
# another sequence stores reals inputted by the user that is associated with its respective curve in
# the other sequence. Up to 10 sequences can be stored.
class Data:

    ## MAX_SIZE the maximum number of curves that the Data object can store
    MAX_SIZE = 10

    ## @brief Initializes the Data abstract object
    # @details Initializes the Data abstract object by creating two sequences that will store the curves and associated real values.
    # @param S The sequence that will store the curve objects.
    # @param Z The sequence that will store the real values associated with a curve.
    @staticmethod
    def init():
        Data.S = []
        Data.Z = []

    ## @brief Adds a curve and real to their respective sequences.
    # @details Adds a curve s to the sequence of curves S and a real z to the sequence of reals z.
    # @param s The curve that will be added to sequence S.
    # @param z The real number that will be added to sequence Z.
    @staticmethod
    def add(s,z):
        if len(Data.S) == Data.MAX_SIZE:
            raise Full()
        if len(Data.Z) > 0 and z <= Data.Z[len(Data.Z)-1]:
            raise IndepVarNotAscending()
        Data.S.append(s)
        Data.Z.append(z)

    ## @brief Returns a curve that was searched for.
    # @details Given an index value i, returns the curve in sequence S at that index if it exisits.
    # @param i The index value of the sequence S that will be referenced.
    # @return The curve at the index i of the sequence S.
    @staticmethod
    def getC(i):
        if i < 0 or i > len(Data.S) or len(Data.S) == 0:
            raise InvalidIndex()
        return Data.S[i]

    ## @brief Estimates the eval(x) at some given z value by interpolating it with the curves
    # beside the z value.
    # @details Takes two consecutive curves in Data.S based on the given z value and evaluates
    # them at a point x, it then performs a linear interpolation using their z values and their
    # evaluated values at x.
    # @param x The point where the curves will be evaluated at.
    # @param z The point where the estimated eval(x) value will be interpolated.
    # @return The estimated eval(x) at z.
    @staticmethod
    def eval(x,z):
        if isInBounds(Data.Z,z) == False:
            raise OutOfDomain()
        return interpLin(Data.Z[index(Data.Z,z)],Data.S[index(Data.Z,z)].eval(x).take(0),Data.Z[index(Data.Z,z)+1],Data.S[index(Data.Z,z)+1].eval(x).take(0),z)

    ## @brief Creates a new curve by evaluating each curve in Data at some point.
    # @details Creates a new curve. First, the independent variable of the new curve is the sequence
    # of z values in Data. The dependent variable will be the curves evaluated at some x value.
    # @param x The point where each curve will be evaluated at.
    # @param i The order of the new curve.
    # @return The new curve.
    @staticmethod
    def slice(x,i):
        __Y__ = []
        for j in range(len(Data.Z)):
            __Y__.append(Data.S[j].eval(x).take(0))
        print(__Y__)
        print(Data.Z)
        return CurveT(Data.Z,__Y__,i)
            

