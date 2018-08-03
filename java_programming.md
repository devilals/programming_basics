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

