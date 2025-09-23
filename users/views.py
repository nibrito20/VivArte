from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

#mudar todos os library:list para library:home, NAO EH PRA FAZER ISSO AINDA SO QUANDO A GNT ADICIONAR HOME NO LIBRARY

def register_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('library:list')
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form})

def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) 
            else:
                return redirect('library:list')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form})
    #ia ser legal um java script aqr pra dar um alert que a conta nao existe ou que a senha ta incorreta algo assim
    
    
def logout_view(request):
    
    if request.method == "POST":
        logout(request)
        return redirect('library:list')

