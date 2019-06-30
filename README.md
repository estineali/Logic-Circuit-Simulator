# Logic Circuit Simulator


Welcome to the logic circuit simulator.
This is our project for CS102-Data Structures and Algorithms Spring'18

# TEAM MEMBERS:
    >Hashim Abbas
    >Bilal Mohiuddin
    >Muhammad Shahrom Ali

The software takes a logic expression as input evaluates it giving the truth-table output and the
circuit schematics. Please use brackets. ~A+~B+~C+~D*E is not the same as ~A+~B+~C+(~D*E). 

# Input format: 
    Parantheses to be used for precidence
    Donot use spaces as those are invalid 
    Code will screen for invalid notation and will not run. 
    > A*()+B is invalid notation 

Rest of the code is rather self explanatory. It's userfriendly and performs the task.


# Functions:
    >and_gate(a,b)
    >or_gate(a,b)
    >not_gate(a)
    >OR(pos, n=1)
    >AND(pos, n=1)
    >NOT(pos, n=1)
    >testing_notation(expression)
    >binary_input(x)
    >infixtopostfix(x)
    >postfixeval(x)
    >logic_circuit_creator(x, n=1)
    >basic_simplify(x)
    >spinal_cord()

# Function Description:
    # and_gate(a,b)
        The and_gate takes two lists. These are truth table inputs. And returns a list with all possible outputs after
        AND-ing them.
        For example:
            >>> c = [0, 0, 1, 1]
            >>> d = [0, 1, 0, 1]
            >>> and_gate(c, d)
            [0, 0, 0, 1]
# or_gate(a,b)
    The or_gate takes two lists. These are truth table inputs. And returns a list with all possible outputs after
    OR-ing them.
    For example:
        >>> c = [0, 0, 1, 1]
        >>> d = [0, 1, 0, 1]
        >>> or_gate(c, d)
        [0, 1, 1, 1]
# not_gate(a)
    Takes a list of possible values. Inverts all of them and returns a list of those inverted values
    For example:
        >>> n = [0, 1, 0, 1]
        >>> not_gate(n)
        [1, 0, 1, 0]
# OR(pos, n=1), AND(pos, n=1), NOT(pos, n=1)
    All of these are Turtle functions. They take th position, from where it needs to start, and an optional argument for
    their size, n. n is the factor by which the turtle graph will expand.

    These need not be called by the user. The program does all this by itself
# testing_notation(expression)
    Takes the expression as input and screens it for incorrect notation. If the notation is wrong, will show an error
    and will not process it.
    Correct notation includes:
        Capital Alphabets
        ~ for NOT
        + for OR
        * for AND
        parentheses
    For example:
        >>> testing_notation('(A*C)+~(~B+~D)')
        True
        >>>testing_notation('(A-C)+~(~B*~D)')
        Incorrect Notation. - is invalid
        False
# binary_input(x)
    Takes a logic expression as argument. Creates a truth-table containing possible values of all the variables. The size
    of the truth table varies according to the number of variables in the logic expression
    For example:
        >>> y = 'A'
        >>> binary_input(y)
        {'A': [0, 1]}
        >>> z = 'A+B'
        >>> binary_input(z)
        {'A': [0, 0, 1, 1], 'B': [0, 1, 0, 1]}
        >>> a = '~(A+B)*C'
        >>> binary_input(a)
        {'A': [0, 0, 0, 0, 1, 1, 1, 1], 'B': [0, 0, 1, 1, 0, 0, 1, 1], 'C': [0, 1, 0, 1, 0, 1, 0, 1]}
# infixtopostfix(x)
    Takes a logic expression as input and returns a post-fix version of that expression. Also applies De-Morgan's
    simplification
    For example:
        >>> infixtopostfix('A+B')
        AB+
        >>> infixtopostfix('(A*C)+~(~B*~D)')
        AC*BD++
# postfixeval(x)
    Takes a logic expression in postfix notation and returns the evaluation of that expression considering all possible
    values of the variables.
    For example:
        >>> m = AC*BD++
        >>> postfixeval(m)
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
# logic_circuit_creator(x, n=1)
    takes the logic expression as input. Draws the circuit diagram and returns the 
    truth table output for the expression.
# basic_simplify(x)
    takes an expression and removes redundancy. It is like the screening function. 
    Only this one applies some basic simplification like A+A+A+A+A becomes A only and 
    doesnot get printed as 5 A inputs OR-ed. 
# spinal_cord()
    This is the real deal. It ties all components together. Asks user for input and runs all required functions. This is the spinal cord of the program.
