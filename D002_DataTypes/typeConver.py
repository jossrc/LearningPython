## 01

num_char = len( input("What's your name? ") )

print( type(num_char) ) # <class 'int'>

str_num_char = str(num_char) # string <- int

print("Your name has " + str_num_char + " characters.")

## 02

decimal = float(123)
print( (type(decimal) ) ) # <class 'float'>

print(70 + float("100.5")) # 170.5

print(str(70) + str(100)) # 70100