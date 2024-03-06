import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('generate_random_code')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('generate_random_code')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def generate_random_code(request):
    if 'generated_code' not in request.session:  # Проверяем, был ли уже сгенерирован код
        random_code = random.randint(1000, 9999)
        request.session['generated_code'] = random_code
        return render(request, 'random_code.html', {'random_code': random_code})
    else:
        del request.session['generated_code']  # Удаляем сгенерированный код при перезагрузке страницы
        return redirect('login')
