def biggest_palindrome(num):
    for i in range(num,0,-1):
        y=str(i)
        z=y[::-1]
        if y==z:
            print(z)
            break
biggest_palindrome(22000)  
biggest_palindrome(200)
biggest_palindrome(1000)