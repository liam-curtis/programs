import re
from pip._vendor.pyparsing.core import nums

#basic python exercises found on codingBat,
def main():
    hi = [1,2,3,4,5,6,7,8]
    print(make_bricks(3,1,9))



##warmup-1 exercises

#determines if user should sleep in 
#if weekday if's not weekday or it is vacation user should sleep in
def sleep_in(weekday,vacation):
    if (weekday != True or vacation == True):
        return True 
    else:
        return False

##string-1 exercises

#says hello to the inputed name
def hello_name(name):
    return ("Hello " + name + "!")

#returns parameters a and b in abba order
def make_abba(a,b):
    return a+b+b+a

##string-2 exercises

#counts number of his in a string
def count_hi_re(string):
    x = re.findall("hi",string)
    return len(x)

def count_hi(string):
    return count_hi_helper(string,0)

def count_hi_helper(string, count): #helper methods to count_hi (needs to kick-start)
    if(len(string) == 1 or len(string) == 0):
        return count
    elif(string[0:2] == "hi"):
        count = count + 1
        return count_hi_helper(string[1:],count)
    else:
        return count_hi_helper(string[1:],count)

#returns True if the string act and dog appear the same number of times in the given string
def cat_dog(s):
    dog = 0;
    cat = 0;
    for x in s[0:len(s)-2]:
        if(s[0:3] == "dog"):
            dog = dog + 1
        if(s[0:3] == "cat"):
            cat = cat + 1
        s = s[1:]   
    return dog == cat    
        
##list-2 exercises 
#return the number of evens in a given array
def count_evens(nums):
    count = 0
    for nums in nums:
        if nums % 2 == 0:
            count = count + 1
    return count
                    
#returns the difference between the largest and smallest values
def big_diff(nums):
    big = nums[0]
    small = nums[0]
    for nums in nums:
        if nums > big:
            big = nums
        if nums < small:
            small = nums
    return big-small

"""
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
"""
def make_bricks(small, big, goal):
    return small+big*5 >= goal 

if __name__ == "__main__": 
    main()
