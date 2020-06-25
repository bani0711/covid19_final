# chart/views.py
from django.shortcuts import render
from .models import Status
from django.db.models import Count, Q
import json

def home(request):
    return render(request, 'home.html')

def covid19(request):

    dataset = Status.objects \
        .values('date', 'country', 'confirmed') \
        .filter(Q(country='Korea, South'))

    dataset2 = Status.objects \
        .values('date', 'country', 'confirmed') \
        .filter(Q(country='China'))

    dataset3 = Status.objects \
        .values('date', 'country', 'confirmed') \
        .filter(Q(country='US'))

    dataset4 = Status.objects \
        .values('date', 'country', 'confirmed') \
        .filter(Q(country='France'))

    dataset5 = Status.objects \
        .values('date', 'country', 'confirmed') \
        .filter(Q(country='Italy'))

    xdataset = Status.objects \
        .values('date', 'country', 'confirmed') \
        .filter(Q(country='Korea, South'))

    categories = list()
    Korea_South_series_data = list()
    China_series_data = list()
    US_series_data = list()
    France_series_data = list()
    Italy_series_data = list()
    xAxis_data = list()

    for entry in dataset:
        Korea_South_series_data.append(entry['confirmed'])

    for entry in dataset2:
        China_series_data.append(entry['confirmed'])

    for entry in dataset3:
        US_series_data.append(entry['confirmed'])

    for entry in dataset4:
        France_series_data.append(entry['confirmed'])

    for entry in dataset5:
        Italy_series_data.append(entry['confirmed'])

    for entry in xdataset:
        xAxis_data.append(entry['date'])

    Korea_South_series = {
        'name': 'Korea, South',
        'data': Korea_South_series_data,
        'color': '#045275'
    }

    China_series = {
        'name': 'China',
        'data': China_series_data,
        'color': '#7CCBA2'
    }

    US_series = {
        'name': 'US',
        'data': US_series_data,
        'color': '#FCDE9C'
    }

    France_series = {
        'name': 'France',
        'data': France_series_data,
        'color': '#7C1D6F'
    }

    Italy_series = {
        'name': 'Italy',
        'data': Italy_series_data,
        'color': '#DC3977'
    }

    chart = {
        'chart': {'type': 'spline'},
        'title': {'text': 'COVID-19 확진자 발생율'},
        'xAxis': {'type': 'datetime', 'minTickInterval': 24 * 3600 * 1000},
        'plotOptions': {'spline': {'marker': {'enabled': 'false'}}},
        'series': [Korea_South_series, China_series, US_series, France_series, Italy_series],
    }
    dump = json.dumps(chart)

    return render(request, 'covid19.html', {'chart': dump})
