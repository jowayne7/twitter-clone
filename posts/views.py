from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from urllib import request
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    #if method is POST
    if request.method =='POST':
        form= PostForm(request.POST, request.FILES)
        # if the form is valid
        if form.is_valid():
            #if yes then save the form
            form.save()
            # once saved redirect to Home page
            return HttpResponseRedirect('/')
        #if no, then show error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    
    #get all posts and limit =20
    posts=Post.objects.all()[:20]

    #show
    return render(request, 'posts.html',{'posts':posts} )
        
def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like_view (request,post_id):
    post = Post.objects.get(id = post_id)
    new_vaule = post.likes+1
    post.likes = new_vaule
    post.save()
    return HttpResponseRedirect('/')

def edit (request,post_id):
    post = Post.objects.get(id = post_id)
    if request.method=='POST':
        form= PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json)
    form= PostForm
    return render(request,'edit.html',{'post':post,'form':form })
        