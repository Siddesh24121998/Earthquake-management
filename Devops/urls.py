from django.urls import re_path as url
from django.contrib import admin
from etv import views as v1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', v1.index, name='home'),
    url(r'^quakes/', v1.quakes, name='quakes'),
    url(r'^$', v1.index, name='home'),
]

admin.site.site_url = '/home'
