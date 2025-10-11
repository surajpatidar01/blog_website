from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm,BlogPostForm
from django.template.defaultfilters import  slugify
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts=Blogs.objects.all().count()

    context={
       'category_counts':category_counts,
       'blogs_counts':blogs_counts
}
    return render(request,'dashboard.html',context)

#Category view-------
def categories(request):

    return render(request,'categories.html',)

#add category
def add_categories(request):
    if request.method =="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'add_categories.html', context)


#--delete category
def delete_categories(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()

    return redirect('categories')




#posts
def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'posts.html',context)

#---add  posts view
def add_posts(request):
    if request.method =="POST":
        form =BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data.get('title')
            post.slug = slugify(title)
            post.save()

            print('succsesss')
            return redirect('posts')
        else:
            print(form.errors)

    form = BlogPostForm()
    context = {
        'form': form
    }

    return render(request,'add_posts.html',context)

#--edit posts
def edit_posts(request, pk):
    post = Blogs.objects.get(pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)  # Edit hone ke baad kahin redirect karo
    else:
        form = BlogPostForm(instance=post)

    context = {
        'form': form
    }
    return render(request, 'edit_posts.html', context)

#delete post functionality
def delete_posts(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    post.delete()

    return redirect('posts')