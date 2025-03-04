from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import *

from recipes.models import Recipe

''' A parte das views sera onde ira mostrar o que cada pagina do site sera puxada e exibida ao usuario
podendo ser dados vindo diretamente do Data Base e gosto de comecar nas views antes de ir para a urls
ainda pretendo utilizar class based views'''

def home(request):
    recipes = Recipe.objects.filter(
            is_published=True,
            ).order_by('-id')
    
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
})


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
            ).order_by('-id')
        )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | ',
})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
})