def longest_word(array):
    length=len(array[0])
    for i in array:
        if len(i)>length:
            length=len(i)
    return (length)        
print(longest_word(['simple', 'is', 'better', 'than', 'complex']))