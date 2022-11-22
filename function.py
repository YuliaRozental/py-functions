#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    list = [a, b, c]
    return max(list)    

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(myList):
    result = 1
    for x in myList:
        result = result * x
        return result
    
#Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    return str[::-1]

#Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(a,b,c):
        if(a>=b) and (a<=c):
            print(a,"is within the range",b,"-",c)

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
        return n>=1

