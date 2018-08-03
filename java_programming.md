## This is Quick Reference Guide (QRC) for Java Programming Basics

This tutorial is not a complete tutorial for java programming but is only aiming to capture the differences w.r.t C programming or 
anything to be noted.

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
        
        
