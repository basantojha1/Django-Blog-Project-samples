from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# def home(request):
#     context = {}
#     return render(request, 'myblog/home.html', context)

class HomeView(ListView):
    model         = Post
    template_name = 'myblog/home.html'
    ordering      = ['-post_date']
    # ordering      = ['-id']

class ArticleView(DetailView):
    model         = Post
    template_name = 'myblog/article.html'

class AddPostView(CreateView):
    model         = Post
    form_class    = PostForm
    template_name = 'myblog/addpost.html'
    #fields        = '__all__'

class UpdatePostView(UpdateView):
    model         = Post
    form_class    = UpdateForm
    template_name = 'myblog/updatepost.html'
    # fields        = ['title','title_tag','body']

class DeletePostedView(DeleteView):
    model         = Post
    template_name = 'myblog/deletepost.html'
    success_url   = reverse_lazy('home')