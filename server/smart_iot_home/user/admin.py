from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','useremail','password') # 사용자(User) 리스트 정보를 유저 이름과 비밀번호로 보이게 한다.

admin.site.register(User, UserAdmin)
