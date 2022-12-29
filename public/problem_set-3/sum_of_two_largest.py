def sum_of_two_largest(array):
        
        max1=array[0]
        max2=array[1]
        for i in array:
            if i>max1:
                max2=max1
                max1=i
            elif ((i>max2) and (i!=max1)):
                max2=i 
        total=max1+max2
        return (total)
print (sum_of_two_largest([10,20,30,40,50]))