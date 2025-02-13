
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Admin, Player, Designer, Developer

# Trang chủ, chỉ hiển thị template mà không truyền dữ liệu
def main(request):
    return render(request, 'userprofile.html')

# Hàm xử lý hiển thị thông tin người dùng theo vai trò và ID
def userprofile(request, role, user_id):
    # Xác định đối tượng người dùng theo vai trò
    user = None
    if role == "admin":
        user = get_object_or_404(Admin, adminID=user_id)
    elif role == "player":
        user = get_object_or_404(Player, playerID=user_id)
    elif role == "designer":
        user = get_object_or_404(Designer, designerID=user_id)
    elif role == "developer":
        user = get_object_or_404(Developer, developerID=user_id)
    else:
        # Trả về trang 404 nếu vai trò không hợp lệ
        return render(request, '404.html', {'error': 'Invalid role'})

    # Truyền dữ liệu người dùng và vai trò vào template
    return render(request, 'userprofile.html', {'user': user, 'role': role})

from django.shortcuts import render, redirect
from .forms import UserProfileForm

def userprofile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("userprofile")  # Điều hướng về trang profile sau khi lưu
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, "userprofile.html", {"form": form})
