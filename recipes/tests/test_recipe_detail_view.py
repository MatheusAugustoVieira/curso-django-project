# from unittest import skip
from django.urls import reverse, resolve
from recipes import views

from .test_recipe_base import RecipeTestBase


''' Aqui sera a parte responsavel por orquestrar os testes da views
mostrando se tudo esta indo de acordo ate nas mensagens de erro da pagina'''


# @skip -> utilizado para pular tests

# Realizando teste das views para identificar se tem algum erro
class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

   # Testando Status 404
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipes(self):
        needed_title = 'This is a detail page - It load one recipe'
        
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title , content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        
        '''Test category is_published False dont show'''
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))

        self.assertEqual(response.status_code, 404)