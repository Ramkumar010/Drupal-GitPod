def is_you_are_good(array,yours_average):
    total=0
    x=len(array)
    for i in array:
        total=total+i
    peers_avg=total/x
    if yours_average>peers_avg:
        return ("True")
    else:
        return ("False")
print(is_you_are_good([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
        