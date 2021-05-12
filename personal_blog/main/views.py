from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView
from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *

@login_required(login_url='login')
def index(request):
    posts = Articles.objects.order_by('-date')
    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUser
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('index')
        context = {'form': form}
    return render(request, 'main/login.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            user = authenticate(request, username=username, password=password,email=email)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, '')

        context = {}
        return render(request, 'main/login.html', context)






class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/post.html'
    context_object_name = 'post'


def works(request):
    return render(request, 'main/works.html')