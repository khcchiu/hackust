from django.shortcuts import render
from django.http import HttpResponse

from main.forms import *
import os
import subprocess
import json

# Create your views here.
def home(request):
    return render(request, 'home.html', {

    })

def analysis(request):
    if request.POST:
        form = AnalysisForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('dataset') == '1':
                result = []
                locations = ['Towngas Cooking Centre', '三星台菜食堂 Tristar Kitchen', 'C.P.U. Cafe', 'Mini Friday', 'InterContinental Hong Kong', '東寶小館 Tung Po Kitchen']
                for file in sorted([f for f in os.listdir('./main/images/sample') if not f.startswith('.')]):
                    command = "./main/inference.py -image './main/images/sample/{}'".format(file)
                    print(command)
                    out = subprocess.check_output(command, shell=True)
                    result.append((str(out))[2:-3])
                print('final output', result)
                json_data = json.dumps([{'food_category': food_category, 'location': location} for food_category, location in zip(result, locations)])
                analysis = Analysis(result=json_data)
                analysis.save()
            if form.cleaned_data.get('dataset') == '2':
                json_data = [{"food_category": "hot_and_sour_soup"}, {"food_category": "Egg_Tart"}, {"food_category": "Pork_liver"}, {"food_category": "ice_cream"}, {"food_category": "hummus"}, {"food_category": "spaghetti_bolognese"}, {"food_category": "baby_back_ribs"}, {"food_category": "sashimi"}, {"food_category": "hummus"}, {"food_category": "spaghetti_carbonara"}, {"food_category": "Fried_chicken_drumsticks"}, {"food_category": "hot_and_sour_soup"}, {"food_category": "apple_pie"}, {"food_category": "macarons"}, {"food_category": "grilled_salmon"}, {"food_category": "fried_calamari"}, {"food_category": "Ice_cream"}, {"food_category": "churros"}, {"food_category": "takoyaki"}, {"food_category": "spaghetti_bolognese"}, {"food_category": "tuna_tartare"}, {"food_category": "donuts"}, {"food_category": "Steamed_Fish_Head_with_Diced_Hot_Red_Peppers"}, {"food_category": "chicken_curry"}, {"food_category": "frozen_yogurt"}, {"food_category": "crab_cakes"}, {"food_category": "macarons"}, {"food_category": "chicken_curry"}, {"food_category": "ice_cream"}, {"food_category": "paella"}, {"food_category": "ice_cream"}, {"food_category": "ramen"}, {"food_category": "shrimp_and_grits"}, {"food_category": "french_fries"}, {"food_category": "ice_cream"}, {"food_category": "White_fungus_soup"}, {"food_category": "hummus"}, {"food_category": "Sauteed_Shredded_Pork_in_Sweet_Bean_Sauce"}, {"food_category": "baby_back_ribs"}, {"food_category": "apple_pie"}, {"food_category": "Roast_pork"}, {"food_category": "huevos_rancheros"}, {"food_category": "grilled_cheese_sandwich"}, {"food_category": "pho"}, {"food_category": "ice_cream"}, {"food_category": "Biscuits"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Pork_ribs_soup_with_radish"}, {"food_category": "macarons"}, {"food_category": "Poached_Egg"}, {"food_category": "ice_cream"}, {"food_category": "Sauteed_bean_sprouts"}, {"food_category": "deviled_eggs"}, {"food_category": "ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Egg_pudding"}, {"food_category": "spring_rolls"}, {"food_category": "Dumplings"}, {"food_category": "seaweed_salad"}, {"food_category": "ice_cream"}, {"food_category": "chocolate_mousse"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "foie_gras"}, {"food_category": "hamburger"}, {"food_category": "Ice_cream"}, {"food_category": "ramen"}, {"food_category": "takoyaki"}, {"food_category": "ramen"}, {"food_category": "cup_cakes"}, {"food_category": "Fruit_salad"}, {"food_category": "strawberry_shortcake"}, {"food_category": "Saute_Spicy_Chicken"}, {"food_category": "bread_pudding"}, {"food_category": "Egg_pudding"}, {"food_category": "sushi"}, {"food_category": "grilled_salmon"}, {"food_category": "donuts"}, {"food_category": "grilled_salmon"}, {"food_category": "chicken_curry"}, {"food_category": "pork_chop"}, {"food_category": "macarons"}, {"food_category": "beef_tartare"}, {"food_category": "churros"}, {"food_category": "chocolate_cake"}, {"food_category": "frozen_yogurt"}, {"food_category": "pho"}, {"food_category": "hamburger"}, {"food_category": "greek_salad"}, {"food_category": "hot_dog"}, {"food_category": "hamburger"}, {"food_category": "bread_pudding"}, {"food_category": "panna_cotta"}, {"food_category": "cup_cakes"}, {"food_category": "gnocchi"}, {"food_category": "cup_cakes"}, {"food_category": "chocolate_mousse"}, {"food_category": "ice_cream"}, {"food_category": "peking_duck"}, {"food_category": "cannoli"}, {"food_category": "Ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "Peanut"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "clam_chowder"}, {"food_category": "peking_duck"}, {"food_category": "ice_cream"}, {"food_category": "steak"}, {"food_category": "Ice_cream"}, {"food_category": "oysters"}, {"food_category": "deviled_eggs"}, {"food_category": "apple_pie"}, {"food_category": "ice_cream"}, {"food_category": "scallops"}, {"food_category": "poutine"}, {"food_category": "foie_gras"}, {"food_category": "frozen_yogurt"}, {"food_category": "sushi"}, {"food_category": "dumplings"}, {"food_category": "foie_gras"}, {"food_category": "sashimi"}, {"food_category": "oysters"}, {"food_category": "ice_cream"}, {"food_category": "hot_and_sour_soup"}, {"food_category": "Boiled_Fish_with_Picked_Cabbage_and_Chili"}, {"food_category": "Spicy_Chicken"}, {"food_category": "bibimbap"}, {"food_category": "caprese_salad"}, {"food_category": "hot_dog"}, {"food_category": "Cold_noodles"}, {"food_category": "Ice_cream"}, {"food_category": "chocolate_mousse"}, {"food_category": "Ice_cream"}, {"food_category": "hummus"}, {"food_category": "Biscuits"}, {"food_category": "filet_mignon"}, {"food_category": "ice_cream"}, {"food_category": "falafel"}, {"food_category": "poutine"}, {"food_category": "Ice_cream"}, {"food_category": "dumplings"}, {"food_category": "hummus"}, {"food_category": "ramen"}, {"food_category": "escargots"}, {"food_category": "Pork_ribs_soup_with_radish"}, {"food_category": "hummus"}, {"food_category": "lobster_bisque"}, {"food_category": "fried_rice_noodles"}, {"food_category": "foie_gras"}, {"food_category": "bread_pudding"}, {"food_category": "bread_pudding"}, {"food_category": "sushi"}, {"food_category": "Egg_pie_cake"}, {"food_category": "shrimp_and_grits"}, {"food_category": "Steamed_Fish_Head_with_Diced_Hot_Red_Peppers"}, {"food_category": "deviled_eggs"}, {"food_category": "garlic_bread"}, {"food_category": "beignets"}, {"food_category": "Beer_duck"}, {"food_category": "Saute_Spicy_Chicken"}, {"food_category": "beet_salad"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "macarons"}, {"food_category": "Dumplings"}, {"food_category": "Boiled_Shredded_pork_in_chili_oil"}, {"food_category": "Pork_ribs_soup_with_radish"}, {"food_category": "Fruit_salad"}, {"food_category": "Minced_Pork_Congee_with_Preserved_Egg"}, {"food_category": "Spicy_crayfish"}, {"food_category": "Ice_cream"}, {"food_category": "foie_gras"}, {"food_category": "Mapo_Tofu"}, {"food_category": "caesar_salad"}, {"food_category": "ramen"}, {"food_category": "garlic_bread"}, {"food_category": "breakfast_burrito"}, {"food_category": "Ice_cream"}, {"food_category": "cheese_plate"}, {"food_category": "ramen"}, {"food_category": "pho"}, {"food_category": "macarons"}, {"food_category": "frozen_yogurt"}, {"food_category": "paella"}, {"food_category": "garlic_bread"}, {"food_category": "Egg_pudding"}, {"food_category": "foie_gras"}, {"food_category": "ramen"}, {"food_category": "pho"}, {"food_category": "Egg_pudding"}, {"food_category": "chicken_curry"}, {"food_category": "peking_duck"}, {"food_category": "oysters"}, {"food_category": "pho"}, {"food_category": "churros"}, {"food_category": "chocolate_cake"}, {"food_category": "frozen_yogurt"}, {"food_category": "Steamed_bun_with_purple_potato_and_pumpkin"}, {"food_category": "beignets"}, {"food_category": "Ice_cream"}, {"food_category": "pulled_pork_sandwich"}, {"food_category": "Ice_cream"}, {"food_category": "chicken_curry"}, {"food_category": "ice_cream"}, {"food_category": "ramen"}, {"food_category": "ice_cream"}, {"food_category": "risotto"}, {"food_category": "ramen"}, {"food_category": "Ice_cream"}, {"food_category": "foie_gras"}, {"food_category": "Grilled_fish"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Steamed_pork_with_rice_powder"}, {"food_category": "cannoli"}, {"food_category": "cheesecake"}, {"food_category": "Steamed_egg_custard"}, {"food_category": "Lamb_shashlik"}, {"food_category": "ramen"}, {"food_category": "Egg_pudding"}, {"food_category": "chocolate_cake"}, {"food_category": "hummus"}, {"food_category": "sashimi"}, {"food_category": "nachos"}, {"food_category": "lobster_bisque"}, {"food_category": "ceviche"}, {"food_category": "ice_cream"}, {"food_category": "hummus"}, {"food_category": "pancakes"}, {"food_category": "ice_cream"}, {"food_category": "tiramisu"}, {"food_category": "huevos_rancheros"}, {"food_category": "fried_rice"}, {"food_category": "croque_madame"}, {"food_category": "Steamed_Perch"}, {"food_category": "foie_gras"}, {"food_category": "ice_cream"}, {"food_category": "donuts"}, {"food_category": "chocolate_mousse"}, {"food_category": "Rice_porridge"}, {"food_category": "hummus"}, {"food_category": "cannoli"}]
            if form.cleaned_data.get('dataset') == '3':
                result = []
                for file in sorted([f for f in os.listdir('./main/images/all') if not f.startswith('.')]):
                    command = "./main/inference.py -image './main/images/all/{}'".format(file)
                    print(command)
                    out = subprocess.check_output(command, shell=True)
                    result.append((str(out))[2:-3])
                print('final output', result)
                json_data = json.dumps([{'food_category': category} for category in result])
                analysis = Analysis(result=json_data)
                analysis.save()
            print(json_data)
            return render(request, 'analysis_result.html', {
                'json_data': json_data,
            })

    else:
        form = AnalysisForm()
    return render(request, 'analysis.html', {
        'form': form,
    })

def shift(request):
    pass