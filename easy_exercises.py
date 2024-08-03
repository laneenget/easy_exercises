# Implementation of easy leet code exercises to use as warm-up

# Slicing works like arr[start:stop:step]
# Check if a string is a palindrome by reversing the string
def isPalindrome(x):

    if x < 0:
        return False
    
    num_str = str(x)

    return True if num_str == num_str[::-1] else False

# Check if input is a palindrome without string conversion
def isPalindromeNum(x):

    if x < 0:
        return False
    
    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x

# Convert a roman numeral to an integer
def romanToInt(s):

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0

    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
            num += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
        else:
            num += roman_dict[s[i]]

# ...girl
# Takes an input string and determines if any included brackets are not a valid match
def isValidBracket(s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s) % 2 != 0:
        return False

    open_brackets = []

    for char in s:
        if char in '([{':
            open_brackets.append(char)
        else:
            if not open_brackets or \
                (char == ')' and open_brackets[-1] != '(') or \
                (char == ']' and open_brackets[-1] != '[') or \
                (char == '}' and open_brackets[-1] != '{'):
                    return False
            open_brackets.pop()
    return not open_brackets

# Merges two sorted linked lists into one
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1, temp2 = list1, list2
        list3 = ListNode()
        ret = list3

        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    list3.next = ListNode(temp1.val)
                    temp1 = temp1.next
                else:
                    list3.next = ListNode(temp2.val)
                    temp2 = temp2.next
            elif temp1:
                list3.next = ListNode(temp1.val)
                temp1 = temp1.next
            elif temp2:
                list3.next = ListNode(temp2.val)
                temp2 = temp2.next
            list3 = list3.next

        return ret.next

# Write a program which will find all such numbers which are divisible 
# by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence 
# on a single line.
def div_by_seven():

    div = []
    for num in range(2000, 3200):
        if num % 7 == 0 and num % 5 != 0:
            div.append(str(num))

    print(','.join(div))

# Write a program which can compute the factorial of a given
# numbers. The results should be printed in a comma-separated
# sequence on a single line.
def factorial(n):

    if n == 0:
        return 1
    
    return n * factorial(n-1)

# With a given integral number n, write a program to
# generate a dictionary that contains (i, i*i) such
# that i is an integral number between 1 and n included.
# The program should print the dictionary.
def square(n):
    return n*n

def squareDict(n):

    square_dict = {}
    i = 0

    while i <= n:
        square_dict[i] = square(i)
        i+=1

    return square_dict

# Write a program which accepts a sequence of comma-separated
# numbers from console and generate a list and a tuple which
# contains every number.
def list_and_tuple():

    lst = input("Enter a sequence of comma-separated numbers: ").split(", ")
    tpl = tuple(lst)
    print(lst)
    print(tpl)

# Define a class which has at least two methods. getString: to
# get a string from console input, printString: to print the string
# in upper case.
class GetAndPrint:

    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Input a string: ")
    
    def printString(self):
        print(self.str)

# Write a program that calculates and prints the value according to
# the formula Q = sqrt((2*C*D)/H) where C = 50, H = 30, and D is 
# an input value
def calculate_q():

    c = 50
    h = 30
    d = input("Enter a sequence of numbers seperated by a comma: ").split(", ")

    

def main():
    print(factorial(8))
    print(factorial(4))

    print(squareDict(6))
    print(squareDict(9))

    list_and_tuple()

if __name__ == "__main__":
    main()