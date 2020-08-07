from django.urls import path

from .views import home_view, fb_view

app_name = 'facebook'

urlpatterns = [
    path('', home_view, name='home_page'),
    path('fb', fb_view, name='fb_page'),
]