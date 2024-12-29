from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Sau khi đăng nhập thành công, chuyển đến trang home
            else:
                form.add_error(None, "Invalid login credentials")
    else:
        form = AuthenticationForm()

    return render(request, 'Dang_Nhap/login.html', {'form': form})
