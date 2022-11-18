Q26. What is a string? How can we declare string in Python?
  Ans-Python are arrays of bytes representing unicode characters. However, Python does not have a character data type,
   a single character is simply a string with a length of 1. Square bracket
    For example, "hello world" and "LKJH019283" are both examples of strings

Q27. How can we access the string using its index?
  Ans-You can access the characters in a string by referring to its index number inside square brackets [] 

Q28. Write a code to get the desired output of the following``
string = "Big Data iNeuron"
desired_output = "iNeuron"
  Ans-  string="Big data iNeuron"
         print(string[9: ])

 Q29. Write a code to get the desired output of the following  \
       string = "Big Data iNeuron"
         desired_output = "norueNi"
    Ans-string="Big data iNeuron"
        print(string[ :8 : -1])

Q30. Resverse the string given in the above question
   Ans-   print(string[9: ])

 Q29. Write a code to get the desired output of the following  \
       string = "Big Data iNeuron"
         desired_output = "norueNi"
    Ans-string="Big data iNeuron"
        print(string[ :8 : -1])      

Q30. Resverse the string given in the above question
  ANs- Ans-string="Big data iNeuron"
        print(string[ : : -1])  

Q31. How can you delete entire string at once?
  ANs-string="yunus"
del string

Q32. What is escape sequence?
   ANs-The escape character allows you to use double quotes when you normally would not be allowed:
     txt = "We are the so-called \"Vikings\" from the north."


Q33. How can you print the below string?
```'iNeuron's Big Data Course
  Ans-txt = "\'INeuron's Big data course\'"
print(txt)

Q34. What is a list in Python?
  ANs-A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
   lists are defined by having values between square brackets [ ] .

Q35. How can you create a list in Python?
  ANs txt=["yunus",22,'mulla']
    print(txt)

Q36. How can we access the elements in a list?
  Ans-The syntax for accessing the elements of a list is the same as the syntax for accessing the characters of a string.
   We use the index operator[]

Q37. Write a code to access the word "iNeuron" from the given list.
```lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
  ANs-lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
smpl=lst[4]
print(smpl[2])

Q38. Take a list as an input from the user and find the length of the list.
  Ans-lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(len(lst))

Q39. Add the word "Big" in the 3rd index of the given list.
```lst = ["Welcome", "to", "Data", "course"]
  Ans-lst = ["Welcome", "to", "Data", "course"]
lst.insert(2,"Big")
print(lst)

Q40. What is a tuple? How is it different from list?
  Ans-Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable.
  List is useful for insertion and deletion operations. Tuple is useful for readonly operations like accessing elements. List consumes more memory.
   Tuples consumes less memory.

Q41. How can you create a tuple in Python?
  ANs-A tuple is created by placing all the items (elements) inside parentheses () , separated by commas.


Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason
  Ans-tple=()
  tple[1]='Yunus'
  print(tple)
    'tuple' object does not support item assignment or insertion

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
  Ans-though it cannot modify an existing tuple, so we cannot append the tupple 

Q44. Take a tuple as an input and print the count of elements in it.
  Ans-tple=("Yunus")
  for i in tple:
   print(len(i))

Q45. What are sets in Python?
   ANs- A  set is created by placing all the items (elements) inside curly braces {} 
It can have any number of items and they may be of different types (integer, float, tuple, string etc.).# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error
Set items are unordered, unchangeable, and do not allow duplicate values.

Q46. How can you create a set?
  Ans-WE can create a set by curly braces {} 
     Ex my_set={1,2,3,4}

Q47. Create a set and add "iNeuron" in your set.
  Ans-set={'' }
set.add("iNeuron")
print(set)

Q48. Try to add multiple values using add() function.
  Ans-# myset={'mango','yunus'}
# mylist=("iNeuron",'Big data',"yunus777")
#
# myset.update(mylist)
#
# print(myset)

Q49. How is update() different from add()?
   Ans-We use add() method to add single value to a set. We use update() method to add sequence values to a set.
    Here Sequences are any iterables including list , tuple , string , dict etc.

Q50. What is clear() in sets?
  Ans-clear() function is used to remove all the elements of the set container. It clears the set and converts its size to 0.


Q51. What is frozen set?
   Ans-Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time
   The frozenset() function returns an unchangeable frozenset object

Q52. How is frozen set different from set?
    Ans-Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. Due to this,
     frozen sets can be used as keys in Dictionary or as elements of another set

Q53. What is union() in sets? Explain via code.
  Ans-What is a union in sets?
Image result for Q53. What is union() in sets? Explain via code.
The union of two sets is a set containing all elements that are in A or in B (possibly both)
x∈(A∪B)
myset={'mango','yunus'}
mylist={'grapes','salman'}
z=myset.union(mylist)
print(z)

Q54. What is intersection() in sets? Explain via code
  Ans-The intersection of sets can be denoted using the symbol '∩'.
   As defined above, the intersection of two sets A and B is the set of all those elements which are common to both A and B
   myset={'mango','yunus'}
mylist={'grapes','salman','yunus'}
z=myset.intersection(mylist)
print(z)

Q55. What is dictionary in Python?
   Ans-Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
Ex-thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

Q56. How is dictionary different from all other data structures
   Ans-A dictionary is a collection of data values. 
   It holds a key: value pair in which we can easily access a value if the key is known. 
   It improves the readability of your code and makes it easier to debug
   It is fast as the access of a value through a key is a constant time operation

Q57. How can we delare a dictionary in Python?
  Ans-A Dictionary in python is declared by enclosing a comma-separated list of key-value pairs using curly braces({})
  Ex-thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

Q58. What will the output of the following?
```var = {}
    print(type(var)
 Ans=<class 'dict'>

Q59. How can we add an element in a dictionary?
  Ans-by using the update() method:
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"colour":"red"})
print(thisdict)thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"colour":"red"})
print(thisdict)

Q60. Create a dictionary and access all the values in that dictionary.
  Ans-thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for k,v in thisdict.items():
 print("the value of dict is ",v)

Q61. Create a nested dictionary and access all the element in the inner dictionary.
   Ans-thisdict = {
   "mydict1": {
 "brand": "Ford",
   "model": "Mustang",
     "year": 1964,
},

     "mydict2":{

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }
}

for k,v in thisdict.items():
  print("the value of dict is ",k,"\'"
        "And the value of key is ",v,"\'")

Q62. What is the use of get() function?
  Ans-
  The get() method returns the value of the item with the specified key.
  thisdict = {
   "mydict1": {
 "brand": "Ford",
   "model": "Mustang",
     "year": 1964,
},

     "mydict2":{

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }
}
x=thisdict.get("mydict1")
print(x)

Q63. What is the use of items() function?
  Ans-The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
      The view object will reflect any changes done to the dictionary, see example below.
      Ex-thisdict = {
   "mydict1": {
 "brand": "Ford",
   "model": "Mustang",
     "year": 1964,
},

     "mydict2":{

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }
}
x=thisdict.items()
print(x)

Q64. What is the use of pop() function?
   Ans-The pop() method removes the specified item from the dictionary.
   mydict2={

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }

mydict2.pop("name")
print(mydict2)

Q65. What is the use of popitems() function?
  Ans-The popitem() method removes the item that was last inserted into the dictionary.
   In versions before 3.7, the popitem() method removes a random item
   mydict2={

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }

mydict2.popitem()
print(mydict2)

Q66. What is the use of keys() function?
   Ans-The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
       The view object will reflect any changes done to the dictionary
       mydict2={

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }

x=mydict2.keys()
# mydict2["branch"]="civil"
print(x)

Q67. What is the use of values() function?
  Ans-The values() method returns a view object. The view object contains the values of the dictionary, as a list.
      The view object will reflect any changes done to the dictionary
     mydict2={

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }

x=mydict2.values()
# mydict2["branch"]="civil"
print(x)

Q68. What are loops in Python?
   Ans-Looping means repeating something over and over until a particular condition is satisfied. A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied.
    Such a type of statement is also known as an iterative statement.

Q69. How many type of loop are there in Python?
  Ans-There are two types of loops in Python, for and while.

Q70. What is the difference between for and while loops?
  Ans-Both for loop and while loop is used to execute the statements repeatedly while the program runs. The major difference between for loop and the while loop is that for loop is used when the number of iterations is known,
   whereas execution is done in the while loop until the statement in the program is proved wrong.

Q71. What is the use of continue statement?
   Ans-A continue statement ends the current iteration of a loop. Program control is passed from the continue statement to the end of the loop body.
    A continue statement can only appear within the body of an iterative statement, such as do , for , or while .

Q72. What is the use of break statement?
   Ans-Break Statement is a loop control statement that is used to terminate the loop. As soon as the break statement is encountered from within a loop,
    the loop iterations stop there, and control returns from the loop immediately to the first statement after the loop.

Q73. What is the use of pass statement?
  Ans-The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
   Empty code is not allowed in loops, function definitions, class definitions, or in if statements

Q74. What is the use of range() function?
  Ans-The range() is an in-built function in Python. It returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number. 
  It has three parameters, in which two are optional: start: It's an optional parameter used to define the starting point of the sequence.

Q75. How can you loop over a dictionary?
  ANs-In Python, to iterate the dictionary ( dict ) with a for loop, use keys() , values() , items() methods
    Ex-mydict2={

        "name": "yunus",
        "rollno": 22,
        "subj":"history"

     }

for i in mydict2.items():
    print(i)

Q76. Write a Python program to find the factorial of a given number
  Ans-def myfact(n):
    if n==0 or n==1:
     return 1

    result=1
    for num in range(1,n+1):
     result=result*num
    return result

z=7
print("the fact of x is ",myfact(z))

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100
  ANs-p=int(input("ENter the principle amount = "))
      r=int(input("ENter the rate of interest % = "))
      t=int(input("Enter the time period = "))
      si=(p*r*t)/100
      print("The simple intrest is ",si)

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t
  Ans-# P=int(input("ENter the principle amount = "))
# R=int(input("Enter the rate of intrest = "))
# t=int(input("Enter the time take = "))
# Ci=P*(1+ R/100)**t
# print("The compound interest is = ",Ci)

Q79. Write a Python program to check if a number is prime or not
   Ans-
num=10
for i in range(2,num):
    if num%i==0:
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break

Q80. Write a Python program to check Armstrong Number.
   Ans-num=int(input("Enter the positive integer = "))
order=len(str(num))
sum=0
temp=num
while temp>0:
 digit=num%10
 sum=digit**order
 temp=num//10

if num==sum:
    print("The number is armstrong",num)
else:
    print('Not an armstrong',num)

Q81. Write a Python program to find the n-th Fibonacci Number.
   ANs-# def fib(n):
#     a=0
#     b=1
#     c=a+b
#     for i in range(2,n):
#         if n==1:
#             print(1)
#             a = b
#             b = c
#             c = a + b
#         while n>1:
#
#          a=b
#          b=c
#          c=a+b
#         print(c)
#         break
#
#
#
# fib(10)

Q82. Write a Python program to interchange the first and last element in a list
   Ans-
def exchnge(num):
    st=len(num)

    temp=num[0]
    num[0]=num[-1]
    num[-1]=temp
    return num
num=[1,2,3,4,6,7,8,5,8,4]
print("The new list is ",exchnge(num))


Q83. Write a Python program to swap two elements in a List
    Ans-def swaping(mylist):


    mylist[1],mylist[3]=mylist[3],mylist[1]
    return mylist

mylist = [22, 5, 66, 7]

Q84. Write a Python program to find N largest element from a list.
    ans=def N_max_elements(list, N):
    result_list = []

    for i in range(0, N):
        maximum = 0

        for j in range(len(list)):
            if list[j] > maximum:
                maximum = list[j]

        list.remove(maximum)
        result_list.append(maximum)

    return result_list


list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

print(N, "max elements in ", list1)


print(N_max_elements(list1, N))

Q85. Write a Python program to find cumulative sum of a List  
   ans-num=[10,30,20,40,3]
result=[]
sum=0

for i in num:
   sum=sum+i
   result.append(sum)



print(result)

Q86. Write a Python program to check if a string is palindrome or not
   Ans-def palindrome(mystring):
    if(mystring==mystring[:  : -1]):
        print("the string is palindrome =",mystring)
    else:
        print("Not a palindrome = ",mystring)

mystring="madam"
palindrome(mystring)

Q87. Write a Python program to remove i'th element from a string
   Ans-# def remove_i(s,n):
#      a=s[0:n]
#      b=s[n+1: ]
#      return a+b
#
# s="yunus"
# n=0
# remove_i(s,n)

Q88. Write a Python program to check if a substring is present in a given string
   Ans-def find_substring(string ,substring):
     if substring in string :
          print("yes")
     else:
          print("no")



mystring="yunus Mulla"
substring="yunus"
find_substring(mystring,substring)

Q89. Write a Python program to find words which are greater than given length k
   Ans-def word_k(k, s):    
  
    word = s.split(" ")
    
    for x in word:
      
        if len(x)>k:
          
          print(x)
k = 3
s ="Python is good"
word_k(k, s)

Q90. Write a Python program to extract unquire dictionary values
   Ans-mydict={
     "a":[1,2,3],
     "b":[4,5,6,3,1],
     "c":[7,8,9]

}

res = list(sorted({ele for val in mydict.values() for ele in val}))
print(res)

Q91. Write a Python program to merge two dictionary
  ANs-mydict1 = {
          "name": "yunus",
          "rallno": 57,
          "age": 23
     }


mydict2={
     "college":"siet",
     "branch":"cv"
}

print(mydict1 | mydict2)

Q92. Write a Python program to convert a list of tuples into dictionary.
```Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
   Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
     Ans-mylist= [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
x=dict(mylist)
print(x)

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```Input: list = [9, 5, 6]
   Output: [(9, 729), (5, 125), (6, 216)
     Ans-mylist = [9, 5, 6]
sum=0



result=[(i,i**3) for i in mylist]
print(result)


Q94. Write a Python program to get all combinations of 2 tuples.
```Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
   Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
      Ans-test_tuple1 = (7, 2)
test_tuple2 = (7,8)
print("the tuple 1 is ="+str(test_tuple1))
print("the tuple 1 is ="+str(test_tuple2))
result=0
# for i in test_tuple1:
#  for j in test_tuple2:
result=[(x,y)for x in test_tuple1 for y in test_tuple2]
result=result+[(x,y)for x in test_tuple2 for y in test_tuple1]
print(str(result))


Q95. Write a Python program to sort a list of tuples by second item.
```Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
   Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
   Ans- 


Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * *
  Ans-   x=5
for i in range (0,x):
 for j in range(0,i+1):
     print("*" ,end=" ")
 print("\n")

Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
x=7
for i in range (0,x):
 for j in range(0,x):
     if j<=x-i:
         print(" ",end=" ")
     else:
         print("*",end=" ")

 print("\n")

 Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * *
  Ans-
x=5
for i in range(x):
    for j in range (x-i-1):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

   
Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4
   Ans- x=5
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E
   Ans-x=5
for i in range(65,x+65):
        for j in range(65,i+1):
            print(chr(i),end=" ")
        print()
  
     
  
