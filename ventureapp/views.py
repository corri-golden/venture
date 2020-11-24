from django.shortcuts import render, reverse, get_object_or_404
from ventureapp.models import Post, Comment
from . import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from ventureapp.forms import PostForm, PostCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (DeleteView, UpdateView, TemplateView, ListView, DetailView, CreateView)
from django.http import HttpResponseRedirect

# Create your views here.
# Mixins is used like decorators but for class based views

def home(request):
    return render(request, 'home.html', {})


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = models.Post
    #python turns the name of the model lowercase and add _list.  for example post_list, which is used in the fourloop on the front end.

    #if you want to make that a easier name to understand you can
    context_object_name = 'posts'

    # this method is defining how I want to grab the list, which allows us to use django orm. be
    
    # def post_publish(request,pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     post.publish()
    #     return redirect('post_list',pk=pk)

    # def get_queryset(self):
    #     return Post.objects
        # return Post.objects.filter(date)

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
            # look in the db to see what post we are on
            # this will grab from post table the post with id of pk we are own | total like come model .py
            post_menu = Post.objects.all()
            context = super(PostDetailView, self).get_context_data(*args, **kwargs)
            stuff = get_object_or_404(Post, id=self.kwargs['pk'])
            total_likes = stuff.total_likes()

            liked = False

            if stuff.likes.filter(id=self.request.user.id).exists():
                liked = True
            context["total_likes"] = total_likes
            context["post_menu"] = post_menu
            context["liked"] = liked    
            return context
    #same for detail view except it lowercase the model.
    # context_object_name = 'post_detail'

class CreatePostView(LoginRequiredMixin, CreateView):
    
    #mixins take in a couple more attributes
    #if user is not logged in where should they go
    login_url = '/login/'
    #redirect
    redirect_field_name = 'ventureapp/post_list.html'
    form_class = PostForm
    model = models.Post

class AddCommentView(CreateView):
    model = Post
    #mixins take in a couple more attributes
    #if user is not logged in where should they go
    # login_url = '/login/'
    #redirect
    redirect_field_name = 'ventureapp/post_list.html'
    form_class = PostCommentForm
    template_name = "add_comment.html"
    success_url = reverse_lazy('ventureapp:post_list')
    
    # this is a way to hold the form information which passes the post id.  
    def form_valid(self, form):
        #the pk get passed as a kwarg.  we can take it and assign to post id
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'ventureapp/post_list.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    #we don't want success url to active until we delete, so we use reverse lazy
    #we don't want the 
    success_url = reverse_lazy('ventureapp:post_list')




# As a function view just cause its easier.  When it's called we want to save to the db.  We need to know the which post and save.
def LikeView(request, pk):
    # look up Post and grab the id that equals the request | post_id come from the name in post detail.  Which ever id it is lookit up in the post variable.
    # and assign to post variable then save
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    like = False
    # the request passes in the user which contains whether the user is logged in.  look up if a like has been liked by 
    #user 1 and if it exist do something
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        # we are saving a like from a user.
        post.likes.add(request.user)
        liked = True
        #to redirect to the same page.
        # pass the id to know id
    return HttpResponseRedirect(reverse('ventureapp:post_detail', args=[str(pk)]))


def comment_list(request, author_id):
    comments = Comment.objects.filter(author_id=author_id).order_by('when')
    author = Author.objects.get(id=author_id)





    





