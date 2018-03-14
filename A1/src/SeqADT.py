## @file SeqADT.py
# @title SeqADT
# @author Ninos Yomo
# @date 01/13/2018

## @brief This class represents a sequence.
# @details This class represents a sequence using a list while allowing operations that add, remove and get elements along with other functions.
class SeqT:

    ## @brief Initializes object of class SeqT
    # @details Initializes object of class SeqT with an empty list that the other class methods use.
    def __init__(self):
        self.sequence = []

    ## @brief Adds element to the sequence.
    # @details Adds an element v to a specific index of the sequence i.
    # @param i An integer, the specified index to add the element into the sequence.
    # @param v A real number, the value to be stored in the sequence.
    def add(self, i, v):
        self.sequence.insert(i, v)

    ## @brief Removes element in sequence.
    # @details Removes an element in the sequence with index specified by i.
    # @param i An integer, the specified index to remove the element in the sequence.
    def rm(self, i):
        del self.sequence[i]

    ## @brief Changes element in sequence.
    # @details Changes an element at a specific index i to become the value v.
    # @param i An integer, the specified index to change the element in the sequence.
    # @param v A real number, the value to be stored in the sequence.
    def set(self, i, v):
        self.sequence[i] = v

    ## @brief Returns an element from the sequence.
    # @details Returns a specific element at index i from the sequence.
    # @param i An integer, the specified index to get the element from the sequence.
    # @return Returns the value of the element of index i from the sequence.
    def get(self, i):
        return self.sequence[i]

    ## @brief Returns length of sequence.
    # @details Returns the number of elements that are in the sequence.
    # @return The number of elements in the sequence.
    def size(self):
        return len(self.sequence)

    ## @brief Finds index of element in sequence.
    # @details Finds the specific index of element v in the sequence, where s.get(i) <= v <= s.get(i+1). This is done by truncating the value v. Once truncated, a loop iterates over the list and compares the value of each element and checks if it matches with v. Once matched, the index is returned.
    # @param v A real number, the value to be searched in the sequence.
    # @return The index of the element v in the sequence.
    def indexInSeq(self, v):
        v = int(v)
        for i in range(0,(len(self.sequence) + 1)):
            if self.sequence[i] == v:
                return i
