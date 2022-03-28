from django.urls import re_path
from . import views

urlpatterns=[
    re_path('^$',views.gallery,name = 'gallery'),
    re_path(r'^location/(\d+)',views.location,name = 'location'),
    re_path(r'^search/',views.search,name='search')
]
