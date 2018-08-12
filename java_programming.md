## This is Quick Reference Guide (QRC) for Java Programming Basics

This tutorial is not a complete tutorial for java programming but is only aiming to capture the mainly the differences w.r.t C programming or something catches my attention.

The following chart summarizes the default values for the above data types.

Data Type	Default Value (size in bits)
byte	0 (8) <br />
short	0 (16) <br />
int	0 (32)<br />
long	0L (64)<br />
float	0.0f (32)<br />
double	0.0d (64)<br />
char	'\u0000' (16)<br />
String (or any object)  	null  (no fixed size)<br />
boolean	false (**not clearly known**)<br />


#### Using Underscore Characters in Numeric Literals
In Java SE 7 and later, any number of underscore characters (_) can appear anywhere between digits in a numerical literal. This feature enables you, for example. to separate groups of digits in numeric literals, which can improve the readability of your code

Example:

long creditCardNumber = 1234_5678_9012_3456L;<br />
long socialSecurityNumber = 999_99_9999L;<br />
float pi =  3.14_15F;<br />
long hexBytes = 0xFF_EC_DE_5E;<br />
long hexWords = 0xCAFE_BABE;<br />
long maxLong = 0x7fff_ffff_ffff_ffffL;<br />
byte nybbles = 0b0010_0101;<br />
long bytes = 0b11010010_01101001_10010100_10010010;<br />


You can place underscores only between digits; you cannot place underscores in the following places:

>> At the beginning or end of a number<br />
>> Adjacent to a decimal point in a floating point literal<br />
>> Prior to an F or L suffix<br />
>> In positions where a string of digits is expected<br />


#### Declaring a variable to point to an array 
// declares an array of integers

int[] anArray;

This declaration is quite different syntactically from C...  

You can also place the brackets after the array's name:

// this form is discouraged
float anArrayOfFloats[];
However, convention discourages this form; the brackets identify the array type and should appear with the type designation.

**Below are valid array initializations**

int[] anArray = { 
    100, 200, 300,
    400, 500, 600, 
    700, 800, 900, 1000
};

The size is determined by the number of values in the curly braces.

Other way is using _new_

// create an array of integers
anArray = new int[10];


Array of strings is declared in this way:

String[][] names

In the Java programming language, a multidimensional array is an array whose components are themselves arrays. This is unlike arrays in C or Fortran. A consequence of this is that the rows are allowed to vary in length, as shown in the following

String[][] names = {
            {"Mr. ", "Mrs. ", "Ms. "},
            {"Smith", "Jones"}
        };
        
        

[java.util.array](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html) provides a handful of methods to menupulate arrays 

Some other useful operations provided by methods in the java.util.Arrays class, are:

Searching an array for a specific value to get the index at which it is placed (the binarySearch method).<br />
Comparing two arrays to determine if they are equal or not (the equals method).<br />
Filling an array to place a specific value at each index (the fill method).<br />
Sorting an array into ascending order. This can be done either sequentially, using the sort method, or concurrently, using the parallelSort method introduced in Java SE 8. Parallel sorting of large arrays on multiprocessor systems is faster than sequential array sorting.<br />


**Operators in Java**

Similar to C, all operators in same line have equal precedence. Binary operators operate from left to right and assignment operators from right to left.

Logical right shift is ">>>"  which is extra to C language. Similarly the assignment operator >>>=

_instanceof_ is another operator in jave:<br />
The java instanceof operator is used to test whether the object is an instance of the specified type (class or subclass or interface).

The instanceof in java is also known as type comparison operator because it compares the instance with type.

**A note or question from operators**

What is difference between NOT(~) and NEGATION(!) ?
The operator ~ toggles each bit in the binary representation of the number
For example ~(11111111) is 00000000 (in decimal  ~(-1) is 0) <br />
and ~(11111110) is 00000001 (in decimal ~(-2) is 1) 

The operator ! works differently.
!0 is 1
!(anything other than zero) is 0


[Summary of operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/opsummary.html) link from Oracle's java tutorial has summary. 


### Classes and Objects

#### Classes

**Constructor** is a method in the class with no return type and the name is same as that of the class.
If there is no constructor in the class, the compiler provides automatically a no-argument constructor.
This default constructor will call the no-argument constructor of the superclass; in this case if the superclass does not have a no-argument constructor (but have a constructor with arguments), the compiler will complain.



#### Objects

int value; // this is pr
imitive variable and the compiler reserves memory required to store an integer for this variable.

You can also declare a reference variable on its own line. For example:

Point originOne; //this is just a reference and it does not reserve memory as Point is a class; this is merely declaration of a reference.

Object will be created only with "new" keyword, then the memory is reserved for the object of the class Point.<br />
Creating an object of a class is also termed as **instantiating a class** 

**Return type**

_Covariant return type_ is a technique to override a method and define it to return a subclass of the original method.

**This pointer**
Usage [reference](https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html): 
1. For referring to a fields of the class which are overshadowed by constructor parameters etc.
2. From within a constructor, you can also use the this keyword to call another constructor in the same class. Doing so is called an explicit constructor invocation.
If present, the invocation of another constructor must be the first line in the constructor.

#### Controlling Access to Members of a Class
Access Levels

|Modifier |	Class	| Package |	Subclass |	World |
|--------------|:------------|:------------|:-------------|:---------|
|public |		Y |		Y |		Y |		Y |	
|protected |		Y |		Y |		Y |		N |	
|no modifier (package-private) |		Y |		Y |		N |		N |	
|private |		Y |		N |		N |		N |	


**Tips on Choosing an Access Level:** 
If other programmers use your class, you want to ensure that errors from misuse cannot happen. Access levels can help you do this.

- Use the most restrictive access level that makes sense for a particular member. Use private unless you have a good reason not to.<br />
- Avoid public fields except for constants. (Many of the examples in the tutorial use public fields. This may help to illustrate some points concisely, but is not recommended for production code.) Public fields tend to link you to a particular implementation and limit your flexibility in changing your code.<br />


#### Class Variables and Class Methods
Class variable are not instance variables meaning that these variables are associated with the class itself and not with the instance 
of the class. The instance of the class can access these variables but the value of these variables remain same for different instances 
of the class. These variables can be declared with _static_ keyword. Any object or instance of the class can change the class variables but they can also be changed without creating an object.

Class methods, similar to the class variables, are associated with the class as a whole and not with an instance of the class.
The class methods are also declared with _static_ keyword.

**Constants** 

The static modifier, in combination with the final modifier, is also used to define constants. The final modifier indicates that the value of this field cannot change.
static final double PI = 3.141592653589793;


A **static initialization block** is a normal block of code enclosed in braces, { }, and preceded by the static keyword. 
This is basically where you would like to put some logic when simple assignment is not adequate. Here is an example:

static {
    // whatever code is needed for initialization goes here
}

There is an alternative to static blocks — you can write a private static method:

class Whatever {
    public static varType myVar = initializeClassVariable();
        
    private static varType initializeClassVariable() {

        // initialization code goes here
    }
}
The advantage of private static methods is that they can be reused later if you need to reinitialize the class variable.

#### Interfaces in Java
Interface in java is a reference type similar to a class and it contains only constants, method signatures, default methods, static methods, and nested types. 
It is basically a set of methods, constatnts defined so that a class can agree to implement the interface or interfaces defined or multiple classes can agree to implement that interface or theat set of interfaces.

In below class declaration OperateCar is an interface which every car has to implement and this interface defines methods such as 
turnRight, turnLeft, changeLane etc.
public class OperateBMW760i implements OperateCar {
.
.
.
}

**These example can also be understood in the way that regulators define the interfaces and all OEMs have to implement the interfaces for the products in order to get certified.**

In commercial software products interfaces are also used as **APIs** (Application Programming Interfaces)

**defining an interface is as easy as defining a class**

An interface declaration consists of modifiers, the keyword interface, the interface name, a comma-separated list of parent interfaces (if any), and the interface body. For example:

public interface GroupedInterface extends Interface1, Interface2, Interface3 {
//constant declaration

//method signatures
}

If public keyword is not used then the interface becomes package-private; classes in the package can access the interface.

**Using interfaces** A very good demo is at [this page](https://docs.oracle.com/javase/tutorial/java/IandI/interfaceAsType.html)

**Evolving interfaces**
Suppose you have an interface and later you want to add another method in it. The problem comes is all classes implementing this interface have to implement the new method. There are two ways to solve this problem:
1. Define one more interface which implements existing one and declare the new method. If the existing interface is DoIt then have another interface DoItPlus as below
public interface DoItPlus extends DoIt{
    //new method definition
}
Now the classes which needs the new method will change and implements DoItPlus and remaining classes do not have any change.

2. Second solution is to implement [default method](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html).
Remember that default methods have to be implemented inside the interface unlike regular methods in the interface.

public interface DoIt {
       //methods declaration same in DoIt
      default boolean didItWork(int i, double x, String s) {
       // Method body 
   }
   
}
You could also define new [static methods](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html#static) to existing interfaces.




#### Inheritence
* A class has only one superclass or parent class. If no explicit superclass, _object_ class is the one all classes inherit by default.
* Subclass inherits all members i.e. all fields, methods of the superclass
* Constructors are not inherited from the superclass. Constructors are not members of the class, hence not inherited.

**What can you do in a Subclass**
A subclass inherits all of the public and protected members of its parent, no matter what package the subclass is in. If the subclass is in the same package as its parent, it also inherits the package-private members of the parent. You can use the inherited members as is, replace them, hide them, or supplement them with new members:

* The inherited fields can be used directly, just like any other fields.
* You can declare a field in the subclass with the same name as the one in the superclass, thus hiding it (not recommended).
* You can declare new fields in the subclass that are not in the superclass.
* The inherited methods can be used directly as they are.
* You can write a new instance method in the subclass that has the same signature as the one in the superclass, thus overriding it.
* You can write a new static method in the subclass that has the same signature as the one in the superclass, thus hiding it.
* You can declare new methods in the subclass that are not in the superclass.
* You can write a subclass constructor that invokes the constructor of the superclass, either implicitly or by using the keyword super.
* The following sections in this lesson will expand on these topics

All public and protected members are accessible to subclass. Private members are not accessible but if the superclass's public or private member access the private member then that private member will be accessible in the subclass as well.


**type casting of objects is tricky** 
If the object is declared as parent class object 

_What is not covered/studied_:
* Method Refereces
* Lambda Expressions
* Nested classes
* Annotations
* Using an interface as a type (read again)

**Overriding and Hiding**

An instance method in a subclass with the same signature (name, plus the number and the type of its parameters) and return type as an instance method in the superclass **overrides** the superclass's method.

If a subclass defines a static method with the same signature as a static method in the superclass, then the method in the subclass **hides** the one in the superclass.



#### Java Exceptions 
Exception is short form of exceptional event. Exception events occur when the normal flow of the program is disrupted.
When the error occurs an exception object is created and handed over to the system; this object contains the information about the error occured.

Code that fails to honor the Catch or Specify Requirement will not compile

Checked exceptions are subject to the Catch or Specify Requirement. All exceptions are checked exceptions, except for those indicated by Error, RuntimeException, and their subclasses.


**Advantages of Exceptions** over usual error handling, [details](https://docs.oracle.com/javase/tutorial/essential/exceptions/advantages.html):
* Advantage 1: Separating Error-Handling Code from "Regular" Code
* Advantage 2: Propagating Errors Up the Call Stack
* Advantage 3: Grouping and Differentiating Error Types





References //this is just a reference and it does not reserve memory as Point is a class and originOne is a object.
1. **Most Important** Oracle Official Java Tutorial : https://docs.oracle.com/javase/tutorial/java/index.html 
2. Difference between C and Java : http://durofy.com/10-major-differences-between-c-and-java/
