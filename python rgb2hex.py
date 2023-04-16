"""
RGB-HEX Converter
In this project, we’ll use Bitwise operators to build a calculator that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

We’ll add three methods to the project:

A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle
The program should do the following:

Prompt the user for the type of conversion they want
Ask the user to input the RGB or Hex value
Use Bitwise operators and shifting in order to convert the value
Print the converted value to the user

python rgb2hex.py

"""


def rgb_hex():
  invalid_msg = "error detected, deez are not the nutz you are looking for"
  
  red = int(raw_input("enter RED value: "))
  if (red < 0) or (red > 255):
    print invalid_msg
    return

  green = int(raw_input("enter GREEN value: "))
  if (green < 0) or (green > 255):
    print invalid_msg
    return

  blue = int(raw_input("enter BLUE value: "))
  if (blue < 0) or (blue > 255):
    print invalid_msg
    return

  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
  hex_val = raw_input("Input hexadecimal value (6 hex digits): ")
  if len(hex_val) != 6:
    print "invalid value was entered,"
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits

  print "Red: %s Green: %s Blue: %s" % (red, green, blue)

def convert():
  while  True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB to Hex..."
      rgb_hex()
    elif option == "2":
      print "HEX to RGB..."
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "ERROR 404deeznutz..."

convert()
