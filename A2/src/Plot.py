## @file Plot.py
# @title Plot
# @author Ninos Yomo
# @date 02/21/2018

from CurveADT import *
import matplotlib.pyplot as plt

## @brief Plots two sequences.
# @details Plots two sequences with the first argument as the independent
# variable and the second argument as the dependent variable.
# @param X The independent sequence.
# @param Y The dependent sequence.
def PlotSeq(X,Y):
    if len(X) != len(Y):
        raise SeqSizeMismatch()
    plt.plot(X,Y)
    plt.show()

## @brief Plots a curve.
# @details Given a curve c, this function plots it while considering how
# many evenly spaced points n to plot.
# @param c The curve being plotted.
# @param n The number of equally spaced points to plot.
def PlotCurve(c,n):
    plotPointsX = []
    plotPointsY = []
    plotPointsY.append(c.f(c.minD()).take(0))
    spacing = (c.maxx - c.minx)/n
    plotPointsX.append(c.minD() + spacing)
    for i in range(1,n-1):
        plotPointsX.append(plotPointsX[i-1] + spacing)
        plotPointsY.append(c.f(plotPointsX[i]).take(0))
    plt.plot(plotPointsX,plotPointsY)
    plt.show()
