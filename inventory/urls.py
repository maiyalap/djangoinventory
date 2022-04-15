from django.urls import path
from .views import *


urlpatterns = [
    path('',HomePage, name='home-page'),
    path('login/',LoginPage, name='login-page'),
    path('instock/',InstockPage, name='instock-page'),
    path('showitem/',ShowItemPage, name='showitem-page'),    
    path('outstock/',OutstockPage, name='outstock-page'),
    path('about/',AboutPage, name='about-page')

]
