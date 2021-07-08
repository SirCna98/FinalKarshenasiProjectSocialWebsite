from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView

)
from .models import Post , Comment
from users.models import Profile
from django.urls import reverse_lazy
#from django import forms

def home(request):
    context = {
        'posts': Post.objects.all(),
	'comments': Comment.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.all().order_by('-date_posted'),
            'comments': Comment.objects.all(),
        })
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False

def news(request):
    return render(request, 'blog/news.html', {'title': 'News'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact Us'})

def writer(request):
    profiles = Profile.objects.all()
    context = {
        'title': 'writer',
        'profiles': profiles
    }
    return render(request, 'blog/writer.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

    
def calender(request):
    return render(request, 'blog/calender.html', {'title': 'calender'})


#class CommentForm(forms.ModelForm):
#    class Meta:
#        model =Comment
#        fields = ('post', 'body', 'date_added')
#        widgets = {
#             'post':forms.TextInput(attrs ={'class':'form.control' }),
#             'body':forms.TextInput(attrs ={'class':'form.control' }),
#             'date_added':forms.TextInput(attrs ={'class':'form.control' })
#                }


class AddCommentView(CreateView):
    model = Comment
#    form_class = CommentForm
    template_name = 'blog/addcomment.html'
#    fields = '__all__'
    fields = ("body",)
    success_url = reverse_lazy('blog-home')
#    reverse_lazy(viewname, urlconf=None, args=None, kwargs=None, current_app=None)

    def form_valid(self,form):
        form.instance.author = self.request.user.username
        post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)


