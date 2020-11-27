# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

LIVE = 90 # years

YEAR_DAYS = 365
YEAR_WEEKS = 52
YEAR_MONTHS = 12

DAYS_OF_LIVE = LIVE * YEAR_DAYS
WEEKS_OF_LIVE = LIVE * YEAR_WEEKS
MONTHS_OF_LIVE = LIVE * YEAR_MONTHS

myAge = int(age)

remainingYears = LIVE - myAge

remainingDays = YEAR_DAYS * remainingYears
remainingWeeks = YEAR_WEEKS * remainingYears
remainingMonths = YEAR_MONTHS * remainingYears

print(f'You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left')
