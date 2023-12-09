import stuffs
import re
import time


food_nutrient_check = {'carbs':"moderate" or "high", 'protein':"high", 'fats':"low", 'vitamin_A':"low", 'vitamin_C':"low", 'calcium':"low", 'iron':"low"}

topping_nutrient_check = ['moderate', 'high']

count = 0

#find several potential instances of the food or topping entered by the user if not found
def food_finder(key, food, food_or):
    found = []
    dict_keys = list(key.keys())
    for f in dict_keys:
        pattern = re.compile(rf"{food}.+", re.IGNORECASE)
        finder = pattern.search(f) 
        if not finder == None:
            found.append(finder.group())
    if len(found) == 0:
        print(f"sorry we found 0 instances of {food} in our inventory")
    else:
        for i in range(len(found)):
            print(f"{i+1}. {found[i]}")
        print(f"these are what we found available, is your {food_or} found here")
        answer=input()
        if answer == 'no':
            print(":) Byebye")
        else:
            print(f"Please, type in the index for the {food_or} of choice")
            topin_index = int(input())
            return found[topin_index-1]

#check the nutrient intake for the food the user entered
def evaluate_fnutrient_intake(food):
        initial_count = 0
        for n_key, n_value in food_nutrient_check.items():
            for key, value in stuffs.nutrient_info[food].items():
                if n_key == key:
                    if n_value == value:
                       initial_count+=1
                    else:
                        initial_count+=0
        return initial_count

#check the nutrient intake for the topping the user entered
def evaluate_tnutrient_intake(topping):
    initial_count = 0 
    if stuffs.toppings_nutrients[topping] == topping_nutrient_check[0] or stuffs.toppings_nutrients[topping] == topping_nutrient_check[1]:
        initial_count+=1
    else:
        initial_count+=0
    return initial_count

#find out how many times the user ate and ise that info to evaluate the calorie and nutrient intake
eaten_food = 0
total_food = int(input("How many times did you eat today??  "))

for i in range(total_food):
    print(f"what is the number {i+1} meal: ", end=" ")
    food = input()
    food_qnty = input("was it a full plate, half plate, almost full plate or quater plate of food - ")
    any_topping = input(f"only {food}??  ")
    if any_topping.lower() == 'no':
        add_topping = input("add topping ")
    else:
        add_topin = None
    
    if food not in stuffs.plate_info[food_qnty].keys():
        found_food = food_finder(stuffs.plate_info[food_qnty], food, "food")
        eaten_food+=stuffs.plate_info[food_qnty][found_food]
        grade_num = evaluate_fnutrient_intake(found_food)
        if grade_num > 0:
            count+=grade_num
            

    else:
        eaten_food+=stuffs.plate_info[food_qnty][food]
        grade_num = evaluate_fnutrient_intake(food)
        if grade_num > 0:
            count+=grade_num
    if not add_topping == None:
        if add_topping not in stuffs.toppings_calories.keys():
            found_topping = food_finder(stuffs.toppings_calories, add_topping,"toppings")
            eaten_food+=stuffs.toppings_calories[found_topping]
            grade_num = evaluate_tnutrient_intake(found_topping)
            if grade_num > 0:
                count+=grade_num

        else:
            eaten_food+=stuffs.toppings_calories[add_topping]
            grade_num=evaluate_tnutrient_intake(add_topping)
            if grade_num > 0:
                count+=grade_num

if count >= 8:
    print("You're not doing too badly :) ")
else:
    print("You're not eating well :( ")


time.sleep(2)
print()
print()
if eaten_food >= 2000 and eaten_food <= 2500:
    print("Well Done!!!")
    print(f"your calorie deficit is around {eaten_food} calories")
elif eaten_food < 2000:
    print(f"But it seems you're not eating enough, but keeping going you're at {eaten_food} calories, just a little more to get to 2000 calories a day")
elif eaten_food > 2500:
    print(f"But woah slow down, you eaten way too much, try to eat less")
    print(f"I mean you're at {eaten_food} calories, that's too much")



   

