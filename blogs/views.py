from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Blogs, Category


def posts_by_category(request,category_id):
    #fetch the posts that belongs to the category with id category_id
    posts = Blogs.objects.filter(status ='published',category=category_id)

    category=get_object_or_404(Category,pk=category_id)
    context ={
        'posts':posts,

    }
    return render(request,'blog_main/posts_by_category.html',context)



#blogs

def blogs(request,slug):
    return  render(request,'blogs.html')
