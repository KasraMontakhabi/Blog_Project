from django.shortcuts import render
from Blog.models import Post, Comment
from Blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  
        # This is like writing a query # __lte = less than or equal 

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView): #mixin deos the same work that login required decorator does for the view functions
    # mixine attributes
    login_url = "/login/"
    redirect_field_name = "Blog/post_detail.html"
    form_class = PostForm
    # mixine attributes

    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # mixine attributes
    login_url = "/login/"
    redirect_field_name = "Blog/post_detail.html"
    form_class = PostForm
    # mixine attributes

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "Blog/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")