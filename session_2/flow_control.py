if 'Vol Surface' < 'Volatility Surface':
    print("'Vol Surface' comes earlier than 'Volatility Surface'.")
else:
    print("'Vol Surface' comes later than 'Volatility Surface'.")


# In this program,
# we check if the number is positive or
# negative or zero and
# display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# The value of the expression depends on the condition checked.
print('Positive' if num > 0 else 'Not positive')


# Import the datetime system library and get today's date.
# Checking whether today is Sunday/Saturday or not.
import datetime
my_date = datetime.date.today()
print('Today: ', my_date)
print('Working day.' if my_date.weekday() < 5 else 'Weekend.')
