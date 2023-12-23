from django.shortcuts import render,HttpResponse,redirect
from web import models
from .forms import BlogForm
from django.contrib import messages
# for paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.

def home(request):
    data=models.Blog.objects.all().values()
    print(data)
    return render(request,'index.html',{'data':data})

def aboutus(request):
    return render(request,'about.html')

def blog(request):

    blog_posts=models.Blog.objects.all()

    # Number of blog posts to display per page
    posts_per_page = 2

    paginator = Paginator(blog_posts, posts_per_page)
    print("fkhdsjfsjadfjosdaijo",paginator)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page',1)

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    

    return render(request,'blog.html',{'blogs':current_page,'current_page': current_page,'allblogs':blog_posts})

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=models.Contactus.objects.create(name=name,email=email,subject=subject,message=message)
        data.save()
        print(data)
        return HttpResponse("<script>alert('We will tuch you soon..');window.location.href='/contact/'</script>")
    return render(request,'contact.html')

def addNewBlog(request):
    if request.method=="POST":
        categories=request.POST.get('categories')
        title=request.POST.get('title')
        desc=request.POST.get('description')
        writer=request.POST.get('writer')
        image = request.FILES['image']
        bimage = request.FILES['bimage']
        data=models.Blog.objects.create(categories=categories,title=title,description=desc,writer=writer,image=image,banner_image=bimage)
        data.save()
         # Add a success message
        messages.success(request, 'New Blog added successfully.')
        return redirect('/showData/')
    return render(request,'addNewBlog.html')

def showData(request):
    data=models.Blog.objects.all().values()
    return render(request,'showBlogData.html',{'data':data})

def editBlog(request,id):
    data=models.Blog.objects.get(id=id)
    print(data)
    form=BlogForm(request.POST, request.FILES, instance=data)
    print(form)
    if form.is_valid():
        form.save()
         # Add a success message
        messages.success(request, 'Blog entry Updated successfully.')
        return redirect('/showData/')

    return render(request,'editBlog.html',{'blog':data})

def deleteBlog(request,id):
    data=models.Blog.objects.get(id=id)
    data.delete()
     # Add a success message
    messages.success(request, 'Blog entry deleted successfully.')

    return redirect('/showData/')


def postDetails(request, blog_id):
    # for recent blog showing in html table
    recent_blogs=models.Blog.objects.all().order_by('-date')[:4]

    print(f"Received blog_id: {blog_id}")
    blogs = models.Blog.objects.filter(id=blog_id)

    # Retrieve the specific blog post
    blog = models.Blog.objects.get(id=blog_id)

    # Retrieve all comments associated with the blog post
    comments = models.Comments.objects.filter(blog=blog)

    # comment counting for show total comment
    comment_count = comments.count()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        comment_text = request.POST.get('message')

        # Create a new comment associated with the specific blog post
        comment = models.Comments.objects.create(name=name, email=email, subject=subject, comments=comment_text, blog=blog)
        comment.save()


    return render(request, 'post-details.html', {'blogs': blogs,'recent_blogs':recent_blogs, 'comments': comments,'comment_count':comment_count})



# for comments on blog store
# , blog_id
# def blog_detail(request):
#     # blog = get_object_or_404(Blog, pk=blog_id)
#     # comments = blog.comments.all()

#     if request.method == 'POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         subject=request.POST.get('subject')
#         comments=request.POST.get('message')
#         data=models.Comments.objects.create(name=name,email=email,subject=subject,comments=comments)
#         data.save()
#         print(data)
#     return render(request, 'post-details.html', {'blog': blog})
# 'comments': comments