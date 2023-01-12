def maximum_product(array):
    max1=array[0]
    max2=array[1]
    for i in array:
        if i>max1:
            max2=max1
            max1=i
        elif ((i>max2) and (i!=max1)):
            max2=i 
    product=max1*max2
    print(product)
maximum_product([10,100,20,40,102,22])    