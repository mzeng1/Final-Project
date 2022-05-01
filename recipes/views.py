from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from recipes.models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class RecipeDetailView(DetailView):
    model = Post
    template_name = 'recipe_details.html'


class AddRecipeView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_recipe.html'
    # fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_recipe.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')


class NewCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('feed')
    #
    # def handle_no_permission(self):
    #     return redirect('log_in')