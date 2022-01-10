


def sortsquare(array):
    squaresort = [ 0 for _ in range(array)]
    for idx in range(len(array)):
        value = array[idx]
        squaresort[idx] = value * value
    squaresort.sort()
    return sortsquare
array = [1,2,3,6,8,9]
print(sortsquare(array))