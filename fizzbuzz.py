# add your code 
# Define the range of all numbers between 1 to 100.
for number in range(1,100):
    #when a number is easily divible by 3 or 5 without remainder, the FizzBuzz should be executed
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    # if the calculation doesn't meet any of the requirement above, then the number should be printed out
    else:
        print(number)

#end
