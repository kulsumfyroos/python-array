def find_symmetric(pairs):
    seen=set(pairs)
    symmetry=set()

    for a,b in pairs:
        if(b,a) in seen:
            symmetry.add((a,b))
    return symmetry
        
input_pairs = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
result=find_symmetric(input_pairs)
print(result)