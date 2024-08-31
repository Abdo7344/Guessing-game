import random

# List of available meals
meals = [
    "Spaghetti Bolognese", "Chicken Curry", "Beef Stew",
    "Vegetable Stir Fry", "Tacos", "Grilled Cheese Sandwich",
    "Salmon with Asparagus", "Lentil Soup", "Pizza",
    "Baked Ziti", "Chicken Caesar Salad", "Beef Tacos",
    "Pasta Primavera", "Fish Tacos", "Vegetarian Chili"
]

def generate_meal_plan():
    """Generates a random meal plan for the week."""
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {}

    for day in days_of_week:
        meal_plan[day] = random.choice(meals)

    return meal_plan

def display_meal_plan(meal_plan):
    """Displays the meal plan."""
    print("Weekly Meal Plan:")
    for day, meal in meal_plan.items():
        print(f"{day}: {meal}")

# Generate and display the meal plan
weekly_meal_plan = generate_meal_plan()
display_meal_plan(weekly_meal_plan)
