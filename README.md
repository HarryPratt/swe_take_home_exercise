# Prefix Calculator

You are to write a program that accepts numerical calculations in prefix notation, such as + 5 7 or - 12 * 2 6.

You can make the following assumptions:

* The system should support the operators {+, -, *, /} which all take exactly two args.
* The input literals are nonnegative integers, which simplifies parsing, though internally negative numbers can arise and should be handled.
* Calculations can be done in the floating-point or integer domain
* Handling division by zero is unimportant; program can crash or do anything if that arises.

## Sample input (caret prompt for clarity only):
```
> 3
3
> + 1 2
3
> + 1 * 2 3
7
> + * 1 2 3
5
> - / 10 + 1 1 * 1 2
3
> - 0 3
-3
> / 3 2
1 (or 1.5)
```

## Additional Bonus #1
Implement your algorithm but in infix notation with support for full-parenthesized operands. 

Example inputs would be as follows:
```
> 3
> ( 1 + 2 )
> ( 1 + ( 2 * 3 ) )
> ( ( 1 * 2 ) + 3 )
> ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
```

## Additional Bonus #2
Create a web-hosted version of your calculator  a RESTful interface for either the prefix or infix versions (or both) of your calculator. The goal would be to be able to interact with a web-hosted version  of your calculator (e.g. a service) via a RESTful API. 

# Deliverables:
* A GitHub repo with your working code and accompanying test cases
* You are free to use any programming lanugage of choice.
