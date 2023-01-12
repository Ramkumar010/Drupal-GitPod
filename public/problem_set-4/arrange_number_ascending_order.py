def arrange_number_ascending_order(array):
    x=sorted(array)
    y=[str(i) for i in x]
    print(" ".join(y))
arrange_number_ascending_order([10,2,3,1,1,4,1,2,32,41,22,10,2,4])    