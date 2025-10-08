from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Blogs, Category
from django.db.models import Q


def posts_by_category(request,category_id):
    #fetch the posts that belongs to the category with id category_id
    posts = Blogs.objects.filter(status ='published',category=category_id)

    category=get_object_or_404(Category,pk=category_id)
    context ={
        'posts':posts,

    }
    return render(request,'blog_main/posts_by_category.html',context)



#blogs

# def blogs(request,slug):
#     single_post = get_object_or_404(Blogs,slug=slug,status='published')
#     context= {
#         'single_post':single_post,
#     }
#     return  render(request,'blogs.html',context)




def blogs(request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')

    context = {
        'single_post': single_post,

    }

    return render(request, 'blogs.html', context)


#Search Functionality
# def search(request):
#     keyword = request.GET.get('keyword')
#     blog = Blogs.objects.filter(title__icontains=keyword)
#     content = {
#         'blog': blog,      # same variable name as above
#         'keyword': keyword # comma added
#     }
#     return render(request, 'search.html', content)



def search(request):
    query = request.GET.get('q')  # 'q' likhna hai, 'keyword' nahi
    if query:  # check karo query empty na ho
        blog = Blogs.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(body__icontains=query))
    else:
        blog = Blogs.objects.none()  # agar query nahi hai to empty result

    return render(request, 'search.html', {'blog': blog})



