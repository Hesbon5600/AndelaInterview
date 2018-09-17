#####################Solving Santa's problem###################
'''houses = ["Kevo's house", "Dan's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)
'''
################ Calculating factorial of numbers Recursively###########
'''

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
    
number = input("Enter number to calculate factorial: \n" )

print("The factorial of ", number, " is ", str(factorial_recursive(int(number))))
'''
'''
##################Calculating sum recursively#################
#########passing the updated current state to each recursive call as arguments#########

def sum_recursive(current_number, accumulated_sum):
    # base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum
    
    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

sum = sum_recursive(1,0)
print (sum)
'''
##################Calculating sum recursively#################
'''
#################maintain the state by keeping it in global scope###############

# Global mutable state
number = int(input("Enter number to calculate sum: \n"))
current_number = 1
accumulated_sum = 0

def sum_recursive():
    global current_number
    global accumulated_sum
    global number
    #Base case

    if current_number == number + 1:
        return accumulated_sum

    #Recursive case

    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()

sum = sum_recursive()
print (sum)
'''

##############calculating the sum of all the elements of a list recursively#########
'''
def list_sum_recursively(input_list):
    # base case

    if input_list == []:
        return 0
    
    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself

    else:
        head = input_list[0]

        smaller_list = input_list[1:]
        return head + list_sum_recursively(smaller_list)
print(list_sum_recursively([10,20,30])) 
'''
############### recursive function to compute the nth Fibonacci number:###########
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end="\n")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
number = int(input("Enter number to calculate fibonacci \n"))

fibonacci_recursive(number)