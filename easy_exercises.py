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