from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Skill

# Create your views here.
def home(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	skills = Skill.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/home.html', {'posts': posts,'skills': skills})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})