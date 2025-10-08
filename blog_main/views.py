from django.shortcuts import render
from blogs.models import Category, Blogs
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect


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

#-Login View
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password= password)
            if user is not None:
                auth.login(request, user)
                return redirect( 'home' )
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'login.html',context)



#Logout View-----------------------
def logout(request):
    auth.logout(request)
    return redirect('home')



