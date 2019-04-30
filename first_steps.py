# Exercise 1
# Answers to questions that ask for non-code answers can simply be added as comments.

# 1) The following line causes a SyntaxError. Please correct the line so that it's output is 'Hallo Welt!' [1P]
print("Hallo Welt!")

# 2) Calculate the difference between a and b and assign the result to a variable called 'v_1'. What are the datatypes of a, b and 'v_1'? [2P]
a = 976.543
b = 345

v_1 = a - b

# 3) Calculate the remainder of the division 100/17 by only using one operator and save the result in v_2 (maybe the internet can help you) [1P]

v_2 = 100 % 17

# 4) The speed of light is about 300'000 km/s. What is the wavelength (in nanometers) of a light wave with a frequency of 5.0E+14 per second? 
#    Can we see this light? [4P]
#    If you don't know how to convert frequencies to wavelengths, the internet can help you!
#    Save the result in v_3.

# wavelength = speed of light / frequency
## speed of light in nanometers/s
c = 3.0E+12 #nm/s
## calculate v_3
f = 5.0E+14 #1/s
v_3 = c/f
## A: v_3 = 6.0E-3 nm; This means, that the radiation has the wavelength of X-rays. It is not visible.

# 5) Print the following string to the console using the format-function and the variables 'n' and 'pi': "Pi rounded to the first 10 decimals is: 3.1415926536" [2P]
n  = 10
pi = 3.14159265358979323846264338

print('Pi rounded to the first ', n, ' decimals is: ', "{0:11.10f}".format (pi))
# ------------------------------------
# - Don't change stuff below this line
# ------------------------------------

print(v_1)
print(v_2)
print(v_3)
