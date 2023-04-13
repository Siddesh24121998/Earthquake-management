# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.site_header = 'Earthquake Disasters Database Admin'

admin.site.register(Earthquake)
admin.site.register(EarthquakeDamage)
