def insertatbeg(arr,element):
    arr.insert(0,element)
    return arr

def insertatend(arr,element):
    arr.append(element)
    return arr

def insertatpos(arr,element,position):
    arr.insert(position-1,element)
    return arr

def main():
    n=5
    array=[1,2,3,4,5]
    array=insertatbeg(array,6)
    array=insertatend(array,7)
    array=insertatpos(array,8,4)
    print(array)
main()