## Fitness and Health Calculators
## view readme for info about this project!

# # BMI Calculator
unit_chosen = input('Will you be using metric, or imperial units?')
if unit_chosen == 'metric':
    height = input('Please enter your height in cm')
    weight = input('Please enter your weight in kg')
    h = float(height) / 100
    w = float(weight)
    bmi = w/h**2
elif unit_chosen == 'imperial':
    height = input ('Please enter your height, feet and inches separated by a space')
    height = height.split()
    height_in_inches = (float(height[0]) * 12) + float(height[1])
    weight = input ('Please enter your weight in lbs')
    h = height_in_inches
    w = float(weight)
    bmi = (w/(h**2)) * 703
else:
    print("Please restart the program and use a valid unit.")
   

print("Your BMI is ", bmi, ".")
if bmi < 18.5:
    print ("You are underweight. Eat more.")
elif 18.5 <= bmi < 24.9:
    print ("You are at a healthy weight. Keep it up!")
elif 25 <= bmi < 29.9:
    print ("You are slightly overweight. You could shed a little weight mate, but don't sweat it!")
elif 30 <= bmi < 34.9:
    print ("You are obese. Lose some weight!")
elif 35 <= bmi < 39.9:
    print ("You are severely obese. Get some help, but you can do this!")
elif bmi>= 40:
    print ("Alright you're super fat. But you can do this. Nothing is impossible!")

# # Water Intake Calculator

unit_chosen = input('Will you be using metric, or imperial units?')
if unit_chosen == 'metric':
    weight = input('Please enter your weight in kg ')
    w = float(weight)
    water_base  = w * 35 
    sport_per_day = input('How many hours of sport do you do per day?')
    sport_hours = float(sport_per_day)
    water_from_sport = sport_hours*750
    water_total = water_base + (water_from_sport)   
    print ("You need to drink ", water_total, "ml of water per day.")
elif unit_chosen == 'imperial':
    weight = input ('Please enter your weight in lbs') 
    w = float(weight)
    water_base = w/2.20462 *35
    sport_per_day = input('How many hours of sport do you do per day?')
    sport_hours = float(sport_per_day)
    water_from_sport = sport_hours*750
    water_total = water_base + (water_from_sport)
    water_total_ounces = round((water_total/29.574),1)
    print ("You need to drink ", water_total_ounces, "ounces of water per day.")

else:
    print("Please restart the program and use a valid unit.")

# Protein and Carb Intake Calculator

# The Protein Intake Calculator estimates the amount of protein a person needs to eat per day. Based on current body weight and training goal,
# a recommendation is given for how many grams of protein to eat in total each day.


unit_chosen = input('Will you be using metric, or imperial units?')
if unit_chosen == 'metric':
    weight = input('Please enter your weight in kg ')
    w = float(weight)
    goal_chosen = input('What is your goal? Enter "1" for build muscle, enter "2" for improve endurance, or enter "3" for balanced nutrition.')
    if goal_chosen == "1":
        protein = w*1.5
    elif goal_chosen == "2":
        protein = w*1.2
    elif goal_chosen == "3":
        protein = w
    print ("You should eat approximately", protein, " grams of protein per day.")
elif unit_chosen == 'imperial':
    weight = input ('Please enter your weight in lbs') 
    goal_chosen = input('What is your goal? Enter "1" for build muscle, enter "2" for improve endurance, or enter "3" for balanced nutrition.')
    w = float(weight)
    protein = 0
    if goal_chosen == "1":
        protein = round(w/(220.462/150),1)
    elif goal_chosen == "2":
        protein = round(w/(220.462/120),1)
    elif goal_chosen == "3":
        protein = round(w/(220.462/100),1)
    print ("You should eat", protein, "grams of protein per day.")

# # Ideal Heart Rate Calculator

age = input('How old are you?')
age = float(age)
max_heart_rate = 220 - age
target_heart_rate = round(max_heart_rate * .85,0)
print ("Your target heart rate when working out is", target_heart_rate, "." " Your maximum heart rate is", max_heart_rate, ".")


## Carb Calculator

unit_chosen = input('Will you be using metric, or imperial units?')
if unit_chosen == 'metric':
    weight = input('Please enter your weight in kg ')
    activity_level = input ('How active are you? Enter "1" if you exercise 0-1 day per week, "2" for 2-3 days per week, "3" for 4-5 days per week, or "4" for 6-7 days per week.')
    w = float(weight)
    carbs = 0
    if activity_level == "1":
        carbs = w*4
    elif activity_level == "2":
        carbs = w*6
    elif activity_level == '3':
        carbs = w*8
    elif activity_level == '4':
        carbs = w*10
    print ("You should eat approximately ", carbs, " grams of carbs per day.")
elif unit_chosen == 'imperial':
    weight = input ('Please enter your weight in lbs') 
    activity_level = input ('How active are you? Enter "1" if you exercise 0-1 day per week, "2" for 2-3 days per week, "3" for 4-5 days per week, or "4" for 6-7 days per week.')
    w = float(weight)
    carbs = 0
    if activity_level == "1":
        carbs = w*round((400/220.462),1)
    elif activity_level == "2":
        carbs = w*round((600/220.462),1)
    elif activity_level == '3':
        carbs = w*round((800/220.462),1)
    elif activity_level == '4':
        carbs = w*round((1000/220.462),1)
    print ("You should eat", carbs, "grams of carbs per day.")

## Basal Metabolic Rate and Total Daily Energy Expenditure Calculator

unit_chosen = input('Will you be using metric, or imperial units?')
if unit_chosen == 'metric':
     weight = input('Please enter your weight in kg ')
     height = input('Please enter your height in cm')
     gender = input('What is your gender? Enter "F" for Female, and "M" for Male')
     activity_level = input ('How active are you? Enter "1" if you exercise 0-1 day per week, "2" for 2-3 days per week, "3" for 4-5 days per week, or "4" for 6-7 days per week.')
     age = input('How old are you?')
     w = float(weight)
     h = float(height)
     a = float(age)
     bmr = 0
     tdee = 0
     if gender == "M":
         bmr = 66 + (13.7*w) + (5*h) - (6.7*a)
         if activity_level == "1":
             tdee = bmr * 1.4
         elif activity_level == "2":
             tdee = bmr * 1.6
         elif activity_level == "3":
             tdee = bmr * 1.8
         elif activity_level == "4":
             tdee = bmr * 2
     elif gender == "F":
        bmr = 655 + (9.5*w) + (1.85*h) - (4.6*a)
        if activity_level == "1":
             tdee = bmr * 1.4
        elif activity_level == "2":
             tdee = bmr * 1.6
        elif activity_level == "3":
             tdee = bmr * 1.8
        elif activity_level == "4":
             tdee = bmr * 2
if unit_chosen == 'imperial':
    weight = input('Please enter your weight in lb')
    height = input ('Please enter your height, feet and inches separated by a space')
    gender = input('What is your gender? Enter "F" for Female, and "M" for Male')
    activity_level = input ('How active are you? Enter "1" if you exercise 0-1 day per week, "2" for 2-3 days per week, "3" for 4-5 days per week, or "4" for 6-7 days per week.')
    age = input('How old are you?')
    w = float(weight)
    height_split = height.split()
    height_in_inches = (float(height_split[0]) * 12) + float(height_split[1])
    h = float(height_in_inches)
    a = float(age)
    bmr = 0
    tdee = 0
    if gender == "M":
         bmr = 66 + (13.7*(w/2.20462)) + (5*(h*2.54)) - (6.7*a)
         if activity_level == "1":
             tdee = bmr * 1.4
         elif activity_level == "2":
             tdee = bmr * 1.6
         elif activity_level == "3":
             tdee = bmr * 1.8
         elif activity_level == "4":
             tdee = bmr * 2
    elif gender == "F":
        bmr = 655 + (9.5*(w/2.20462)) + (1.85*(h*2.54)) - (4.6*a)
        if activity_level == "1":
             tdee = bmr * 1.4
        elif activity_level == "2":
             tdee = bmr * 1.6
        elif activity_level == "3":
             tdee = bmr * 1.8
        elif activity_level == "4":
             tdee = bmr * 2
print ("Your Basal Metabolic Rate is", round(bmr,0), "and your Total Daily Energy Expenditure is", round(tdee,0),".")
