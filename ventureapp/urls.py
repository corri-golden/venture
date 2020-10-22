from django.urls import include, path
from django.conf.urls import url
from ventureapp import views
from django.urls import path




app_name = "ventureapp"


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    # path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', views.AboutView.as_view(), name="about"),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new', views.CreatePostView.as_view(), name= "post_new"), 
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name = "post_edit"),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name = "post_remove")
]
