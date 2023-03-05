from django.urls import path
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostedView
#from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('addpost', AddPostView.as_view(), name='addpost'),
    path ('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path ('article/<int:pk>/remove', DeletePostedView.as_view(), name='deletepost'),
]
