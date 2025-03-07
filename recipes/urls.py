from django.urls import path

from . import views


'''This is where users will enter URLs into their browsers to access 
certain areas of the site or navigate the site itself. 
Any changes made to the URL may result in errors in your tests, but URLs should be fixed for each site.'''

app_name = 'recipes'



urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),# Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
