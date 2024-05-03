from django.shortcuts import render, redirect
from .forms import *

# Create your views here

# home controller
def home(request):
    # ana sayfada kullanılacak bilgileri alıyoruz
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'home.html', context)

def blog_detail(request, slug):
    context = {}

# login view controller
def login_view(request):
    return render(request, 'login.html')

# add blog controller
def add_blog(request):

    # request üzerinden gelen 'form' fieldını BlogForm olarak alıyoruz
    context = {'form': BlogForm}
    try:
        # gelen isteğin methodunun 'POST' olup olmadığını kontrol ediyoruz
        if request.method == 'POST':
            form = BlogForm(request.POST)
            title = request.POST.get('title')
            image = request.FILES['image']
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']

            # request üzerinden gelen bilgiler ile yeni veritabanına yeni bir kayıt ekleniyor
            BlogModel.objects.create(
                user = user, title = title,
                content = content, image = image
            )

            return redirect('/add_blog/')
    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)

# see blog controller
def see_blog(request): 
    return render(request, 'see_blog.html')

# register controller 
def register(request):
    return render(request, 'register.html')

# logout controller
def logout(request):
    return render(request, 'home.html')