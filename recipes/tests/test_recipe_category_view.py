# from unittest import skip
from django.urls import reverse, resolve
from recipes import views

from .test_recipe_base import RecipeTestBase


''' This will be the part responsible for 
orchestrating the view tests, 
showing whether everything is 
going as expected, including the 
page's error messages.'''


# @skip -> utilizado para pular tests

# Realizando teste das views para identificar se tem algum erro
class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

   # Testando Status 404
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1, )))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        # Check if one recipe exists
        self.assertIn(needed_title , content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        
        '''Test category is_published False dont show'''
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.category.id}))

        self.assertEqual(response.status_code, 404)
