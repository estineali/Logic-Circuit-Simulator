'''
WELCOME TO THE SOURCE CODE FILE OF THE LOGIC CIRCUIT SIMULATOR
DATA STRUCTURES AND ALGORITHMS PROJECT - SPRING 2018
HABIB UNIVERSITY 

	>HASHIM ABBAS
	>BILAL MOHIUDDIN
	>MUHAMMAD SHAHROM ALI

THE CODE IS READABLE AND USER FRIENDLY.

RUN THE CODE. 
'''

#Modules
import turtle
import math

#Functions

#Logic Gates - each function takes a list(s) of binary inputs, performs the relevant function all the inputs and returns the resulting list

def and_gate(a,b):
    return [1 if a[i] == 1 and b[i] == 1 else 0 for i in range(len(a))]

def or_gate(a,b):
    return [0 if a[i] == 0 and b[i] == 0 else 1 for i in range(len(a))]

def not_gate(a):
    return [1 if i == 0 else 0 for i in a]


#Turtle Drawings of Gates

# Specifying the Pen size - psiz, pen color - pclr, pen speed - pspd, and background color - pbgc 
psiz,pclr,pspd,pbgc = 1.5,'white',0,'navy blue'

def OR(pos,n=1):
    orT = turtle.Turtle()
    
    # Specifying the Pen size - psiz, pen color - pclr, pen speed - pspd
    orT.speed(pspd)
    orT.pencolor(pclr)
    orT.pensize(psiz)
    
    a = pos
    orT.pu()
    orT.goto(pos)
    orT.pd()
    orT.lt(45)
    
    #side arc
    for i in range(90):
        if i == 30:
            x = orT.pos()
        elif i == 60:
            y = orT.pos()
        orT.lt(1)
        orT.fd(n*1)
    orT.rt(130)
    count = 0
    
    # top arc
    for i in range(50):
        orT.rt(1)
        count+=1
        orT.fd(n*2.25)
    orT.pu()
    orT.setpos(a)
    orT.lt(count-8)
    orT.pd()
    
    #bottom arc
    for i in range(50):
        orT.lt(1)
        orT.fd(n*2.25)
    orT.rt(47)
    orT.fd(n*50)
    
    p = orT.pos()
    # orT.reset()
    orT.ht()

    #x and y are the coordinates of the gates inputs whereas p is the coordinates of the output of the gate
    return x,y,p

def AND(pos,n=1):
    andT=turtle.Turtle()
    
    # Specifying the Pen size - psiz, pen color - pclr, pen speed - pspd
    andT.speed(pspd)
    andT.pencolor(pclr)
    andT.pensize(psiz)
    
    andT.pu()
    andT.goto(pos)
    andT.pd()
    andT.lt(90)
    
    #half of the vertical line
    andT.fd(25*n)
    y = andT.pos()
    andT.fd(25*n)
    andT.rt(90)
    
    #the arc
    andT.fd(100*n)
    andT.circle(-50*n,180)
    andT.fd(100*n)
    andT.rt(90)
    
    #the other half of the vertical line
    andT.fd(25*n)
    x = andT.pos()
    andT.fd(25*n)
    andT.penup()
    andT.rt(90)
    andT.fd(150*n)
    andT.pendown()
    andT.fd(50*n)
    andT.ht()
    p = andT.pos()
    # andT.reset()
    andT.ht()

    #x and y are the coordinates of the gates inputs whereas p is the coordinates of the output of the gate
    return x,y,p

def NOT(pos,n=1):
    notT = turtle.Turtle()
    
    # Specifying the Pen size - psiz, pen color - pclr, pen speed - pspd
    notT.pencolor(pclr)
    notT.pensize(psiz)
    notT.speed(pspd)
    
    notT.pu()
    notT.goto(pos)
    notT.pd()
    
    #the triangle
    notT.lt(90)
    notT.fd(50*n)
    notT.rt(120)
    notT.fd(100*n)
    notT.rt(120)
    notT.fd(100*n)
    notT.rt(120)
    notT.fd(50*n)
    notT.rt(90)
    
    #the not bubble
    notT.penup()
    notT.fd(100*math.sin((math.pi)/3)*n)
    notT.pendown()
    notT.lt(90)
    notT.circle(-9*n)
    notT.rt(90)
    notT.pu()
    notT.fd(18*n)
    notT.pd()
    
    notT.fd(30*n)
    p = notT.pos()
    # notT.reset()
    notT.ht()

    #p is the coordinates of the output of the gate
    return p

#Operations

def remove_spaces(x):
    r = ''
    for i in x:
        if i != ' ':
            r += i
    return r

def testing_notation(expression):
    #check for empty input
    if len(expression) == 0:
        print("\nLogic: It seems you're not the talkative type. I'll let you try again...\n")
        return False
    
    #check for end command
    if expression == 'end':
    	return True
    
    #screening the expression for any possible characters that would cause an error
    legit_symbols = ['*', '+', '~', '(', ')', '[',']']
    for character in expression:
        if character not in legit_symbols:
            if character.isalpha() == False:
                print('\nLogic: Incorrect Notation.', character, 'is invalid. Please enter input in the correct format.\n' )
                return False
            
    #check for incorrect notation
    for i in range(len(expression)):
    	if i != len(expression)-1:
    		if expression[i].isalpha() and expression[i+1].isalpha():
    			print('\nLogic: Incorrect notation. No operation between', str(expression[i]),'and', str(expression[i+1]),'Please enter input in the correct format.\n')
    			return False
    		    
    #checks for balanced parantheses
    x = list(expression)
    if x.count('(') != x.count(')'):
    	print('\nLogic: Incorrect Notation. Unbalanced parentheses. Please enter input in the correct format.\n')
    	return False
    lstexp = []
    for i in expression:
        if i == "(" or i == ")":
            lstexp += i
    if len(lstexp)%2 != 0:
        print('\nLogic: Incorrect Notation. Unbalanced parentheses. Please enter input in the correct format.\n')
        return False
    if len(lstexp) > 0 and lstexp[0] == ')':
        print('\nLogic: Incorrect Notation. Unbalanced parentheses. Please enter input in the correct format.\n')
        return False
    if len(lstexp) > 0 and lstexp[-1] == '(':
        print('\nLogic: Incorrect Notation. Unbalanced parentheses. Please enter input in the correct format.\n')
        return False
    stack = []
    for i in lstexp:
        if i == "(":
            stack.append(i)
        elif len(stack) != 0 and i == ")" and stack[-1] == '(':
            stack.pop(-1)
    if len(stack) != 0:
        print('\nLogic: Incorrect Notation. Unbalanced parentheses. Please enter input in the correct format.\n')
        return False
    
    #check if there are variables in the expression or not
    novar= True
    for i in x:
        if i.isalpha():
            novar = False
    if novar == True:
        print('\nLogic: Incorrect Notation. Please enter input in the correct format.\n')
        return False
    return True

def binary_input(x):
    var = []
    #list of variables
    [var.append(i) for i in x if i.isalpha() and i  not in var]
    
    #list of binary values according to number of variables
    values = [bin(i)[2:].rjust(len(var),'0')for i in range(2**len(var))]
    
    #a list of values for each variable
    inputs = [[int(j[i])for j in values] for i in range(len(var))]
    
    #a dictionary with a variable as key and a value as a list of binary inputs
    varbin = dict(zip(var,inputs))
    
    return varbin

def infixtopostfix(x):
    a, r, not_var, not_group = [], '', False, False
    op = ['+', '*', '(', ')', '~']
    #the checks not_var and not_group are there to apply DeMorgans laws to the circuit to simplify it
    for i in x:
        
        #for variables (A). If not_var is True the variable is not (~A)
        if i not in op:
            if not_var == True:
                r += '~' + i
            else:
                r += i
            if not_group == True:
                not_var = True
            else: not_var = False
            
        # the presence of the not symbol controls the not checks
        elif i == '~':
            if not_var == True:
                not_var = False
            else: not_var = True
            
        # handles brackets
        elif i == '(':
            if not_var == True:
                not_group = True
            else: not_group = False
            a.append(i)
            
        elif i == ')':
                while a[-1] != '(':
                    r += a.pop()
                a.pop()
                if not_group == True:
                    not_group = False
                    not_var = False
                    
        # + has a lower precendence than *. If not_ group is True + becomes *. 
        elif i == '+':
            if a:
                while a[-1] == '*':
                    r += a.pop()
                    if not a: break
            if not_group == True:
                a.append('*')
            else:
                a.append(i)
                
        # If not_ group is True + becomes *
        elif i == '*':
            if a:
                while a[-1] != '(':
                    r += a.pop()
                    if not a: break
            if not_group == True:
                a.append('+')
            else:
                a.append(i)
                
    #appends whatever is left in the stack
    if a:
        for i in a:
            r += i
    return r

def postfixeval(x):
  a, no = [], False
  val = binary_input(x)
  for i in x:
    if i in val:
        if no == False:
            a.append(val[i])
        else:
            # puts the value through a not gate
            a.append(not_gate(val[i]))
            no = False
    else:
        
      #checks for the not symbol
      if i == '~':
          no = True
          
      #sends top two values in stack through an OR gate.
      elif i == '+':
          r = or_gate(a.pop(),a.pop())
          a.append(r)
          
      #sends top two values in stack through an OR gate.
      elif i == '*':
          r = and_gate(a.pop(), a.pop())
          a.append(r)
          
  #returns final value        
  return a[0]

def logic_circuit_creator(x,n=1):
  a, no = [], False
  val = binary_input(x)
  tot = turtle.Turtle()
  #sets up the output window
  win_width, win_height, bg_color = 2000*(n+0.5), 2000*(n+0.5), 'black'
  turtle.setup(width = 1.0, height = 1.0)
  turtle.screensize(win_width, win_height, bg_color)
  #sets up the specifics of the output circuit
  turtle.bgcolor(pbgc)
  tot.pencolor(pclr)
  tot.pensize(psiz)
  tot.speed(pspd)
  tot.ht()
  #sets to starting position
  tot.pu()
  tot.setx(tot.pos()[0]-500)
  tot.sety(tot.pos()[1]+300)
  tot.pd()
  var = tot.pos()
  for i in x:
      
    #cretes a input line for and writes the name of each variable. Makes a NOT gate if it has a not attached to it.
    if i in val:
        tot.pu()
        tot.setpos(var)
        tot.pd()
        tot.write(i,font=('Arial',int(20*n),'normal'))
        tot.fd(100*n)
        g = tot.pos()
        if no == False:
            a.append(g)
        else:
            a.append(NOT(tot.pos(),0.5*n))
            no = False
            
        #sets the turtle to the next variables position
        tot.pu()
        tot.bk(100*n)
        tot.rt(90)
        tot.fd(100*n)
        tot.lt(90)
        tot.pd()
        var = tot.pos()
    else:
        if i == '~':
            no = True
            
        #connects two inputs to an OR gate
        elif i == '+':
            tot.pu()
            one, two = a.pop(),a.pop()
            if one[0] > two[0]: tot.goto(one)
            else: tot.goto(two)
            tot.goto((tot.pos()[0] + 200 * n, ((one[1] + two[1]) / 2) - 30 * n))
            d, e, f = OR(tot.pos(), n)
            tot.setpos(one)
            tot.pd()
            tot.setx(d[0]-30*n)
            tot.sety(d[1])
            tot.setx(d[0])
            tot.pu()
            tot.setpos(two)
            tot.pd()
            tot.setx(e[0]-30*n)
            tot.sety(e[1])
            tot.setx(e[0])
            a.append(f)
            
        #connects two inputs to an OR gate
        elif i == '*':
            tot.pu()
            one, two = a.pop(),a.pop()
            if one[0] > two[0]: tot.goto(one)
            else: tot.goto(two)
            tot.goto((tot.pos()[0] + 100 * n, ((one[1] + two[1]) / 2)))
            d, e, f = AND(tot.pos(), 0.8 * n)
            tot.setpos(one)
            tot.pd()
            tot.setx(d[0]-30*n)
            tot.sety(d[1])
            tot.setx(d[0])
            tot.pu()
            tot.setpos(two)
            tot.pd()
            tot.setx(e[0]-30*n)
            tot.sety(e[1])
            tot.setx(e[0])
            a.append(f)
            
  #labels the output line
  tot.pu()
  tot.goto(a[0])
  tot.pd()
  tot.write('X', font=('Arial', int(20 * n), 'normal'))

  #returns the evaluation of the expression
  return postfixeval(x)

def basic_simplify(x):
    #removes redundant not values from the expression 
    ex = []
    for i in list(x):
        if i == '~' and len(ex) > 0 and ex[-1] == '~':
            ex.pop()
        else:
            ex.append(i)
    x = ''.join(ex)
    
    #creates a list of variables and operators
    varsity = [] 
    ops =[]
    for i in x:
        if i not in varsity and i.isalpha():
            varsity.append(i)
        elif i not in ops and not i.isalpha():
            ops.append(i)
            
    #our code does not deal with not simplification other than DeMorgans
    if len(varsity) == 1:
            if '~' in ops:
                pass
            else:
                return varsity[0]
            
    #applies idempotent laws of boolean algebra
    if len(ops) == 1:
        a = list(x)
        for i in a:
            if i.isalpha() and a.count(i) > 1:
                while a.count(i) > 1:
                    a.remove(i)
                    a.remove(ops[0])
        return ''.join(a)
    
    return x

def spinal_cord():
    #asks for expression input
    x = input('Input your logic expression(or type end to exit): ').strip()
    x = remove_spaces(x)
    #checks if the expression is correct. If the input is 'end' the program is discontinued.
    while testing_notation(x) == False or x == '':
        x = input('Input your logic expression(or type end to exit): ')
    if x == 'end':
            print('\n-------------------------L O G I C-------------------------')
            return
        
    #simplifies the expression    
    x = basic_simplify(x)
    
    #converts the expression to postfix notation
    post = infixtopostfix(x)
    
    #creates a dictionary of values for the variables in the expression
    values = binary_input(post)
    
    #appends the result of the expression into the dictionary of values
    values['X'] = postfixeval(post)
    
    #formats the output to look like a table of values
    value_keys = [i for i in values]
    value_keys.remove('X')
    value_keys.sort()
    value_keys += ['X']
    print('\nTruthTable:')
    print(value_keys)
    for v in range(len(values[value_keys[0]])):
        d = []
        for i in value_keys:
            d.append(str(values[i][v]))
        print(d)
        
    #prompts the user if they wish to view the circuit diagram
    if input('\nDo you wish to see the circuit diagram for this expression? (Y/N): ') == 'Y':
        
        #asks for desired size of the circuit drawing. There is also a check in place to make sure a numeric value is entered.
        while True:
            try:
                size = eval(input('\nSpecify the size of your circuit (Best Results: 0.5 - 1): '))
            except:
                print('\nLogic: That is not a number...please try again.\n')
                continue
            break
        
        #creates the circuit
        logic_circuit_creator(post,size)

    print('\n-----------------------------L O G I C-----------------------------')
    
#the main function call
spinal_cord()
