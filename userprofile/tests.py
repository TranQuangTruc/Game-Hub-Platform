from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client
from .models import Admin, Player, Designer, Developer

@pytest.mark.django_db
def test_main_view():
    client = Client()
    response = client.get(reverse('main'))  # Đảm bảo bạn có URL name='main'
    assert response.status_code == 200
    assert 'userprofile.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_userprofile_admin():
    client = Client()
    admin = Admin.objects.create(adminID=1, name="Admin Test")
    response = client.get(reverse('userprofile', args=['admin', admin.adminID]))
    assert response.status_code == 200
    assert 'userprofile.html' in [t.name for t in response.templates]
    assert response.context['user'] == admin
    assert response.context['role'] == 'admin'

@pytest.mark.django_db
def test_userprofile_invalid_role():
    client = Client()
    response = client.get(reverse('userprofile', args=['invalid', 1]))
    assert response.status_code == 200  # 404.html có thể trả về 200 nếu xử lý hợp lệ
    assert '404.html' in [t.name for t in response.templates]
    assert response.context['error'] == 'Invalid role'

@pytest.mark.django_db
def test_edit_user_profile(client, django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')
    response = client.post(reverse('userprofile'), {'username': 'updateduser'})
    assert response.status_code == 302  # Redirect về trang profile
    user.refresh_from_db()
    assert user.username == 'updateduser'

# Create your tests here.
