from django.contrib import admin
from .models import Player, Designer, Developer, Admin, CustomUser

# Đăng ký từng model riêng lẻ
admin.site.register(Player)
admin.site.register(Designer)
admin.site.register(Developer)
admin.site.register(Admin)
admin.site.register(CustomUser)

