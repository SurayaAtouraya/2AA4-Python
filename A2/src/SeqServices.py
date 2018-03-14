## @file SeqServices.py
# @title SeqServices
# @author Ninos Yomo
# @date 02/20/2018

## @brief Checks if a sequence is in ascending order.
# @details Takes a sequence X, and determines whether or not the sequence is in ascending order by checking if any element is less than its previous.
# @param X A sequence whose ascending property will be verified.
# @return Returns the boolean value of the ascending property of the sequence.
def isAscending(X):
    for i in range(len(X)-1):
        if X[i+1] < X[i]:
            return False
    return True

## @brief Checks if a value is bounded in a sequence.
# @details Checks if a value x is found to be in the sequence X by seeing if it is within the bound values, such that it x >= X[0] & x <= X[len(X)-1]
# @param X The sequence being examined.
# @param x The value being checked for in the sequence boundaries.
# @return Returns the boolean that says if the value is bounded in the sequence or not.
def isInBounds(X, x):
    if x < X[0] or x > X[len(X)-1]:
        return False
    return True

## @brief Estimates the value of y in some point (x,y) of a line.
# @details Estimates the value of y at point x by using point (x1,y1) which is before (x,y) and (x2,y2) which is after (x,y), for some line.
# @param x1 The x-value of the point before (x,y).
# @param y1 The y-value of the point before (x,y).
# @param x2 The x-value of the point after (x,y).
# @param y2 The y-value of the point after (x,y).
# @param x The x-value of the point (x,y).
# @return Returns the estimated value of y in the point (x,y).
def interpLin(x1, y1, x2, y2, x):
    return ((y2 - y1)/(x2 - x1))*(x - x1) 

## @brief Estimates the value of y in some point (x,y) of a quadratic.
# @details Estimates the value of y at point x by using points (x0,y0) and (x1,y1) which are before (x,y) and (x2,y2) which is after (x,y), for some line.
# @param x0 The x-value of the point (x0,y0) before (x,y).
# @param y0 The y-value of the point (x0,y0) before (x,y).
# @param x1 The x-value of the point (x1,y1) before (x,y).
# @param y1 The y-value of the point (x1,y1) before (x,y).
# @param x2 The x-value of the point (x2,y2) after (x,y).
# @param y2 The y-value of the point (x2,y2) after (x,y).
# @param x The x-value of the point (x,y).
# @return Returns the estimated value of y in the point (x,y).
def interpQuad(x0, y0, x1, y1, x2, y2, x):
    return y1 + ((y2 - y0)/(x2 - x0))*(x - x1) + ((y2 - 2*y1 + y0)/(2*((x2 -x1)**2)))*(x - x1)**2

## @brief Searches index of a value in a sequence.
# @details Takes a value x and searches its index in the sequence X.
# @params X The sequence being searched on.
# @params x The value being searched in the sequence.
# @return Returns the index i of the value x in the sequence X. Or, if the function was called with a value not bounded, tells the user the value was not found.
def index(X, x):
    for i in range(len(X)):
        if X[0] > x:
            print("Element Not Found! " + str(x) + " is not bounded in the list!" )
            break
        if i == len(X)-1 and X[i] >= x:
            return i
        elif i == len(X)-1 and X[i] < x:
            print("Element Not Found! " + str(x) + " is not bounded in the list!" )
            break
        if X[i] <= x and X[i+1] > x:
            return i
