Q1. Why do we call Python as a general purpose and high-level programming language?
  Ans-Because they are not written in machine-readable language, Python programs need to be processed before machines can run them. Python is an interpreted language. This means that every time a program is run,
   its interpreter runs through the code and translates it into machine-readable byte code.Python is an object-oriented, high-level programming language. Object-oriented means this language is based around objects (such as data) rather than functions,
    and high-level means it's easy for humans to understand.

Q2. Why is Python called a dynamically typed language?
  Ans-Yes, it is. Python is a dynamically typed language. What is dynamic? We don't have to declare the type of variable while assigning a value to a variable in Python. Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.
Python don't have any problem even if we don't declare the type of variable. It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language. Let's see one example.
Example
 Live Demo
## assigning a value to a variable
x = [1, 2, 3]
## x is a list here
print(type(x))

Q3. List some pros and cons of Python programming language?
  ANs-Pros         ----         Cons
Cons
Beginner-friendly	        Issues with design
Large Community  	        Slower than compiled languages
Flexible and Extensible 	Security
Extensive Libraries	        Work Environment
Embeddable	                High memory consumption
Highly Scalable	            Dynamically-typed language
IoT Opportunities	        Complex multithreading
Portable                    Garbage collection leads to potential memory losses

Q4. In what all domains can we use Python?
  Ans-Since Python is the go-to programming language for domains such as artificial intelligence, machine learning and deep learning, 
  it's no surprise that it's also a fundamental tool for any data scientist.

Q5. What are variable and how can we declare them? 
  ANs-Variables are the basic unit of storage in a programming language. These variables consist of a data type, the variable name, and the value to be assigned to the variable.
   Unless and until the variables are declared and initialized, they cannot be used in the program.
   f=0
  print(f)
   like this we declare the variable and we can re-declare the variable 
  f='yunus'
  pritn(f)
  both will work fine 
  Python variables are of four different types: Integer, Long Integer, Float, and String.

Q6. How can we take an input from the user in Python?
  Ans- we can input in python in this way
    EX-a=input("Enter the value of =").

Q7. What is the default datatype of the value that has been taken as an input using input() function?
  ANs-String.

Q8. What is type casting?
  ANs-In type casting, the compiler automatically changes one data type to another one depending on what we want the program to do. For instance, in case we assign a float variable (floating point) with an integer (int) value,
   the compiler will ultimately convert this int value into the float value.  

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?  
   Ans-I am not getting this answer.

Q10. What are keywords?
  Ans-    Python keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes.
   These keywords are always available—you'll never have to import them into your code.
      EX-if,else,or true,with,while try return,from ,for ,continue,class,break,in.is.not.or.except,import ,false,raise,
        assert,del,def,async  etc...

Q11. Can we use keywords as a variable? Support your answer with reason.
   ANs-We cannot use a keyword as a variable name, function name or any other identifier. 
     They are used to define the syntax and structure of the Python language. In Python, keywords are case sensitive        

Q12. What is indentation? What's the use of indentaion in Python?
  Ans-     Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only,
   the indentation in Python is very important. 
   Python uses indentation to indicate a block of code.

Q13. How can we throw some output in Python?   
ANs-The basic way to do output is the print statement
a=input("enter the value A")
PRINT("THE VALUE OF A IS",a)

Q14. What are operators in Python?
  Ans-Operators are special symbols in Python that carry out arithmetic or logical computation
      EX -Arithmetic operators:       
  
  +	  Addition  x + y	
   -	Subtraction	x - y	
   *	Multiplication	x * y	
   /	Division	x / y	
   %	Modulus	x % y	
   **	Exponentiation	x ** y	
   //	Floor division	x // y

Q15. What is difference between / and // operators?
   Ans-   '/' is used for the normal division of two numbers.
          '//' is used to obtain the smallest integer nearest to the quotient obtained by
          a = 19
          b = 4
          print(a // b)  #This prints output as 4
          print(a / b)  #This prints output as 4.75

 Q16. Write a code that gives following as an output. 
     Ans-print("iNeuroniNeuroniNeuroniNeuron")   


Q17. Write a code to take a number as an input from the user and check if the number is odd or even.   
   Ans- chek=input("Enter the number to check even or odd =") 
print("Enter the number to check even or odd ",check)
if check%2==0:
 print("The number is even ")
else: 
 print("The number is odd")

Q18. What are boolean operator?
  Ans-Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search,
   resulting in more focused and productive results

Q19. What will the output of the following?
1 or 0
0 and 0
True and False and True
1 or 0 or 0
  Ans-zero values are false and non-zero values are true

Q20. What are conditional statements in Python?
  Ans-The if statement is a conditional statement in python, that is used to determine whether a block of code will be executed or not. Meaning if the program finds the condition defined in the if statement to be true,
   it will go ahead and execute the code block inside the if statement or else statement will be executed

Q21. What is use of 'if', 'elif' and 'else' keywords?
  ANs-The if/elif/else structure is a common way to control the flow of a program, 
  allowing you to execute specific blocks of code depending on the value of some data
  1)f statement:
  If the condition following the keyword if evaluates as true, the block of code will execute. 
  Note that parentheses are not used before and after the condition check as in other languages.
  2)else statement:
You can optionally add an else response that will execute if the condition is false
 3)elif statement
Multiple conditions can be checked by including one or more elif checks after your initial if statement. 
Just keep in mind that only one condition will execute
   
     EX--z = 7

if z > 8:
  print("I won't print!") #this statement does not execute
elif z > 5:
  print("I will!") #this statement will execute
elif z > 6:
  print("I also won't print!") #this statement does not execute
else:
  print("Neither will I!") #this statement does not execute

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote".
 If age is < 18 display "I can't vote".
   ANs- Age=input("Enter the age")
      print("Enter the age ",Age)
if(age>18):
  print("I can vote")  
else:
  print("I cannot vote")

Q23. Write a code that displays the sum of all the even numbers from the given list.
```numbers = [12, 75, 150, 180, 145, 525, 50]
   ANs-numbers = [12, 75, 150, 180, 145, 525, 50]
sum=0
if numbers%2==0:
 for val in numbers:
    sum=sum+val
    print(sum)

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
     Ans-a=input("Enter value of a=")
         b=input("Enter value of b=")
         c=input("Enter value of c=")

        if a>b:
          print(a)
          elif:
            print(b)
          else:
            print(c)

Q25. Write a program to display only those numbers from a list that satisfy the following conditions
 The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
```numbers = [12, 75, 150, 180, 145, 525, 50]
   Ans numbers = [12, 75, 150, 180, 145, 525, 50]
          if numbers%5==0:
         for i in numbers:
           if i>150:
            i++:
          elif(i>500)
            i==0:
        print(i)

   