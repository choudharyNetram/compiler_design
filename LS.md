# Syntax of Language #

## Basic Types ##
Assigning variable names:
```
assign int: x = 42;
assign string: name = "John";
assign bool: flag = True;
```
String functions:
```
name.at(3);
name.replace(ind, "k");
string1.slice(start,end);
string1.concat(string2);
```
at(i) function returns the  character at index i. <br>
replace(i, "c") replaces a character at index i with character "c".<br>
slice(s, e) function returns substring from index s to index e (not inclusive).<br>
concat(str) function concatenates string str at the end.<br>

Operators:
```
Assignment operator: =
Comparison operators: !=,==, <, >
Binary operators: +,-,*,/, **,%, and, or
Unary operators: ++,--
```
Working of operators:
```
assign int: a = 2;
assign int: b = 3;
a == b returns  False;  $ 2 is not equal to 3
a != b returns  True ;  $ 2 is not equal to 3
a  < b returns  True ;  $ 2 is less than 3
a  > b returns  False;  $ 2 is not greater than 3
a  + b returns  5 ;     $ 2+3=5
a  - b returns -1 ;     $ 2-3=-1
a  * b returns  6 ;     $ 2*3=6
a /  b returns  0.67 ;  $ 2/3=0.67
a  % b returns  2       $ 2%3=2
!a returns True;        $ Not True is False
a && b returns False;   $ And operator
a || b returns True ;   $ Or operator
a++;                    $ Adds one to variable a
a--;                    $ Subtracts one from variable a
```

Comments:
>Single line: _$ This is a comment._<br>
Multi line: _$* Comment starts here,<br> and ends here. *$_<br>

Print statement: prnt("Hello World")<br>
Formatted print:...

## Compound Types: ##
Lists, Tuples, and Arrays:<br>
```
tuple: let tuple: tname = (1,2 )
array: assign int: name(max_size) = [1,2,3,4];
lists: assign list: name1 = [];
```
_Mutability:..._

Functions
```
name.append(5) ; 
size = name.size();
var x = name.at(2);
name.head();
name.tail();
data_type x;
name1.append(5);
size = name1.size();
```
>append() function  adds an element to the end. <br>
size() function gives size of the data type. <br>
at(i) function returns the value at index i. <br>
head() function returns first element of the list/array. <br>
tail() function returns last element of the list/array. <br>
data_type x gives the datatype of x. <br>

## Conditionals and Loops ##
If else statement:
>agar condition  {<br>
&emsp; _statement_} <br>
baki condition  {<br>
&emsp; _statement_} <br> 
nahito {<br>
&emsp; _statement_} <br>

While loop:
>jabtak condition {<br>
&emsp; _statement_ } <br>

## Functions: ##
Defining a function:
```
func:bool  myFunction (int: x, int: y)  {
    result = x>y;
    respond result;
}
```
Calling a function:
```
myFunction(3,4); will return false as 3 is not greater than 4
```

## Closures ##
A closure is a way to encapsulate a function along with its environment so that it can be executed later with the help of that environment.
```
func:int myFunction (int: x, int: y)  {
	    assign int: x = 5;
	    assign int: result = 0;
    func:int myFunction (int: a, int: b)  {
	    assign k = x+a;
    	respond k;
    }
    respond result*k;
}
```

## Exceptions ##
You can use try catch blocks to handle exceptions. The "throw" keyword is used to throw an exception and the "catch" keyword is used to catch it.
```
try{
	throw exception
}
catch (exception){
	prnt(3, “ blabla \n”);      $ \n → new line.
	prnt(variable_name);
}
```
