class IndepVarNotAscending(Exception):

    def __init__(self):
        print ("ERROR: Independent variable sequence is not ascending!")

class SeqSizeMismatch(Exception):

    def __init__(self):
        print ("ERROR: Sequences X and Y do not have the same number of values!")

class InvalidInterpOrder(Exception):
    
    def __init__(self):
        print ("ERROR: The order of the curve is not within the range of (1 to 2)")

class OutOfDomain(Exception):
    
    def __init__(self):
        print ("ERROR: The value x is outside the range of the sequences!")

class Full(Exception):

    def __init__(self):
        print ("Cannot add another curve, data is full!")

class InvalidIndex(Exception):

    def __init__(self):
        print ("Index value of curve in Data is invalid!")
