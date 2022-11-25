Q1. What is the purpose of Python's OOP?
   Ans-In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
    It aims to implement real-world entities like inheritance, polymorphisms, encapsulation   and Data Abstraction

Q2. Where does an inheritance search look for an attribute?
   Ans-An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from,
    then in all higher superclasses, progressing from left to right

Q3. How do you distinguish between a class object and an instance object?
   Ans-A class is a template for creating objects in a program, whereas the object is an instance of a class. A class is a logical entity, while an object is a physical entity.
    A class does not allocate memory space; on the other hand, an object allocates memory space

Q4. What makes the first argument in a class’s method function special?
   Ans-The calling process is automatic while the receiving process is not (its explicit). This is the reason the first parameter of a function in class must be the object itself. Writing this parameter as self is merely a convention.
    It is not a keyword and has no special meaning in Python.

Q5. What is the purpose of the init method?
   Ans-The __init__ method allows you to accept arguments to your class.
    More importantly, the __init__ method allows you to assign initial values to various attributes on your class instances

Q6. What is the process for creating a class instance?
   Ans-To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts

Q7. What is the process for creating a class?
   Ans-Create a Class. To create a class, use the keyword class : ...
Create Object. Now we can use the class named MyClass to create objects: ...
The self Parameter. ...
Modify Object Properties. ...
Delete Object Properties. ...
Delete Objects.

Q8. How would you define the superclasses of a class?
   Ans-he class from which a class inherits is called the parent or superclass. A class which inherits from a superclass is called a subclass,
    also called heir class or child class. Superclasses are sometimes called ancestors as well
    class a:
    def feature1(self):
        print("The feature is working")

class b(a):
    def feature2(self):
        print("The feature 2 is working")

c=b()
c.feature1()
c.feature2()

Q9. What is the relationship between classes and modules?
   Ans-So a module in python is simply a way to organize the code, and it contains either python classes or just functions. If you need those classes or functions in your project, you just import them. For instance,
    the math module in python contains just a bunch of functions, and you just call those needed

Q10. How do you make instances and classes?
   Ans-To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.

Q11. Where and how should be class attributes created?
   Ans-A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method.
  Use class_name. ...
  Use class attributes for storing class contants, track data across all instances, and setting default values for all instances of the class.

Q12. Where and how are instance attributes created?
   Ans-Instance attributes are defined in the constructor. Defined directly inside a class.
    Defined inside a constructor using the self parameter.
    class a:
    # Constructor of class
    # it is mainly used for assignment of instance variables
    def feature1(self,name,age):
        self.name=name
        self.age=age

Q13. What does the term "self" in a Python class mean?
   ANs-The self in keyword in Python is used to all the instances in a class. By using the self keyword, 
   one can easily access all the instances defined within a class, including its methods and attributes

Q14. How does a Python class handle operator overloading?
   Ans-Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists.
    It is achievable because '+' operator is overloaded by int class and str class.
    we use class a:
    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __add__(self, other):
        name=self.name+other.name
        age=self.age+other.age

Q15. When do you consider allowing operator overloading of your classes?
   Ans-Operator overloading facilitates the specification of user-defined implementation for operations wherein one or both operands are of user-defined class or structure type. 
   This helps user-defined types to behave much like the fundamental primitive data types

Q16. What is the most popular form of operator overloading?
   Ans-A very popular and convenient example is the Addition (+) operator. Just think how the '+' operator operates on two numbers and the same operator operates on two strings.
    It performs “Addition” on numbers whereas it performs “Concatenation” on strings

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
   Ans-inheritance and polymorphism. Both inheritance and polymorphism are key ingredients for designing robust,
    flexible, and easy-to-maintain software. 

Q18. Describe three applications for exception processing.
   Ans-There are three types of exception—the checked exception, the error and the runtime exception

Q19. What happens if you don't do something extra to treat an exception?
   Ans-An exception object is created when a Python script raises an exception
    If the script explicitly doesn't handle the exception, the program will be forced to terminat

Q20. What are your options for recovering from an exception in your script?
   Ans-You can also provide a generic except clause, which handles any exception. After the except clause(s), you can include an else-clause. The code in the else-block executes if the code in the try: block does not raise an exception. 
   The else-block is a good place for code that does not need the try: block's protection

Q21. Describe two methods for triggering exceptions in your script
   Ans-syntax errors, exceptions and logical errors 
   Ex-a=4
        b=4
try:
    if (a>b):
      print(a)
    else:
      print(c)
except:
    print(str("num not find"))

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists
   Ans-

Q23. What is the purpose of the try statement?
   Ans-The try block lets you test a block of code for errors. 
   The except block lets you handle the error. The else block lets you execute code when there is no error.

Q24. What are the two most popular try statement variations?
   Ans-The Different Try/Except Variations. So far we've used a try / except and even a try / except / except There are two other optional segments to a try block: else and finally 
   . Both of these optional blocks will come after the try and the except .

Q25. What is the purpose of the raise statement?
   Ans-Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program.
    It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack

Q26. What does the assert statement do, and what other statement is it like?
   ANS-The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True,
    if not, the program will raise an AssertionError

Q27. What is the purpose of the with/as argument, and what other statement is it like?
   Ans-In Python, with statement is used in exception handling to make the code cleaner and much more readable. 
   It simplifies the management of common resources like file streams

Q28. What are *args, **kwargs?
   ANs-*args specifies the number of non-keyworded arguments that can be passed and the operations that can be performed on the function in Python
    whereas **kwargs is a variable number of keyworded arguments that can be passed to a function that can perform dictionary operations

Q29. How can I pass optional or keyword parameters from one function to another?
   Ans-Users can either pass their values or can pretend the function to use theirs default values which are specified. In this way, the user can call the function by either passing those optional parameters or just passing the required parameters.
    Without using keyword arguments. By using keyword arguments

Q30. What are Lambda Functions?
   Ans-A lambda function is a small anonymous function.
   A lambda function can take any number of arguments, but can only have one expression
      x = lambda a : a + 10
print(x(5))


Q31. Explain Inheritance in Python with an example?
   Ans-Inheritance allows us to define a class that inherits all the methods and properties from another class.
      Parent class is the class being inherited from, also called base class.
      Child class is the class that inherits from another class, also called derived class
        class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.person()

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func().
 If we call func() from an object of class C, which version gets invoked?
    Ans-

Q33. Which methods/functions do we use to determine the type of instance and inheritance?
   ANs-Use isinstance() to check an instance's type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int .
Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of in

Q34.Explain the use of the 'nonlocal' keyword in Python
   Ans-The nonlocal keyword is used to work with variables inside nested functions,
    where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local

Q35. What is the global keyword?
   ANs-Declare a global variable inside a function, and use it outside the function
     def myfunction(x):
  global x
  x = "hello"
