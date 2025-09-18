from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
	model = Profile
	extra = 0
	max_num = 1
	can_delete = False

class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ["username", "first_name", "last_name", "email"]
	exclude = ['groups', 'user_permissions', 'password', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active']
	inlines = [ProfileInline]
	
	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		form.base_fields['username'].help_text = ''
		return form

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
