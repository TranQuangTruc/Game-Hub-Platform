import os
from datetime import datetime
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.db import models
from django.shortcuts import render

# Cau hinh Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamehub.settings')
application = get_wsgi_application()

# Model Asset quan ly thong tin cua tung tai nguyen (game asset)
class Asset(models.Model):
    name = models.CharField(max_length=255)  # Ten cua tai nguyen
    description = models.TextField()  # Mo ta tai nguyen
    file_path = models.CharField(max_length=500)  # Duong dan file tai nguyen
    asset_type = models.CharField(max_length=10, choices=[('free', 'Free'), ('paid', 'Paid')])  # Loai tai nguyen
    upload_date = models.DateTimeField(auto_now_add=True)  # Thoi gian upload tai nguyen

    def __str__(self):
        # Tra ve chuoi thong tin cua tai nguyen
        return f"Asset: {self.name}, Type: {self.asset_type}, Uploaded on: {self.upload_date}"

# Views de quan ly Asset
def upload_asset(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        file_path = request.POST.get('file_path')
        asset_type = request.POST.get('asset_type')
        
        # Tao doi tuong Asset
        asset = Asset.objects.create(
            name=name,
            description=description,
            file_path=file_path,
            asset_type=asset_type
        )
        asset.save()
        return render(request, 'success.html', {'message': f"Asset '{name}' uploaded successfully!"})
    return render(request, 'upload_asset.html')

# Views hien thi danh sach tai nguyen
def list_assets(request):
    free_assets = Asset.objects.filter(asset_type='free')
    paid_assets = Asset.objects.filter(asset_type='paid')
    return render(request, 'list_assets.html', {'free_assets': free_assets, 'paid_assets': paid_assets})
