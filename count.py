
from collections import Counter
def findrepeat(arr):
    frequency=Counter(arr)
    repeating=[key for key,value in frequency.items() if value>1]
    return repeating
def main():
    arr=[1,1,2,2,2,3,4,4,4,4]
    print("repeating:",findrepeat(arr))
main()