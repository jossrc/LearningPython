print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# TRUE

full = name1 + " " + name2

true_t = full.lower().count('t')
true_r = full.lower().count('r')
true_u = full.lower().count('u')
true_e = full.lower().count('e')


# LOVE
love_l = full.lower().count('l')
love_o = full.lower().count('o')
love_v = full.lower().count('v')
love_e = full.lower().count('e')

tot1 = true_t + true_r + true_u + true_e

tot2 = love_l + love_o + love_v + love_e

score = int(str(tot1) + str(tot2))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.\n")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.\n")
else:
  print(f"Your score is {score}.\n")
