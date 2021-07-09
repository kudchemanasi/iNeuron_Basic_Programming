"""Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3."""
def integer(a,b,c):
    num = 0
    if (a == b and a == c ):
        print("num = 3")
    elif (a == b or a == c):
         print("num = 2")
    else:
        print("num = 0")
    return num
print(integer(6,6,7))

"""Question2
Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]
dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]"""

dict = {'Likes': 2, 'dislikes': 3, 'followers': 31}
list = list(dict.items())
print(list)

#4.Write a function, that replaces all vowels in a string with a specified vowel.
Vowels=["A","E","I","O","U","a","e","i","o","u"]
def removeVowels(str):
    for Vowels in str:
        res=str.replace("manasi","u")
    return res
    print(removeVowels(res))

"""Question5
Create a function that takes a string as input and capitalizes a letter if its 
ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
"""
def fun(*args):
    def split(strr):
        return [char for char in strr]
    for i in split(strr):
        if(num%2==0):
            print(strr.upper())
        else:
             print(strr.lower())
    print(fun())



