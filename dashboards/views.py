from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm

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