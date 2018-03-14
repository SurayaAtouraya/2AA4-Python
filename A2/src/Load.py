## @file Load.py
# @title Load
# @author Ninos Yomo
# @date 02/23/2018

from CurveADT import *
from Data import *

## @brief Populates the Data object with curves from an input file.
# @details Reads some input file called s and creates curves from the input.
# The curves are then added to the Data abstract object.
# @param s The string name of the input file.
def Load(s):
    
    Data.init()
    file = open(s,'r')

    zVals = []                                  #Dealing with input for curve number and order.
    orderVals = []
    zLine = file.readline()
    orderLine = file.readline()
    zVals = zLine.split(",")
    orderVals = orderLine.split(",")
    for i in range(len(zVals)):
        zVals[i] = zVals[i].strip()
        zVals[i] = zVals[i].strip('\n')
        zVals[i] = float(zVals[i])
        orderVals[i] = orderVals[i].strip()
        orderVals[i] = orderVals[i].strip('\n')
        orderVals[i] = int(orderVals[i])

    xVals = []                                  #Formatting input for xVals and yVals.
    yVals = []
    lines = []
    count = 0
    for line in file:
        lines.append(line.split(','))
        for i in range(len(lines[count])):
            lines[count][i] = lines[count][i].strip()
            lines[count][i] = lines[count][i].strip('\n')
            if lines[count][i] != "":
                lines[count][i] = float(lines[count][i])
        count += 1
    print(lines)
       
    for i in range(len(lines)):                 #Sorting input
        for j in range(0,len(lines[0])-1,2):
                xVals.append(lines[i][j])
                yVals.append(lines[i][j+1])

    xTemp = []                                  #Populating Data
    yTemp = []
    for i in range(0,len(zVals)):
        for j in range(i,len(xVals),len(zVals)):
            if xVals[j] == "":
                break
            xTemp.append(xVals[j])
            yTemp.append(yVals[j])
        curve = CurveT(xTemp,yTemp,orderVals[i])
        Data.add(curve,zVals[i])
        xTemp = []
        yTemp = []
    file.close()
    
