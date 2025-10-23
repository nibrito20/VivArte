from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:list')  # Aqui seria para a página onde o usuário será redirecionado após o registro
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Verifica se o parâmetro 'next' foi passado na URL
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)  # Redireciona para a URL original que o usuário queria acessar
            else:
                return redirect('library:home')  # Redireciona para a página principal (home ou qualquer outra página que você defina)
    else:
        form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('library:list')  # Redireciona para a página de listagem ou homepage após logout
    
@login_required
def account_view(request):
    return render(request, 'users/account.html')