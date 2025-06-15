try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
# The code above is a simple example of exception handling in Python.
# It attempts to convert user input into an integer and calculate its reciprocal.