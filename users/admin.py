from django.contrib import admin
from products.admin import BasketAdmin

# Register your models here.
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)
