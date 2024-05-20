from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'welcome.html')

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    instructions = recipe.instructions.split(';') if recipe.instructions else []
    instructions = [instr.strip() for instr in instructions if instr.strip()]  
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'instructions': instructions})