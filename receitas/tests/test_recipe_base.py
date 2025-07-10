from django.test import TestCase
from receitas.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name = 'user',
            last_name = 'name',
            username = 'username',
            password = '123456',
            email = 'username@email.com',
            
        )
        recipe = Recipe.objects.create(
            category =category,
            author = author,
            title = 'Receita Title',
            description = 'Receita Description',
            slug = 'recita-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porçoes',
            preparation_step_is_html = False,
            is_published = True,


        )
        return super().setUp()