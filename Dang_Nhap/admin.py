from django.contrib import admin
from .models import UserProfile  # Import model UserProfile

# Tùy chỉnh giao diện admin cho UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    # Hiển thị các trường trong danh sách
    list_display = ('user', 'favorite_game', 'high_score')
    
    # Thêm tính năng tìm kiếm
    search_fields = ('user__username', 'favorite_game')  # Tìm theo username của user hoặc tên game yêu thích
    
    # Thêm bộ lọc
    list_filter = ('favorite_game', 'high_score')

# Đăng ký model với class tùy chỉnh
admin.site.register(UserProfile, UserProfileAdmin)
