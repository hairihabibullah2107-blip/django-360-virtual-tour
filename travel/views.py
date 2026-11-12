from django import forms
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9

def VirtualTour(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'virtual.html', {'posts': post})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

def PostDetails(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post.html', {'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})
