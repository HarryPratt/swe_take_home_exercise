# Prefix & Infix Calculator

## Part One
You are to write a program that accepts numerical calculations in prefix notation, such as + 5 7 or - 12 * 2 6.

You can make the following assumptions:

* The system should support the operators {+, -, *, /} which all take exactly two args.
* The input literals are positive integers
* Calculations can be done in the floating-point or integer domain
* Handling division by zero is unimportant; program can crash or do anything if that arises.
* You don't need to consider operator presidence
* You are free to use any programming language of choice but please provide any requirements to run the code EG: Python version or Pip dependencies

### Sample input (caret prompt for clarity only):
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
3
> / 3 2
1 (or 1.5)
```

All assumptions from the previous task hold for this one.
=======
## Part Two
Implement your calculator in infix notation with support for full-parenthesized operands. It's OK to assume that all the tokens are space-separated, including the parenethesis tokens


### Sample input (caret prompt for clarity only):
```
> ( 1 + 2 )
3
> ( 1 + ( 2 * 3 ) )
4
> ( ( 1 * 2 ) + 3 )
5
> ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
-1 (or -1.8)
```

## Additional Bonus
Create a web-based version of your calculator, as in a service with a RESTful interface. The goal would be to be able to interact with your calculator over the internet vs a standalone desktop based application.

# Deliverables:
A GitHub repo with your working code for the prefix and infix versions along with accompanying test cases

