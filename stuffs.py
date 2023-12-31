plate_info = {
    "full plate": {
        "sushi": 700,
        "tacos": 600,
        "pizza": 1000,
        "curry": 700,
        "hamburger": 700,
        "dim sum": 500,
        "paella": 700,
        "falafel": 500,
        "kimchi": 75,
        "pierogi": 600,
        "pho": 500,
        "tagine": 700,
        "goulash": 700,
        "ceviche": 300,
        "moussaka": 600,
        "sashimi": 300,
        "chaat": 400,
        "poutine": 1000,
        "jollof rice": 400,
        "couscous": 500,
        "rice": 300,
        "bread": 225,
        "pasta": 300,
        "potatoes": 225,
        "chicken": 450,
        "fish": 300,
        "beef": 450,
        "vegetables": 100,
        "fruits": 100,
        "tomatoes": 45,
        "cheese": 300,
        "olive oil": 180,
        "soy products": 225,
        "spices": "negligible",
        "herbs": "negligible",
        "tea": "negligible",
        "coffee": "negligible",
        "chocolate": 225,
        "wheat": 300,
        "corn": 150,
    },
    "half plate": {
        "sushi": 350,
        "tacos": 300,
        "pizza": 500,
        "curry": 350,
        "hamburger": 350,
        "dim sum": 250,
        "paella": 350,
        "falafel": 250,
        "kimchi": 37.5,
        "pierogi": 300,
        "pho": 250,
        "tagine": 350,
        "goulash": 350,
        "ceviche": 150,
        "moussaka": 300,
        "sashimi": 150,
        "chaat": 200,
        "poutine": 500,
        "jollof rice": 200,
        "couscous": 250,
        "rice": 150,
        "bread": 112.5,
        "pasta": 150,
        "potatoes": 112.5,
        "chicken": 225,
        "fish": 150,
        "beef": 225,
        "vegetables": 50,
        "fruits": 50,
        "tomatoes": 22.5,
        "cheese": 150,
        "olive oil": 90,
        "soy products": 112.5,
        "spices": "negligible",
        "herbs": "negligible",
        "tea": "negligible",
        "coffee": "negligible",
        "chocolate": 112.5,
        "wheat": 150,
        "corn": 75,
    },
    "quarter plate": {
        "sushi": 175,
        "tacos": 150,
        "pizza": 250,
        "curry": 175,
        "hamburger": 175,
        "dim sum": 125,
        "paella": 175,
        "falafel": 125,
        "kimchi": 18.75,
        "pierogi": 150,
        "pho": 125,
        "tagine": 175,
        "goulash": 175,
        "ceviche": 75,
        "moussaka": 150,
        "sashimi": 75,
        "chaat": 100,
        "poutine": 250,
        "jollof rice": 100,
        "couscous": 125,
        "rice": 75,
        "bread": 56.25,
        "pasta": 75,
        "potatoes": 56.25,
        "chicken": 112.5,
        "fish": 75,
        "beef": 112.5,
        "vegetables": 25,
        "fruits": 25,
        "tomatoes": 11.25,
        "cheese": 75,
        "olive oil": 45,
        "soy products": 56.25,
        "spices": "negligible",
        "herbs": "negligible",
        "tea": "negligible",
        "coffee": "negligible",
        "chocolate": 56.25,
        "wheat": 75,
        "corn": 37.5,
    },
    "almost full plate": {
        "sushi": 600,
        "tacos": 500,
        "pizza": 800,
        "curry": 600,
        "hamburger": 600,
        "dim sum": 400,
        "paella": 600,
        "falafel": 400,
        "kimchi": 60,
        "pierogi": 500,
        "pho": 400,
        "tagine": 600,
        "goulash": 600,
        "ceviche": 225,
        "moussaka": 500,
        "sashimi": 225,
        "chaat": 325,
        "poutine": 800,
        "jollof rice": 325,
        "couscous": 400,
        "rice": 225,
        "bread": 168.75,
        "pasta": 225,
        "potatoes": 168.75,
        "chicken": 337.5,
        "fish": 225,
        "beef": 337.5,
        "vegetables": 75,
        "fruits": 75,
        "tomatoes": 33.75,
        "cheese": 225,
        "olive oil": 135,
        "soy products": 168.75,
        "spices": "negligible",
        "herbs": "negligible",
        "tea": "negligible",
        "coffee": "negligible",
        "chocolate": 168.75,
        "wheat": 225,
        "corn": 112.5,
    },
}


toppings_calories = {
    "butter": 100,
    "jam or jelly": 55,
    "cheese": 95,
    "avocado": 50,
    "tomato sauce": 25,
    "pesto": 90,
    "parmesan cheese": 25,
    "sour cream": 40,
    "chives": 1.5,
    "bacon bits": 45,
    "bbq sauce": 40,
    "lemon herb marinade": 15,
    "mushroom sauce": 25,
    "salsa": 15,
    "lemon butter sauce": 50,
    "tartar sauce": 60,
    "garlic aioli": 70,
    "mango salsa": 25,
    "caramelized onions": 35,
    "blue cheese": 35,
    "chimichurri sauce": 35,
    "hummus": 30,
    "balsamic glaze": 35,
    "ranch dressing": 85,
    "olive tapenade": 25,
    "yogurt": 22.5,
    "honey": 25,
    "nut butter": 95,
    "cottage cheese": 70,
    "mozzarella cheese": 75,
    "basil": 1.5,
    "balsamic reduction": 25,
    "olive oil": 120,
    "soy sauce": 12.5,
    "ginger": 7.5,
    "sesame seeds": 55,
    "green onions": 7.5,
    "various spice blends": "negligible",
    "salt and pepper": "negligible",
    "chili flakes": "negligible",
    "cumin": "negligible",
    "fresh basil": "negligible",
    "parsley": "negligible",
    "cilantro": "negligible",
    "dill": "negligible",
    "lemon": 4.5,
    "mint": 1.5,
    "ginger (fresh)": 2.5,
    "milk or cream": 25,
    "sugar or sweetener": 17.5,
    "cinnamon": 8,
    "whipped cream": 55,
    "nuts": 75,
    "fruit (strawberries, raspberries)": 15,
    "sea salt": "negligible",
    "caramel": 55,
    "crackers": 15,
    "grapes": 55,
    "fig jam": 55,
    "lemon": 4.5,
    "mint": 1.5,
    "ginger": 2.5,
    "milk or cream": 25,
    "sugar or sweetener": 17.5,
    "cinnamon": 8,
    "whipped cream": 55,
    "chicken wing": 203,
    "chicken drumstick": 172,
    "chicken breast": 165,
    "chicken thigh": 209,
    "chicken liver": 135,
    "beef steak": 250,
    "pork chop": 143,
    "salmon": 206,
    "shrimp": 99,
    "tofu": 144,
}

nutrient_info = {
    "sushi": {
        "carbs": "moderate",
        "proteins": "low",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "not present",
        "calcium": "low",
        "iron": "moderate",
    },
    "tacos": {
        "carbs": "low",
        "proteins": "moderate",
        "fats": "high",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "moderate",
        "iron": "high",
    },
    "pizza": {
        "carbs": "moderate",
        "proteins": "moderate",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "moderate",
        "iron": "moderate",
    },
    "curry": {
        # Add nutrient information for curry
        "carbs": "moderate",
        "proteins": "moderate",
        "fats": "moderate",
        "vitamin_A": "moderate",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
        },
    "hamburger": {
        "carbs": "moderate",
        "proteins": "high",
        "fats": "high",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "moderate",
        "iron": "moderate",
    },
    "dim sum": {
        "carbs": "moderate",
        "proteins": "moderate",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "low",
    },
    "paella": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "moderate",
        "vitamin_A": "moderate",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "falafel": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "kimchi": {
        "carbs": "low",
        "proteins": "low",
        "fats": "low",
        "vitamin_A": "high",
        "vitamin_C": "moderate",
        "calcium": "low",
        "iron": "low",
    },
    "pierogi": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
     "pho": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "moderate",
        "vitamin_C": "high",
        "calcium": "moderate",
        "iron": "low",
    },
    "tagine": {
        "carbs": "moderate",
        "proteins": "high",
        "fats": "moderate",
        "vitamin_A": "high",
        "vitamin_C": "moderate",
        "calcium": "low",
        "iron": "moderate",
    },
    "goulash": {
        "carbs": "low",
        "proteins": "high",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "ceviche": {
        "carbs": "low",
        "proteins": "high",
        "fats": "low",
        "vitamin_A": "moderate",
        "vitamin_C": "high",
        "calcium": "low",
        "iron": "low",
    },
    "moussaka": {
        "carbs": "moderate",
        "proteins": "moderate",
        "fats": "high",
        "vitamin_A": "moderate",
        "vitamin_C": "low",
        "calcium": "moderate",
        "iron": "moderate",
    },
    "sashimi": {
        "carbs": "low",
        "proteins": "high",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "low",
    },
    "chaat": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "moderate",
        "vitamin_C": "high",
        "calcium": "low",
        "iron": "low",
    },
    "poutine": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "high",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "moderate",
        "iron": "moderate",
    },
    "jollof rice": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "moderate",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "couscous": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "rice": {
        "carbs": "high",
        "proteins": "low",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "low",
    },
    "bread": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "pasta": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "potatoes": {
        "carbs": "high",
        "proteins": "low",
        "fats": "low",
        "vitamin_A": "moderate",
        "vitamin_C": "high",
        "calcium": "low",
        "iron": "moderate",
    },
    "chicken": {

        "carbs": "low",
        "proteins": "high",
        "fats": "moderate",
        "vitamin_A": "moderate",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "fish": {
        "carbs": "low",
        "proteins": "high",
        "fats": "moderate",
        "vitamin_A": "high",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "beef": {
        "carbs": "low",
        "proteins": "high",
        "fats": "high",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "high",
    },
     "vegetables": {
        "carbs": "low",
        "proteins": "low",
        "fats": "low",
        "vitamin_A": "high",
        "vitamin_C": "high",
        "calcium": "low",
        "iron": "low",
    },
    "fruits": {
        "carbs": "high",
        "proteins": "low",
        "fats": "low",
        "vitamin_A": "high",
        "vitamin_C": "high",
        "calcium": "low",
        "iron": "low",
    },
    "tomatoes": {
        "carbs": "low",
        "proteins": "low",
        "fats": "low",
        "vitamin_A": "high",
        "vitamin_C": "high",
        "calcium": "low",
        "iron": "low",
    },
    "cheese": {
        "carbs": "low",
        "proteins": "high",
        "fats": "high",
        "vitamin_A": "moderate",
        "vitamin_C": "low",
        "calcium": "high",
        "iron": "moderate",
    },
    "olive oil": {
        "carbs": "low",
        "proteins": "low",
        "fats": "high",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "low",
    },
    "soy products": {
        "carbs": "moderate",
        "proteins": "high",
        "fats": "moderate",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "moderate",
        "iron": "moderate",
    },
    "spices": "negligible",
    "herbs": "negligible",
    "tea": "negligible",
    "coffee": "negligible",

    "chocolate": {
        "carbs": "moderate",
        "proteins": "moderate",
        "fats": "high",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    },
    "wheat": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "high",
    },
    "corn": {
        "carbs": "high",
        "proteins": "moderate",
        "fats": "low",
        "vitamin_A": "low",
        "vitamin_C": "low",
        "calcium": "low",
        "iron": "moderate",
    }
}

toppings_nutrients = {
    "butter": "high",
    "jam or jelly": "moderate",
    "cheese": "moderate",
    "avocado": "moderate",
    "tomato sauce": "low",
    "pesto": "moderate",
    "parmesan cheese": "low",
    "sour cream": "moderate",
    "chives": "low",
    "bacon bits": "moderate",
    "bbq sauce": "moderate",
    "lemon herb marinade": "low",
    "mushroom sauce": "low",
    "salsa": "low",
    "lemon butter sauce": "moderate",
    "tartar sauce": "moderate",
    "garlic aioli": "moderate",
    "mango salsa": "low",
    "caramelized onions": "low",
    "blue cheese": "low",
    "chimichurri sauce": "low",
    "hummus": "low",
    "balsamic glaze": "low",
    "ranch dressing": "moderate",
    "olive tapenade": "low",
    "yogurt": "moderate",
    "honey": "low",
    "nut butter": "moderate",
    "cottage cheese": "moderate",
    "mozzarella cheese": "moderate",
    "basil": "low",
    "balsamic reduction": "low",
    "olive oil": "moderate",
    "soy sauce": "low",
    "ginger": "low",
    "sesame seeds": "moderate",
    "green onions": "low",
    "various spice blends": "not enough",
    "salt and pepper": "not enough",
    "chili flakes": "not enough",
    "cumin": "not enough",
    "fresh basil": "not enough",
    "parsley": "not enough",
    "cilantro": "not enough",
    "dill": "not enough",
    "lemon": "low",
    "mint": "low",
    "ginger (fresh)": "low",
    "milk or cream": "low",
    "sugar or sweetener": "low",
    "cinnamon": "low",
    "whipped cream": "moderate",
    "nuts": "moderate",
    "fruit (strawberries, raspberries)": "low",
    "sea salt": "not enough",
    "caramel": "moderate",
    "crackers": "low",
    "grapes": "moderate",
    "fig jam": "moderate",
    "chicken wing": "high",
    "chicken drumstick": "high",
    "chicken breast": "high",
    "chicken thigh": "high",
    "chicken liver": "high",
    "beef steak": "high",
    "pork chop": "moderate",
    "salmon": "high",
    "shrimp": "moderate",
    "tofu": "moderate",
}