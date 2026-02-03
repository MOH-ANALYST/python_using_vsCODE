# String Manipulation
import math
name = 'Mustapha oladimeji hamzat'
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name[0:9])
print(name[0])
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(name.replace('h', 'H'))
print(name.split(' '))
first = 'oladimeji'
last = 'mustapha'
mail = '@hulluni.com'
full = (first[0] + '.' + last + mail)
print(full)

# Arithmetic Operations
x = 10 + 3
x += 3
print(x)
y = 10 - 3
y -= 3
print(y)
a = 10 * 3
print(a)
math.copysign(3, -2)
math.fabs(-7.5)

# String Slicing
fruits = 'apple'
print(fruits[1:-1])

# Conditional Statements
temp = 15
if temp > 30:
    print("It's a hot day")
elif temp < 10:
    print("It's a cold day")
print("Enjoy your day")

age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Ternary Operator
age = 70
message = "You are a minor" if age < 18 else "You are an adult"
print(message)

# logical operators
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
if has_high_income or has_good_credit:
    print("Eligible for loan")
if has_high_income and not has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

has_good_credit = True
has_high_income = False
teacher = False
if has_good_credit and has_high_income and teacher:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


has_good_credit = True
has_high_income = False
teacher = True
if (has_good_credit and has_high_income) and not teacher:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# short-circuit evaluation in python logcal operators are short-circuited, meaning that the second operand is evaluated only if necessary.

if 10 == '10':
    print('a')
elif 'bag' > 'apple' and 'bag' > 'cat':
    print('b')
else:
    print('c')

    # loops
    for number in range(1, 21, 4):
        print('scammer', 'stop', number, number * '$')

  # for else loop
congratulations = True
for number in range(3):
    print('attempt')
    if congratulations:
        print('congratulations you are IN')
        break
else:
    print('sorry you are OUT')

    # nested loops
for x in range(3):
    for y in range(3):
        print(f'({x},{y})')

# iterables
for item in 'python':
    print(item)
for item in ['mustapha', 'oladimeji', 'hamzat']:
    print(item)
for item in (1, 2, 3, 4):
    print(item)
shopping_cart = {'apple', 'banana', 'mango'}
for item in shopping_cart:
    print(item)
# while loop = 10
i = 10
while i >= 5:
    print(i)
    i -= 1


# excersice
# write a program displaying even numbers between 1 and 10 and print we have 4 even numbers
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f'we have {count} even numbers')

# def functions


def greet_user(first_name, last_name):
    print(f'hi {first_name} {last_name}')
    print('welcome aboard')


greet_user('mustapha', 'oladimeji')


def greet():
    print('hi there')
    print('welcome aboard')


greet()


# types of functions , 1. functions that perform a task and 2. functions that return a value.
def get_greet(first_name, last_name):
    return f'hi {first_name} {last_name}'


message = get_greet('mustapha', 'oladimeji')
print(message)
print(get_greet('oladimeji', 'hamzat'))

#keyword arguments
def increment(number, by):
    return number + by
result = increment(2, by=5)
print(result)
