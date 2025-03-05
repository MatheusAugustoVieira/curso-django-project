from django.urls import path

from . import views


''' Essa sera a parte onde os usuarios irao colocar nas urls do seu navegador
para ter acesso a determinadas areas do site ou navegar pelo site mesmo,
qualquer alteracao feita na url pode acarretar em erro nos seus teste, porem 
as urls devem ser fixas para cada site'''

app_name = 'recipes'



urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),# Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/search/', lambda request: ..., name="search"),
]
