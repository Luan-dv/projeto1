from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.receitas.factory import make_recipe
from receitas.models import Recipe
from django.http import Http404
# from django.http import HttpResponse
# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'receitas' : recipes,
        
        # [make_recipe() for _ in range(10)]

    })

def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id')
    #Estou pedindo para filtar os objetos por categoria e id por categoria

    # category_name = getattr(
    #     getattr(recipes.first(), 'category', None),
    #     'name',
    #     'Not Found'
    # )
    # if not recipes:
    #     raise Http404('Not Found :/')
    recipes = get_list_or_404(Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id'))
    return render(request, 'receitas/pages/category.html', context={
        'receitas' : recipes,
        'title' : f'{recipes[0].category.name} - Category |'
                    
    })



def recipe(request, id):
    return render(request, 'receitas/pages/recipe-view.html', context={
        'receita' : make_recipe(),
        'is_detail_page': True,

    })
