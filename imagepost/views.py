from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import ImageTable


def signupview(request):
  if request.method == 'POST':
    username_data = request.POST['username_data']
    password_data = request.POST['password_data']
    try:
      user = User.objects.create_user(username_data, '', password_data)
    except IntegrityError:
      return render(request, 'signup.html', {'error': "ユーザー名 {0} は既に使用されています。".format(username_data)})
  else:
    return render(request, 'signup.html', {})
  return render(request, 'signup.html', {})


def loginview(request):
  if request.method == 'POST':
    username_data = request.POST['username_data']
    password_data = request.POST['password_data']
    user = authenticate(request, username=username_data, password=password_data)
    if user is not None:
      login(request, user)
      return redirect('list')
    else:
      return redirect('login')
  return render(request, 'login.html')


@login_required
def logoutview(request):
  logout(request)
  return redirect('login')


def listview(request):
  object_list = ImageTable.objects.all().order_by('-post_date')
  return render(request, 'list.html', {'object_list': object_list})


def detailview(request, pk):
  object_detail = ImageTable.objects.get(pk=pk)
  return render(request, 'detail.html', {'object': object_detail})


class CreateClass(CreateView):
  template_name = 'create.html'
  model = ImageTable
  fields = ('title', 'content', 'author', 'images', 'evaluation')
  success_url = reverse_lazy('list')
