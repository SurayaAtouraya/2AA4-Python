## @file CurveADT.py
# @title CurveT
# @author Ninos Yomo
# @date 02/20/2018

from SeqServices import *
from Exceptions import *
from scipy import interpolate

## @brief Creates a curve object.
# @details This class creates a curve object that has two sequences X and Y which holds the X and Y values of the curve respectively, it also stores the order o
# and has a function f which interpolates the value of the curve at a point when passed as an argument to f. Interpolates in a linear and quadratic method based
# on the value of o which determines if the order is linear or quadratic.
class CurveT:
    ## MAX_ORDER the maximum order of a curve.
    MAX_ORDER = 2
    ## DX the constant used to estimate derivatives.
    DX = 0.001
    
    ## @brief Creates a CurveT object.
    # @details The constructor for the CurveT class. Creates a Curve object by setting its parameters such as minx, maxx and order (o). As well as defining the
    # function f to be the interpolation of the X, Y values based on the order of the function.
    # @param X The sequence of x values of the curve.
    # @param Y The sequence of y values of the curve.
    # @param i The order of the curve. 1 is linear and 2 is quadratic.
    def __init__(self, X, Y, i):
        if isAscending(X) == False:
            raise IndepVarNotAscending()
        if len(X) != len(Y):
            raise SeqSizeMismatch()
        if i < 1 or i > 2:
            raise InvalidInterpOrder()
        self.minx = X[0]
        self.maxx = X[len(X)-1]
        self.o = i
        self.f = interpolate.interp1d(X,Y,i)

    ## @brief Returns the minimum value in the sequence X.
    # @return Returns the minimum value in the sequence X.
    def minD(self):
        return self.minx

    ## @brief Returns the maximum value in the sequence X.
    # @return Returns the maximum value in the sequence X.
    def maxD(self):
        return self.maxx

    ## @brief Returns the order value of the curve.
    # @return Returns the order value of the curve.
    def order(self):
        return self.o

    ## @brief Interpolates a value x on the curve.
    # @param x The value x on the curve being interpolated.
    # @return Interpolates the value of the curve at a point x by calling the interpolation function f.
    def eval(self, x):
        if x < self.minx or x > self.maxx:
            raise OutOfDomain()
        return self.f(x)

    ## @brief Estimates the first order derivative at the point x.
    # @details Estimates the first order derivative at the point x by calling the interpolation function f and applying a first order derivative formula.
    # @param x The x value of the point whose derivative is being calculated.
    # @return The estimate first order derivative of the point x on the curve.
    def dfdx(self, x):
        if x < self.minx or x > self.maxx:
            raise OutOfDomain()
        return (self.f(x+CurveT.DX)-self.f(x))/CurveT.DX

    ## @brief Estimates the second order derivative at the point x.
    # @details Estimates the second order derivative at the point x by calling the interpolation function f and applying a second order derivative formula.
    # @param x The x value of the point whose derivative is being calculated.
    # @return The estimate second order derivative of the point x on the curve.
    def d2fdx2(self, x):
        if x < self.minx or x > self.maxx:
            raise OutOfDomain()
        return (self.f(x+2*CurveT.DX)-2*self.f(x+CurveT.DX)+self.f(x))/(CurveT.DX*CurveT.DX)
    
