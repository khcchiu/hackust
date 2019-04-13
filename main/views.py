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
            result = []
            locations = ['Towngas Cooking Centre', '三星台菜食堂 Tristar Kitchen', 'C.P.U. Cafe', 'Mini Friday', 'InterContinental Hong Kong', '東寶小館 Tung Po Kitchen']
            for file in sorted([f for f in os.listdir('./main/images') if not f.startswith('.')]):
                command = "./main/inference.py -image './main/images/{}'".format(file)
                print(command)
                out = subprocess.check_output(command, shell=True)
                result.append((str(out))[2:-3])
            print('final output', result)
            analysis = form.save(commit=False)
            analysis.location = form.cleaned_data.get('location')
            analysis.hashtag = form.cleaned_data.get('hashtag')
            json_data = json.dumps([{'food-category': food_category, 'location': location} for food_category, location in zip(result, locations)])
            print(json_data)
            analysis.result = json_data
            analysis.save()
            """
            return render(request, 'analysis_result.html', {
                'json_data': json_data,
            })
            """
            return HttpResponse(str(json_data))
    else:
        form = AnalysisForm()
    return render(request, 'analysis.html', {
        'form': form,
    })