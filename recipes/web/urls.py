from django.urls import path

from recipes.web.views import show_home, create_recipe, edit_recipe, details, delete_recipe

urlpatterns = (
    path('', show_home, name='show home'),
    path('create/', create_recipe, name='create'),
    path('edit/<int:pk>/', edit_recipe, name='edit'),
    path('details/<int:pk>/', details, name='details'),
    path('delete/<int:pk>/', delete_recipe, name='delete'),
)
