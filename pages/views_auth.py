from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    next_url = request.GET.get("next") or request.POST.get("next")
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect(next_url or 'dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html', {'next': next_url})

def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('login')