def remaining_in_bus(array):
    new_array=[]
    for j in array:
        if ((j[0]<0) or (j[1]<0)):
            new_array.append(j)
    if len(new_array)==0:
        
        inside=0
        outside=0
        remaining=0
        for i in array:
            inside=inside+i[0]
            outside=outside+i[1]
            remaining=inside-outside
        return ('Remaining people in the bus is'+" "+ str(remaining))
    else:
        return ("Integer can't be negative")

x=remaining_in_bus([[3,0],[9,-1],[4,10],[12,2],[6,1],[7,10]])
print(x)