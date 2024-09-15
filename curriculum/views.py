from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def homeblog(request):
#   return redirect('article-detail',{'pk':1})
    return redirect(reverse('article-detail', kwargs={'pk':1}))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-due_date']
#   ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
#   fields =  '__all__'
#   fields =  ('title','body')

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html' 
#   fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html' 
    success_url = reverse_lazy('home')



class CategoryHomeView(ListView):
    model = Category
    template_name = 'category_list.html'
    ordering = ['-id']

class AddCategoryView(CreateView):
    model = Category
#   form_class = CategoryForm
    template_name = 'add_category.html'
    fields =  '__all__'
#   fields =  ('title','body')

class EditCategoryView(UpdateView):
    model = Category
    form_class = EditForm
    template_name = 'edit_category.html' 
#   fields = ['title','title_tag','body']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.title())
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts': category_posts})


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')
