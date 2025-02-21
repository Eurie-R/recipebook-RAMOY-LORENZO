from django.urls import path 
from .views import recipelist, recipe1, recipe2

urlpatterns = [
    path('recipes/list/', recipelist, name='recipes'),
    path('recipes/1/', recipe1, name='recipe1'),
    path('recipes/2/', recipe2, name='recipe2')
    
    
]

app_name = "recipeapp"