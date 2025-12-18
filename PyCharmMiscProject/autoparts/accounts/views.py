from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте данные.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        print(f"POST данные получены: username={request.POST.get('username')}")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Форма валидна, проверяем пользователя: {username}")
            user = authenticate(username=username, password=password)
            print(f"Результат authenticate: {user}")

            if user is not None:
                login(request, user)
                print(f"Пользователь вошел: {request.user.is_authenticated}")
                messages.success(request, f'Добро пожаловать, {username}!')
                next_url = request.GET.get('next', 'profile')
                print(f"Редирект на: {next_url}")
                return redirect(next_url)
            else:
                print("Пользователь не найден или неверный пароль")
        else:
            print(f"Ошибки формы: {form.errors}")
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def about(request):
    return render(request, 'about.html')