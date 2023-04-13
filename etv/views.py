# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render


def index(request):
    return render(request, 'etv/home.html')


def quakes(request):
    all_quakes = Earthquake.objects.all
    damage = EarthquakeDamage.objects.all
    context = {'all_quakes': all_quakes, 'damage': damage}
    return render(request, 'etv/quake.html', context)


