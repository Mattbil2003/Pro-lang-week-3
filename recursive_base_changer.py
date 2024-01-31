import math
def decimal_to_any_base(num, base, sequence=""):
    if num < base:
        return (sequence+str(num))[::-1]
    return decimal_to_any_base(math.floor(num/base),base,sequence+str(num%base))

print(decimal_to_any_base(1260,2))


