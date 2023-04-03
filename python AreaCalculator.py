"""
Basic Area calculate
enter following into terminal to run: python AreaCalculator.py
"""

print "begin shenanigans"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Enter radius "))
  area = 3.14159 * radius**2
  print str(area)
  print "program is exiting"
elif option == "T":
  base = float(raw_input("Enter base"))
  height = float(raw_input("Enter height"))
  area = (0.5 * base) * height
  print str(area)
  print "program is exiting"
else:
  print "incorrect shape entered"
