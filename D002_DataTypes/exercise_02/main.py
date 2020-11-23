# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_as_float = float(height)
weight_as_int   = int(weight)

bmi = weight_as_int / (height_as_float**2)

bmi_as_int = int(bmi)

print(bmi_as_int)
