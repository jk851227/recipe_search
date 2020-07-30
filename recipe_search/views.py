from django.shortcuts import render, redirect
import requests

def index(request):
    
    return render(request, 'index.html')

def food_list(request):
    url = 'https://api.spoonacular.com/recipes/findByIngredients?apiKey=ba2645667f5b40a3a7d42da11db66def&ingredients={}'
    ingredients = request.POST['ingredients']
    foods = requests.get(url.format(ingredients)).json()


    context = {
        'foods': foods
    }

    return render(request, 'food_list.html', context)

def recipe_info(request, food_id):
    url = 'https://api.spoonacular.com/recipes/{}/information?apiKey=ba2645667f5b40a3a7d42da11db66def&includeNutrition=false'
    recipe_info = requests.get(url.format(food_id)).json()

    all_ingredients = recipe_info['extendedIngredients']
    instructions = recipe_info['instructions']

    context = {
        'food': recipe_info,
        'all_ingredients': all_ingredients,
        'instructions': instructions
    }

    return render(request, 'recipe_info.html', context)

def random_meal(request):
    url = 'https://api.spoonacular.com/recipes/random?apiKey=ba2645667f5b40a3a7d42da11db66def&number=1'
    random_meal = requests.get(url).json()

    context = {
        'food': random_meal['recipes'][0]
    }

    return render(request, 'random_meal.html', context)