

# # subsequnce

# def ValidSequnce(array, sequence):
#     arridx = 0
#     seqidx =0
    
#     while arridx < len[array] and seqidx < len[sequence]:
#         if array[arridx] == sequence[seqidx]:
#             seqidx +=1
#         arridx +=1
#     return seqidx == len(sequence)

# array = [5,1,22,25,6,-1,8,10]
# sequence =[1,6,-1,10]

# print(ValidSequnce(array, sequence))


def ValidSequebce(array, sequence):
    seqidx = 0
    for value in array:
        if seqidx == len(sequence):
            return True
        if sequence[seqidx] == value:
            seqidx += 1
    return seqidx == len(sequence)

array = [5,1,22,25,6,-1,8,10]
sequence =[1,6,-1,10]

print(ValidSequebce( array, sequence))