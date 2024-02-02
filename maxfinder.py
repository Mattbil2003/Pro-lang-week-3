def max(val1,val2):
    if val1 >= val2:
        return val1
    else:
        return val2
    
def max3(val1,val2,val3):
    return max(val1, max(val2,val3))



val1 = 1
val2 = 4
val3 = 10
print("the max of %d and %d is %d." % (val1,val2,max(val1,val2)))
print("the max of %d,%d, and %d is %d." % (val1,val2,val3,max3(val1,val2,val3)))
print("end of program!")
