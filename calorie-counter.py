print("Today's Date?")
todays_date = input()

print("Breakfast calories?")
breafast_calories = int(input())

print("Lunch calories?")
lunch_calories = int(input())

print("Dinner calories?")
dinner_calories = int(input())

print("Snack calories?")
snack_calories = int(input())

calorie_content = breafast_calories + lunch_calories + dinner_calories + snack_calories
print("Calorie content for " + todays_date + ": " + str(calorie_content) + " calories!" )