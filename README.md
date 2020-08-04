# Prefix Calculator

Candidate is to write a program that accepts numerical calculations in prefix notation, such as + 5 7 or - 12 * 2 6.

* The system should support the operators {+, -, *, /} which all take exactly two args.
* The input literals are nonnegative integers, which simplifies parsing, though internally negative numbers can arise and should be handled.
* Calculations can be done in the floating-point or integer domain
* Handling division by zero is unimportant; program can crash or do anything if that arises.
* It's OK to assume that all the tokens are space-separated, including the paren tokens. 

## Sample input (caret prompt for clarity only):
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


# Goal:
The goal is to get running code. You're looking for signal about how they approach a coding problem, even more than an algorithmic problem. What do they do when they (inevitably) make a mistake? Do they have good debugging techniques or good ways of preventing errors? Do they document/use invariants? Do they use logging for debugging or use the IDE debugger? Are they hopeless?

