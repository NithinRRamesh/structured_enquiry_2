from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from django.utils import timezone
from .models import Blog

# Create your views here.


def login(request):
    return render(request,"blogger/login.html")


def create_blog(request):

    if(request.user.is_authenticated):
        return render(request,'blogger/create_blog.html')
    else:
       return redirect('login')

def create_blog_entry(request):
    title = request.POST['blog_title']
    description = request.POST['description']
    if (request.user.is_authenticated):
        username= request.user.username
        u = User.objects.get(username=username)
        u.blog_set.create(title=title,description=description,pub_date=timezone.now())
        return redirect('myblogs')
    else:
        return redirect('login')
def myblogs(request):
    if(request.user.is_authenticated):
        username = request.user.username
        u = User.objects.get(username=username)
        blog_list = u.blog_set.all()
        return render(request,'blogger/myblogs.html',context={'blogs_list': blog_list })
    else:
        return redirect('login')

def detail(request,blog_id):
    if(request.user.is_authenticated):
        blog = Blog.objects.get(pk=blog_id)
        try:
            blog = Blog.objects.get(pk=blog_id)
        except blog.DoesNotExist:
            raise Http404("Blog does not exist")
        return render(request, 'blogger/detail.html', {'blog': blog})
    else:
        return redirect('login')

def delete_blog(request):
    if(request.user.is_authenticated):
        username = request.user.username
        u = User.objects.get(username=username)
        blog_list = u.blog_set.all()
        return render(request,'blogger/delete_blog.html',context={'blogs_list': blog_list })
    else:
        return redirect('login')

def delete(request,blog_id):
    if(request.user.is_authenticated):
        try:
            blog = Blog.objects.get(pk=blog_id)
        except blog.DoesNotExist:
            raise Http404("Blog does not exist")
        blog.delete()
        return redirect('myblogs')
    else:
        return redirect('login')


def home(request):
    if(request.user.is_authenticated):
        blogs_list = Blog.objects.all()
        return render(request,'blogger/allblogs.html',{'blogs_list':blogs_list})
    else:
        return redirect('login')

def create_user(request):
    if(request.user.is_authenticated):
        if(request.user.is_superuser):
            if(User.objects.count()<=13):
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                first_name = request.POST['firstname']
                last_name = request.POST['lastname']
                u = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                u.save()
                return redirect('home')
            else:
                return render(request,"blogger/limitscrossed.html")
        else:
            return render(request,"blogger/sorryperm.html")
    else:
        return redirect('login')

def create_user_form(request):
    if (request.user.is_authenticated):
        if (request.user.is_superuser):
            return render(request, "blogger/createuser.html")
        else:
            return render(request, "blogger/sorryperm.html")
    else:
        return redirect('login')

def forgot_password_form(request):
    return render(request,"blogger/forgotpassword.html")

def forgot_password(request):
    email = request.POST['email']
    try:
        u = User.objects.get(email=email)
    except u.DoesNotExist:
        raise Http404("email doesnot exist")
        return render(request,"blogger/sorryperm.html")
    request.session['email']=email
    return render(request,"blogger/change_password.html")

def change_password(request):
    email = request.session['email']
    u = User.objects.get(email=email)
    password = request.POST['password']
    u.set_password(password)
    u.save()
    return redirect('login')
