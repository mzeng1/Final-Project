from django.urls import path
from .views import HomeView, RecipeDetailView, AddRecipeView, UpdatePostView, DeletePostView, NewCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/edit/<int:pk>', UpdatePostView.as_view(), name='update_recipe'),
    path('recipe/delete/<int:pk>', DeletePostView.as_view(), name='delete_recipe'),
    path('post/<int:pk>/comment', NewCommentView.as_view(), name='add_comment'),
]
