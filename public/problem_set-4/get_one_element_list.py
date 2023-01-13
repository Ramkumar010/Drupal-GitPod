def get_one_element_list(array):
    l=len(array)
    x=str(l)

    if x[-1]==str(2) or x[-1]==str(4) or x[-1]==str(8) or x[-1]==str(6):
        count=1
        i=1 
        while i<=l:
            y=l/2
            if y!=1:
                count=count+1 
                l=y
            if y==1:
                break
            i+=1 
        print(count)
    else:
        print("invalid input")
        
get_one_element_list([1,2,3,4,5,6,7,8])   
get_one_element_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
get_one_element_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])