
counter = 0

while counter < 100:
    counter = counter + 1

print(counter)

stop = False
while not stop:
    # In this program, we input a number
    # check if the number is positive or
    # negative or zero and display
    # an appropriate message
    # This time we use nested if
    # NOTE: if code runner is installed, you will need to right click anywhere in the editor and choose:
    # "Run Python File in Terminal"
    user_input = input("Enter a number ('stop' to exit): ")
    if user_input.lower() == 'stop':
        stop = True
        break
    
    num = float(user_input)
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")
