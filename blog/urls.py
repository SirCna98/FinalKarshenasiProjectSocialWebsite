from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AddCommentView,
    news,
    contact,
    writer,
    about,
    calender
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('news/', news, name='blog-news'),
    path('contact/', contact, name='blog-contact'),
    path('writer/', writer, name='blog-writer'),
    path('about/', about, name='blog-about'),
    path('calender/', calender, name='blog-calender'),
    path('post/<int:pk>/commnet', AddCommentView.as_view(), name ='add_comment'),
]
