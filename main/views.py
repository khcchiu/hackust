from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import EmailMessage

from main.forms import *
import os
import subprocess
import json
import pycronofy
import random

cronofy = pycronofy.Client(access_token="7HIwG8LSBfGbVNRszgbxUu1d8-nfJMo_")
calendar_id = 'cal_XLIvcZop-QDHVc4X_3FfAQIl3bLzzNsG4uuW1yA'

# Create your views here.
def home(request):
    return render(request, 'home.html', {

    })

def hr(request):
    return render(request, 'hr.html', {

    })

def analysis(request):
    if request.POST:
        form = AnalysisForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('dataset') == '1':
                result = []
                #locations = ['Towngas Cooking Centre', '三星台菜食堂 Tristar Kitchen', 'C.P.U. Cafe', 'Mini Friday', 'InterContinental Hong Kong', '東寶小館 Tung Po Kitchen']
                for file in sorted([f for f in os.listdir('./main/images/sample') if not f.startswith('.')]):
                    command = "./main/inference.py -image './main/images/sample/{}'".format(file)
                    print(command)
                    out = subprocess.check_output(command, shell=True)
                    result.append((str(out))[2:-3])
                print('final output', result)
                #json_data = json.dumps([{'food_category': food_category, 'location': location} for food_category, location in zip(result, locations)])
                json_data = json.dumps([{'food_category': food_category} for food_category in result])
                analysis = Analysis(result=json_data)
                analysis.save()
            if form.cleaned_data.get('dataset') == '2':
                json_data = [{"food_category": "hot_and_sour_soup"}, {"food_category": "Egg_Tart"}, {"food_category": "Pork_liver"}, {"food_category": "ice_cream"}, {"food_category": "hummus"}, {"food_category": "spaghetti_bolognese"}, {"food_category": "baby_back_ribs"}, {"food_category": "sashimi"}, {"food_category": "hummus"}, {"food_category": "spaghetti_carbonara"}, {"food_category": "Fried_chicken_drumsticks"}, {"food_category": "hot_and_sour_soup"}, {"food_category": "apple_pie"}, {"food_category": "macarons"}, {"food_category": "grilled_salmon"}, {"food_category": "fried_calamari"}, {"food_category": "Ice_cream"}, {"food_category": "churros"}, {"food_category": "takoyaki"}, {"food_category": "spaghetti_bolognese"}, {"food_category": "tuna_tartare"}, {"food_category": "donuts"}, {"food_category": "Steamed_Fish_Head_with_Diced_Hot_Red_Peppers"}, {"food_category": "chicken_curry"}, {"food_category": "frozen_yogurt"}, {"food_category": "crab_cakes"}, {"food_category": "macarons"}, {"food_category": "chicken_curry"}, {"food_category": "ice_cream"}, {"food_category": "paella"}, {"food_category": "ice_cream"}, {"food_category": "ramen"}, {"food_category": "shrimp_and_grits"}, {"food_category": "french_fries"}, {"food_category": "ice_cream"}, {"food_category": "White_fungus_soup"}, {"food_category": "hummus"}, {"food_category": "Sauteed_Shredded_Pork_in_Sweet_Bean_Sauce"}, {"food_category": "baby_back_ribs"}, {"food_category": "apple_pie"}, {"food_category": "Roast_pork"}, {"food_category": "huevos_rancheros"}, {"food_category": "grilled_cheese_sandwich"}, {"food_category": "pho"}, {"food_category": "ice_cream"}, {"food_category": "Biscuits"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Pork_ribs_soup_with_radish"}, {"food_category": "macarons"}, {"food_category": "Poached_Egg"}, {"food_category": "ice_cream"}, {"food_category": "Sauteed_bean_sprouts"}, {"food_category": "deviled_eggs"}, {"food_category": "ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Egg_pudding"}, {"food_category": "spring_rolls"}, {"food_category": "Dumplings"}, {"food_category": "seaweed_salad"}, {"food_category": "ice_cream"}, {"food_category": "chocolate_mousse"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "foie_gras"}, {"food_category": "hamburger"}, {"food_category": "Ice_cream"}, {"food_category": "ramen"}, {"food_category": "takoyaki"}, {"food_category": "ramen"}, {"food_category": "cup_cakes"}, {"food_category": "Fruit_salad"}, {"food_category": "strawberry_shortcake"}, {"food_category": "Saute_Spicy_Chicken"}, {"food_category": "bread_pudding"}, {"food_category": "Egg_pudding"}, {"food_category": "sushi"}, {"food_category": "grilled_salmon"}, {"food_category": "donuts"}, {"food_category": "grilled_salmon"}, {"food_category": "chicken_curry"}, {"food_category": "pork_chop"}, {"food_category": "macarons"}, {"food_category": "beef_tartare"}, {"food_category": "churros"}, {"food_category": "chocolate_cake"}, {"food_category": "frozen_yogurt"}, {"food_category": "pho"}, {"food_category": "hamburger"}, {"food_category": "greek_salad"}, {"food_category": "hot_dog"}, {"food_category": "hamburger"}, {"food_category": "bread_pudding"}, {"food_category": "panna_cotta"}, {"food_category": "cup_cakes"}, {"food_category": "gnocchi"}, {"food_category": "cup_cakes"}, {"food_category": "chocolate_mousse"}, {"food_category": "ice_cream"}, {"food_category": "peking_duck"}, {"food_category": "cannoli"}, {"food_category": "Ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "Peanut"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "clam_chowder"}, {"food_category": "peking_duck"}, {"food_category": "ice_cream"}, {"food_category": "steak"}, {"food_category": "Ice_cream"}, {"food_category": "oysters"}, {"food_category": "deviled_eggs"}, {"food_category": "apple_pie"}, {"food_category": "ice_cream"}, {"food_category": "scallops"}, {"food_category": "poutine"}, {"food_category": "foie_gras"}, {"food_category": "frozen_yogurt"}, {"food_category": "sushi"}, {"food_category": "dumplings"}, {"food_category": "foie_gras"}, {"food_category": "sashimi"}, {"food_category": "oysters"}, {"food_category": "ice_cream"}, {"food_category": "hot_and_sour_soup"}, {"food_category": "Boiled_Fish_with_Picked_Cabbage_and_Chili"}, {"food_category": "Spicy_Chicken"}, {"food_category": "bibimbap"}, {"food_category": "caprese_salad"}, {"food_category": "hot_dog"}, {"food_category": "Cold_noodles"}, {"food_category": "Ice_cream"}, {"food_category": "chocolate_mousse"}, {"food_category": "Ice_cream"}, {"food_category": "hummus"}, {"food_category": "Biscuits"}, {"food_category": "filet_mignon"}, {"food_category": "ice_cream"}, {"food_category": "falafel"}, {"food_category": "poutine"}, {"food_category": "Ice_cream"}, {"food_category": "dumplings"}, {"food_category": "hummus"}, {"food_category": "ramen"}, {"food_category": "escargots"}, {"food_category": "Pork_ribs_soup_with_radish"}, {"food_category": "hummus"}, {"food_category": "lobster_bisque"}, {"food_category": "fried_rice_noodles"}, {"food_category": "foie_gras"}, {"food_category": "bread_pudding"}, {"food_category": "bread_pudding"}, {"food_category": "sushi"}, {"food_category": "Egg_pie_cake"}, {"food_category": "shrimp_and_grits"}, {"food_category": "Steamed_Fish_Head_with_Diced_Hot_Red_Peppers"}, {"food_category": "deviled_eggs"}, {"food_category": "garlic_bread"}, {"food_category": "beignets"}, {"food_category": "Beer_duck"}, {"food_category": "Saute_Spicy_Chicken"}, {"food_category": "beet_salad"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "macarons"}, {"food_category": "Dumplings"}, {"food_category": "Boiled_Shredded_pork_in_chili_oil"}, {"food_category": "Pork_ribs_soup_with_radish"}, {"food_category": "Fruit_salad"}, {"food_category": "Minced_Pork_Congee_with_Preserved_Egg"}, {"food_category": "Spicy_crayfish"}, {"food_category": "Ice_cream"}, {"food_category": "foie_gras"}, {"food_category": "Mapo_Tofu"}, {"food_category": "caesar_salad"}, {"food_category": "ramen"}, {"food_category": "garlic_bread"}, {"food_category": "breakfast_burrito"}, {"food_category": "Ice_cream"}, {"food_category": "cheese_plate"}, {"food_category": "ramen"}, {"food_category": "pho"}, {"food_category": "macarons"}, {"food_category": "frozen_yogurt"}, {"food_category": "paella"}, {"food_category": "garlic_bread"}, {"food_category": "Egg_pudding"}, {"food_category": "foie_gras"}, {"food_category": "ramen"}, {"food_category": "pho"}, {"food_category": "Egg_pudding"}, {"food_category": "chicken_curry"}, {"food_category": "peking_duck"}, {"food_category": "oysters"}, {"food_category": "pho"}, {"food_category": "churros"}, {"food_category": "chocolate_cake"}, {"food_category": "frozen_yogurt"}, {"food_category": "Steamed_bun_with_purple_potato_and_pumpkin"}, {"food_category": "beignets"}, {"food_category": "Ice_cream"}, {"food_category": "pulled_pork_sandwich"}, {"food_category": "Ice_cream"}, {"food_category": "chicken_curry"}, {"food_category": "ice_cream"}, {"food_category": "ramen"}, {"food_category": "ice_cream"}, {"food_category": "risotto"}, {"food_category": "ramen"}, {"food_category": "Ice_cream"}, {"food_category": "foie_gras"}, {"food_category": "Grilled_fish"}, {"food_category": "ice_cream"}, {"food_category": "ice_cream"}, {"food_category": "Ice_cream"}, {"food_category": "Steamed_pork_with_rice_powder"}, {"food_category": "cannoli"}, {"food_category": "cheesecake"}, {"food_category": "Steamed_egg_custard"}, {"food_category": "Lamb_shashlik"}, {"food_category": "ramen"}, {"food_category": "Egg_pudding"}, {"food_category": "chocolate_cake"}, {"food_category": "hummus"}, {"food_category": "sashimi"}, {"food_category": "nachos"}, {"food_category": "lobster_bisque"}, {"food_category": "ceviche"}, {"food_category": "ice_cream"}, {"food_category": "hummus"}, {"food_category": "pancakes"}, {"food_category": "ice_cream"}, {"food_category": "tiramisu"}, {"food_category": "huevos_rancheros"}, {"food_category": "fried_rice"}, {"food_category": "croque_madame"}, {"food_category": "Steamed_Perch"}, {"food_category": "foie_gras"}, {"food_category": "ice_cream"}, {"food_category": "donuts"}, {"food_category": "chocolate_mousse"}, {"food_category": "Rice_porridge"}, {"food_category": "hummus"}, {"food_category": "cannoli"}]
                result = ['hot_and_sour_soup', 'Egg_Tart', 'Pork_liver', 'ice_cream', 'hummus', 'spaghetti_bolognese', 'baby_back_ribs', 'sashimi', 'hummus', 'spaghetti_carbonara', 'Fried_chicken_drumsticks', 'hot_and_sour_soup', 'apple_pie', 'macarons', 'grilled_salmon', 'fried_calamari', 'Ice_cream', 'churros', 'takoyaki', 'spaghetti_bolognese', 'tuna_tartare', 'donuts', 'Steamed_Fish_Head_with_Diced_Hot_Red_Peppers', 'chicken_curry', 'frozen_yogurt', 'crab_cakes', 'macarons', 'chicken_curry', 'ice_cream', 'paella', 'ice_cream', 'ramen', 'shrimp_and_grits', 'french_fries', 'ice_cream', 'White_fungus_soup', 'hummus', 'Sauteed_Shredded_Pork_in_Sweet_Bean_Sauce', 'baby_back_ribs', 'apple_pie', 'Roast_pork', 'huevos_rancheros', 'grilled_cheese_sandwich', 'pho', 'ice_cream', 'Biscuits', 'Ice_cream', 'Ice_cream', 'Ice_cream', 'Pork_ribs_soup_with_radish', 'macarons', 'Poached_Egg', 'ice_cream', 'Sauteed_bean_sprouts', 'deviled_eggs', 'ice_cream', 'Ice_cream', 'Ice_cream', 'Egg_pudding', 'spring_rolls', 'Dumplings', 'seaweed_salad', 'ice_cream', 'chocolate_mousse', 'Ice_cream', 'Ice_cream', 'Ice_cream', 'Ice_cream', 'foie_gras', 'hamburger', 'Ice_cream', 'ramen', 'takoyaki', 'ramen', 'cup_cakes', 'Fruit_salad', 'strawberry_shortcake', 'Saute_Spicy_Chicken', 'bread_pudding', 'Egg_pudding', 'sushi', 'grilled_salmon', 'donuts', 'grilled_salmon', 'chicken_curry', 'pork_chop', 'macarons', 'beef_tartare', 'churros', 'chocolate_cake', 'frozen_yogurt', 'pho', 'hamburger', 'greek_salad', 'hot_dog', 'hamburger', 'bread_pudding', 'panna_cotta', 'cup_cakes', 'gnocchi', 'cup_cakes', 'chocolate_mousse', 'ice_cream', 'peking_duck', 'cannoli', 'Ice_cream', 'ice_cream', 'Peanut', 'ice_cream', 'ice_cream', 'ice_cream', 'clam_chowder', 'peking_duck', 'ice_cream', 'steak', 'Ice_cream', 'oysters', 'deviled_eggs', 'apple_pie', 'ice_cream', 'scallops', 'poutine', 'foie_gras', 'frozen_yogurt', 'sushi', 'dumplings', 'foie_gras', 'sashimi', 'oysters', 'ice_cream', 'hot_and_sour_soup', 'Boiled_Fish_with_Picked_Cabbage_and_Chili', 'Spicy_Chicken', 'bibimbap', 'caprese_salad', 'hot_dog', 'Cold_noodles', 'Ice_cream', 'chocolate_mousse', 'Ice_cream', 'hummus', 'Biscuits', 'filet_mignon', 'ice_cream', 'falafel', 'poutine', 'Ice_cream', 'dumplings', 'hummus', 'ramen', 'escargots', 'Pork_ribs_soup_with_radish', 'hummus', 'lobster_bisque', 'fried_rice_noodles', 'foie_gras', 'bread_pudding', 'bread_pudding', 'sushi', 'Egg_pie_cake', 'shrimp_and_grits', 'Steamed_Fish_Head_with_Diced_Hot_Red_Peppers', 'deviled_eggs', 'garlic_bread', 'beignets', 'Beer_duck', 'Saute_Spicy_Chicken', 'beet_salad', 'ice_cream', 'ice_cream', 'macarons', 'Dumplings', 'Boiled_Shredded_pork_in_chili_oil', 'Pork_ribs_soup_with_radish', 'Fruit_salad', 'Minced_Pork_Congee_with_Preserved_Egg', 'Spicy_crayfish', 'Ice_cream', 'foie_gras', 'Mapo_Tofu', 'caesar_salad', 'ramen', 'garlic_bread', 'breakfast_burrito', 'Ice_cream', 'cheese_plate', 'ramen', 'pho', 'macarons', 'frozen_yogurt', 'paella', 'garlic_bread', 'Egg_pudding', 'foie_gras', 'ramen', 'pho', 'Egg_pudding', 'chicken_curry', 'peking_duck', 'oysters', 'pho', 'churros', 'chocolate_cake', 'frozen_yogurt', 'Steamed_bun_with_purple_potato_and_pumpkin', 'beignets', 'Ice_cream', 'pulled_pork_sandwich', 'Ice_cream', 'chicken_curry', 'ice_cream', 'ramen', 'ice_cream', 'risotto', 'ramen', 'Ice_cream', 'foie_gras', 'Grilled_fish', 'ice_cream', 'ice_cream', 'Ice_cream', 'Steamed_pork_with_rice_powder', 'cannoli', 'cheesecake', 'Steamed_egg_custard', 'Lamb_shashlik', 'ramen', 'Egg_pudding', 'chocolate_cake', 'hummus', 'sashimi', 'nachos', 'lobster_bisque', 'ceviche', 'ice_cream', 'hummus', 'pancakes', 'ice_cream', 'tiramisu', 'huevos_rancheros', 'fried_rice', 'croque_madame', 'Steamed_Perch', 'foie_gras', 'ice_cream', 'donuts', 'chocolate_mousse', 'Rice_porridge', 'hummus', 'cannoli']
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
                'dataset': form.cleaned_data.get('dataset'),
                'json_data': json_data,
                'result': json.dumps(result)
            })

    else:
        form = AnalysisForm()
    return render(request, 'analysis.html', {
        'form': form,
    })

def shift(request):
    """
    events = cronofy.read_events(
        from_date='2019-04-14',
        to_date='2019-04-19',
        tzid='Etc/UTC')
    print(events)
    calendars = cronofy.list_calendars()
    print(calendars)
    event = {
        'event_id': "qTtZdczOccgaPncGJaCiLg",
        'summary': "Board meeting",
        'description': "Discuss plans for the next quarter.",
        'start': "2019-04-14T15:30:00Z",
        'end': "2019-04-14T17:00:00Z",
        'tzid': "Asia/Singapore",
        'location': {
            'description': "Board room"
        }
    }
    cronofy.upsert_event(calendar_id=calendar_id, event=event)
    """
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = {}
            event['event_id'] = str(timezone.now())
            event['start'] = str(form.cleaned_data['start']).replace(' ', 'T', 1).replace('+00:00', 'Z', 1)
            print(str(form.cleaned_data['start']).replace(' ', 'T', 1))
            event['end'] = str(form.cleaned_data['end']).replace(' ', 'T', 1).replace('+00:00', 'Z', 1)
            print(str(form.cleaned_data['end']).replace('+00:00', 'Z', 1))
            event['summary'] =  form.cleaned_data['staff']
            event['description'] = 'Allocated time'
            event['tzid'] = 'Asia/Singapore'
            print(event)
            cronofy.upsert_event(calendar_id=calendar_id, event=event)
            mail_subject = 'Your allocated shift.'
            message = 'Here is your allocated time for work:\nStart: ' + event['start'].replace('T', ' ', 1).replace('+08:00', '', 1) + '\nEnd: ' + event['end'].replace('T', '', 1).replace('+08:00', '', 1)
            to_email = 'kennethchiuhc@gmail.com'
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
    else:
        form = EventForm()
    return render(request, 'shift.html', {
        'form': form,
    })

def availability_rule(request):
    return render(request, 'availability_rule.html')

def availability_viewer(request):
    return render(request, 'availability_viewer.html')

import networkx as nx
from networkx.algorithms import community
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import math
import time

import io
import urllib, base64

def food_delivery(request):

    class Vec2f():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    #food order class
    class FoodOrder():
        def __init__(self, orderID, x, y, orderTime):
            self.orderID = orderID
            self.groupID = -1
            #self.address
            self.pos = Vec2f(x, y)
            self.orderTime = orderTime
            #self.remainTime = time + 30min

        def printinfo(self):
            print(self.orderID, self.groupID, self.pos.x, self.pos.y, time.strftime("%b %d %a %H:%M:%S", time.localtime(self.orderTime)))


    center = Vec2f(0, 0)
    foodOrders = []
    G = nx.Graph()
    #add center
    G.add_node(0, id=-1)
    #adj matrix
    distMatrix = np.array([[0]])#[0]#numpy

    def getVec2fDistance(v1, v2):
        return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

    def getNodeDistance(i, j): #center: < 0 #to check
        #google map dist?
        i -= 1
        j -= 1

        if (i < -1 or i >= len(foodOrders) or j < -1 or j >= len(foodOrders)):
            print("getNodeDistance: invalid index")
            return None
        if i == -1:
            return getVec2fDistance(center, foodOrders[j].pos)
        if j == -1:
            return getVec2fDistance(center, foodOrders[i].pos)
        return getVec2fDistance(foodOrders[i].pos, foodOrders[j].pos)

    def addFoodOrder(orderID, x, y, orderTime):
        foodOrders.append(FoodOrder(orderID, x, y, orderTime))

        nonlocal distMatrix

        length = distMatrix.shape[0] + 1
        distMatrix = np.append(distMatrix, np.zeros((length-1, 1)), axis=1)
        distMatrix = np.append(distMatrix, np.zeros((1, length)), axis=0)

        for i in range(length):
            d = getNodeDistance(i, length-1)
            distMatrix.itemset((i, length-1), d)
            distMatrix.itemset((length-1, i), d)

    def constructPos():
        nodePos = np.zeros((len(foodOrders)+1, 2))
        nodePos[0] = [center.x, center.y]

        for i in range(len(foodOrders)):
            nodePos[i + 1] = [foodOrders[i].pos.x, foodOrders[i].pos.y]

        return nodePos

    def constructGraph():
        G = nx.Graph()
        nodePos = {}

        G.add_node(0, label="center")
        nodePos[0] = (center.x, center.y)
        for i in range(len(foodOrders)):
            G.add_node(i+1, label=foodOrders[i].orderID)
            nodePos[i+1] = (foodOrders[i].pos.x, foodOrders[i].pos.y)

        [G.add_edge(i, j, weight=distMatrix[i, j]) for i in range(0, distMatrix.shape[1]) for j in range(i+1, distMatrix.shape[1])]

        return G, nodePos

    addFoodOrder(123, 3, 8, time.time())
    addFoodOrder(223, 12, 6, time.time())
    addFoodOrder(133, -3, -3, time.time())
    addFoodOrder(104, 4, 17, time.time())
    addFoodOrder(225, 6, 0, time.time())
    addFoodOrder(346, 10, 4, time.time())
    addFoodOrder(117, -1, 2, time.time())
    addFoodOrder(128, -2, 7, time.time())
    addFoodOrder(169, -4, 1, time.time())

    for i in range(10, 11):
        addFoodOrder(random.randint(100, 300), random.randint(-5,5), random.randint(-5,5), time.time())

    nodePos = constructPos()

    kmeans = KMeans(n_clusters=3, random_state=0).fit(nodePos[1:, :])
    color = np.concatenate(([0], kmeans.labels_ + 1))


    def draw():
        plt.figure(figsize=(10,10))

        G, nodePos = constructGraph()

        nx.draw_networkx_nodes(G, nodePos, node_color=color, node_size=1000, alpha=0.6)
        nx.draw_networkx_edges(G, nodePos, alpha=0.1)
        nx.draw_networkx_labels(G, nodePos, labels=nx.get_node_attributes(G, "label"))

        plt.axis('off')

        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())

        uri = 'data:image/png;base64,' + urllib.parse.quote(string)
        html = '<img src=" %s " height="600px" />' % uri

        return html

    html = draw()

    return render(request, 'delivery.html', {
        'img': html
    })
