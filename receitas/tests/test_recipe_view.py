# from django.test import TestCase
from django.urls import resolve,reverse
from receitas import views
# from receitas.models import Category, Recipe, User




class RecipeViewsTest(RecipeTestBase):
    

    def tearDown(self):
        return super().tearDown()


    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs= {'category_id' : 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs= {'id' : 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs= {'id' : 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'receitas/pages/home.html')
    
    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No Recipes found here :/</h1>', response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
       
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['receitas']
        self.assertIn('Receita Title', content)
        self.assertEqual(len(response_context_recipes), 1)
        pass    
        # self.assertEqual(response_recipes.first().title, 'Recipe Title')


    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs= {'id' : 1000}))
        self.assertEqual(response.status_code, 404)