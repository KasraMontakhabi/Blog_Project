from django.shortcuts import render, get_object_or_404,redirect
from Blog.models import Post, Comment
from Blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

#################################################################
#################################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect("post_detail", pk = pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST": #some one has filled the form and hit enter
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False) 
            comment.post = post
            comment.save()
            return redirect("post_detail", pk = post.pk)
    else:
        form = CommentForm()
    return render(request, "Blog/comment_form.html", {"form":form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect("post_detail", pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("post_detail", pk = post_pk) #if we use comment.post.pk instead of post_pk, by the time we delete comment then python would not understand 
    # what is comment, because it is deleted