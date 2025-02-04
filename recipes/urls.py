from django.urls import path
from recipes.views import *


urlpatterns = [
    path('', home), # Home
    path('sobre/', sobre),
    path('contato/', contato),
]
