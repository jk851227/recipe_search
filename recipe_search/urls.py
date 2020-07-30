from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search_food', views.food_list),
    path('recipe_info/<int:food_id>', views.recipe_info),
    path('random_meal', views.random_meal)
]
