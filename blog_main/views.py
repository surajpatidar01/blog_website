from django.shortcuts import render
from blogs.models import Category, Blogs
from .forms import RegistrationForm


def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True)
    posts = Blogs.objects.filter(is_featured=False, status='published')

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts,
    }
    return render(request, 'blog_main/home.html', context)

#[--------
def register(request):
    form = RegistrationForm()
    context = {

        'form': form,
    }
    return render(request,'register.html',context)

