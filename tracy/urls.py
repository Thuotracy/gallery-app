from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url(r'^location/(\d+)',views.location,name = 'location'),
    url(r'^search/',views.search,name='search')
]
