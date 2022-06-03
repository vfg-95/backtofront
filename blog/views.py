from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-posted_on")
    template_name = "home.html"


class BlogPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(post=post).order_by('-posted_on') 

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
