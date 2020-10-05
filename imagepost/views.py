from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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
