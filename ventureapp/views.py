from django.shortcuts import render, reverse
from ventureapp.models import Post
from django.urls import reverse_lazy
from ventureapp.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (DeleteView, UpdateView, TemplateView, ListView, DetailView, CreateView)

# Create your views here.
# Mixins is used like decorators but for class based views

def home(request):
    return render(request, 'home.html', {})


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
    # this method is defining how I want to grab the list, which allows us to use django orm. be
    
    def get_queryset(self):
        return Post.objects
        # return Post.objects.filter(date)

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    
    #mixins take in a couple more attributes
    #if user is not logged in where should they go
    login_url = '/login/'
    #redirect
    redirect_field_name = 'ventureapp/post_detail.html'
    form_class = PostForm

    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'ventureapp/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    #we don't want success url to active until we delete, so we use reverse lazy
    #we don't want the 
    success_url = reverse_lazy('post_list')