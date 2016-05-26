from django.http import HttpResponse, HttpResponseRedirect                      #to respond with 'custom' html
from django.shortcuts import render, get_object_or_404, redirect                #to respond with html pages (templates)
from .forms import PostForm                                                     #from forms.py
from .models import Post
from django.contrib import messages                                             #popup time ;)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger        #to use paginator

#CRUD                                                                           #function based views

def blog_create(request):                                                       #Create R U D
    form = PostForm(request.POST or None)                                       #"this field id required"
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()                                                         #stores in db
        messages.success(request, "Post Created!")                              #useless messages
        return HttpResponseRedirect(instance.get_absolute_url())                #redirects after edit
    context_data = {
        "form":form,
    }
    return render(request, 'post_form.html', context_data)

def blog_detail(request, id=None):                                              #C Retrieve U D
    instance = get_object_or_404(Post, id = id)
    context_data = {
        "title":instance.title,
        "instance":instance,
    }
    return render(request, 'post_detail.html', context_data)

def blog_list(request):                                                         #list items
    queryset_list = Post.objects.all()#.order_by("-timestamp")                       #queryset to get data from db
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page
        queryset = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page  of results.
        queryset = paginator.page(paginator.num_pages)

    context_data = {                                                            #context dict to pass data through pages
        "object_list":queryset,
        "title":"List",
        "page_request_var": page_request_var,
    }
    return render(request, 'post_list.html', context_data)

def blog_update(request, id=None):                                              #C R Update D
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance=instance)                    #"this field id required" + reloads data
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Updated!", extra_tags='some-tag')
        return HttpResponseRedirect(instance.get_absolute_url())
    context_data = {
        "title":instance.title,
        "instance":instance,
        "form":form
    }
    return render(request, 'post_form.html', context_data)

def blog_delete(request, id=None):                                              #C R U Delete
    instance = get_object_or_404(Post, id = id)
    instance.delete()
    messages.success(request, "Deleted!")
    return redirect("posts:list")
