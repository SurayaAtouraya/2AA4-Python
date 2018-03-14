import SeqADT
import CurveADT

print("Testing file SeqADT")                                                                                    #SeqADT object creation test
print("Creating object 'test' from class 'SeqT'...")
test = SeqADT.SeqT()
print("Expecting empty sequence to print:")
if len(test.sequence) != 0:
    print("FAIL!")
else:
    print(test.sequence)
    print("PASS")
    
print("")

print("Testing method 'add' from class 'SeqT'")                                                                 #Testing add method from SeqT     
print("Using proper argument (adding '0' at index 0)...")
test.add(0,0)
print("Expecting '[0]' to print:")
if len(test.sequence) != 1:
    print("FAIL")
else:
    print(test.sequence)
    print("PASS")
    
print("Using inproper argument (adding '-1' at index -1)...")
test.add(-1,-1)
print("Expecting '[-1, 0]' to print:")
if test.sequence[0] != -1:
    print("FAIL")
else:
    print(test.sequence)
    print("PASS")

print("Using proper argument (adding '10' in the middle of the sequence using index '1')")
test.add(1,10)
print("Expecting '[-1, 10, 0]' to print:")
if test.sequence[1] != 10:
    print("FAIL")
else:
    print(test.sequence)
    print("PASS")

print("")

print("Testing method 'rm' from class 'SeqT'")                                                                  #Testing rm method from SeqT  
print("Using proper argument (removing '-1' at index 0)...")
test.rm(0)
print("Expecting '[10, 0]' to print:")
if test.sequence[0] != 10:
    print("FAIL")
else:
    print(test.sequence)
    print("PASS")
    
print("Using inproper argument (removing non-existent element at index 100)...")
print("Error expected (since index out of bounds):")
try:
    test.rm(100)
    print("FAIL, should have caught error!")
except:
    print("Error caught! Sequence unchanged.")
    print("PASS")
    
print("")

print("Testing method 'set' from class 'SeqT' using sequence '[1,2,3]'")                                        #Testing set method from SeqT  
test.rm(0)
test.rm(0)
test.add(0,3)
test.add(0,2)
test.add(0,1)
print("Using proper argument (setting value at 0 to go from 1 to 0)...")
test.set(0,0)
print("Expecting '[0,2,3]' to print:")
if test.sequence[0] != 0:
    print("FAIL")
else:
    print(test.sequence)
    print("PASS")
    
print("Using inproper argument (setting non-existent element at index 100 to 0)...")
print("Error Expected:")
try:
    test.set(100,0)
    print("FAIL, should have caught error!")
except:
    print("Error caught! Sequence unchanged.")
    print("PASS")
    
print("")

print("Testing method 'get' from class 'SeqT' using sequence '[0,2,3]'")                                        #Testing get method from SeqT
print("Using proper argument (getting value at 0)...")
print("Expecting '0' to print:")
if test.get(0) != 0:
    print("FAIL")
else:
    print(test.get(0))
    print("PASS")
print("Using inproper argument (getting value at 100)...")
print("Error Expected:")
try:
    test.get(100)
    print("FAIL, should have caught error!")
except:
    print("Error caught! Sequence unchanged.")
    print("PASS")
    
print("")
    
print("Testing method 'size' from class 'SeqT' using sequence '[0,2,3]'")                                       #Testing size method from SeqT
print("Expecting '3' to print:")
if test.size() != 3:
    print("FAIL")
else:
    print(test.size())
    print("PASS")
    
print("")

print("Testing method 'indexInSeq' from class 'SeqT' using sequence '[0,2,3]'")                                 #Testing indexInSeq method from SeqT
print("Using proper argument (searching exact value 0)...")
print("Expecting '0' to print:")
if test.indexInSeq(0) != 0:
    print("FAIL")
else:
    print(test.indexInSeq(0))
    print("PASS")
print("Using odd argument (searching inner value 2.5)...")
print("Expecting '1' to print:")
if test.indexInSeq(2.5) != 1:
    print("FAIL")
else:
    print(test.indexInSeq(2.5))
    print("PASS")
print("Using inproper argument (searching nonexistent value 100)...")
print("Error Expected:")
try:
    print(test.indexInSeq(100))
    print("FAIL, error not caught!")
except:
    print("Error caught! Sequence unchanged.")
    print("PASS")
    
print("")

print("________________________________________________________")

print("")

print("Testing file CurveADT")                                                                                  #Testing file CurveADT
print("Creating object 'test' with input file 'input.txt' of x^2 from 0 to 5...")
try:
    test = CurveADT.CurveT("input.txt")
    print("PASS")
except:
    test = CurveADT.CurveT("src/input.txt")
print("Expecting object 'test' to contain two sequences of the x and y vals:")
try:
    print(test.xVals.sequence)
    print(test.yVals.sequence)
    print("PASS")
except:
    print("FAIL")
print("Attempting to create object 'test2' with non-existent file...")
print("Error expected:")
try:
    test2 = CurveADT.CurveT()
    print("FAIL")
except:
    print("Error caught!")
    print("PASS")
    
print("")

print("Testing method 'linVal' from class 'CurveT' using 'input.txt'")
print("Using proper argument (interpolating 2.5)...")
print("Expecting roughly 6.25:")
if test.linVal(2.5) < 6.25*0.9 or test.linVal(2.5) > 6.25 * 1.1:
    print("FAIL")
else:
    print(test.linVal(2.5))
    print("PASS")
    
print("Using boundary case (left side data point 0)...")
print("Expecting 0:")
if test.linVal(0) != 0:
    print("FAIL")
else:
    print(test.linVal(0))
    print("PASS")
    
print("Using boundary case (right side data point 5)...")
print("Expecting erratic behaviour:")
if test.linVal(5) != None:
    print("FAIL")
else:
    print(test.linVal(5))
    print("PASS")
    
print("")

print("Testing method 'quadVal' from class 'CurveT' using 'input.txt'")
print("Using proper argument (interpolating 2.5)...")
print("Expecting roughly 6.25:")
if test.quadVal(2.5) < 6.25*.9 or test.quadVal(2.5) > 6.25*1.1:
    print("FAIL")
else:
    print(test.quadVal(2.5))
    print("PASS")
print("Using boundary case (left side data point 0)...")
print("Expecting 0:")
if test.quadVal(0) != 0.0:
    print("FAIL")
else:
    print(test.quadVal(0))
    print("PASS")
print("Using boundary case (right side data point 5)...")
print("Expecting erratic behaviour:")
if test.quadVal(5) != None:
    print("FAIL")
else:
    print(test.quadVal(5))
    print("PASS")

print("")

print("Testing method 'npolyVal' from class 'CurveT' using 'input.txt'")
print("Using proper arguments (interpolating 2.5 with proper rank of 2)...")
print("Expecting roughly 6.25:")
try:
    test.npolyVal(2,2.5)
    print("PASS")
except:
    print("FAIL")
print("Using inproper arguments (interpolating 2.5 with inproper rank of 100)...")
print("Expecting roughly 6.25 with error:")
try:
    test.npolyVal(100,2.5)
    print("PASS")
except:
    print("FAIL")
print("Using absurd arguments (interpolating 100 with inproper rank of 100)...")
print("Expecting wild result:")
try:
    test.npolyVal(100,100)
    print("PASS")
except:
    print("FAIL")









