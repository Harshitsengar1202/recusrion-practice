def palindrome(i,strng):
    if i>=len(strng)/2:
        return True
    elif strng[i]!=strng[len(strng)-i-1]:
        return False
    else:
        return palindrome(i+1,strng)
    

strng=input("Enter a string:")
print(palindrome(0,strng))