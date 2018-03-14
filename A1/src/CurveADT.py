## @file CurveADT.py
# @title CurveADT
# @author Ninos Yomo
# @date 01/13/2018

import SeqADT
import numpy

## @brief Holds x and y values in sequence from input file.
# @details This class has two sequences from SeqADT.py that will store data from an input file. Specifically, the input file contains data about some function, once the function is stored, interpolation can be conducted on it as well as regression.
class CurveT:

    ## @brief Constructor for the CurveT class.
    # @details Constructs two sequences, the sequences will store data from an input file s. The input file will contain two columns with data entry seperated by commas. The first column represents x values and the other y values. These will be stored in their respective sequences.
    # @param s A string that holds the name of the input file used.
    def __init__(self, s):

        ## xVals is a field of the object created by class CurveT which is a sequence used to store x points from input file.
        self.xVals = SeqADT.SeqT()
        ## yVals is a field of the object created by class CurveT which is a sequence used to store y points from input file.
        self.yVals = SeqADT.SeqT()

        ## file is a field opens the input file s and is used to extract the data from it.
        file = open(s,"r")

        for i in file:
            ## A field that is used to hold each line of data and split it two corresponding sequences as the loop iterates through the file.
            lineTemp = i.split(",")
            self.xVals.add(self.xVals.size(), int(lineTemp[0]))
            self.yVals.add(self.yVals.size(), int(lineTemp[1]))

        file.close()

    ## @brief Interpolates value x in function using a linear model.
    # @details A value x is to be interpolated in the function that is stored in two sequences. An interpolation formula with a linear model is used and the calculated y value is returned.
    # @param x The x value of the function who's y value is to be interpolated.
    # @return The calculated y value.
    def linVal(self, x):

        for i in range(self.xVals.size()):
            if self.xVals.get(i) > x:
                return (((self.yVals.get(i) - self.yVals.get(i-1))/(self.xVals.get(i) - self.xVals.get(i-1)))*(x - self.xVals.get(i-1)) + self.yVals.get(i-1))

    ## @brief Interpolates value x in function using a quadratic model.
    # @details A value x is to be interpolated in the function that is stored in two sequences. An interpolation formula with a quadratic model is used and the calculated y value is returned.      
    # @param x The x value of the function who's y value is to be interpolated.
    # @return The calculated y value.
    def quadVal(self, x):
        
        for i in range(self.xVals.size()):
            if self.xVals.get(i) > x:
                return (self.yVals.get(i-1) + ((self.yVals.get(i) - self.yVals.get(0))/(self.xVals.get(i) - self.xVals.get(0)))*(x - self.xVals.get(i-1)) + ((self.yVals.get(i) - 2*self.yVals.get(i-1) + self.yVals.get(0))/(2*(self.xVals.get(i)-self.xVals.get(i-1)))**2)*((x - self.xVals.get(i-1))**2))

    ## @brief A function that uses regression to find a y value given an x.
    # @details Uses polyfit from package numpy to regress a function, uses the highest order n and at x value x. This is then mapped using poly1d and the y value is calculated and returned.
    # @param n The highest order of the function, using a very high number will result in errors.
    # @param x The x value whos y value is to be returned.
    # @return The calculated y value.
    def npolyVal(self, n, x):

        ## The bestfit to the function which is found using numpy.polyfit(x,y,n) which is passed our x, y sequences and the rank n.
        bestfit = numpy.polyfit(self.xVals.sequence, self.yVals.sequence, n)
        ## The estimated function, values at x can now be calculated.
        f = numpy.poly1d(bestfit)
        print(f(x))

        
