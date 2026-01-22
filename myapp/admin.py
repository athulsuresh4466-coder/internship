from django.contrib import admin

from django.contrib import admin
from .models import Service, ServiceFeature




class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1




@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ServiceFeatureInline]


from .models import HomeService

@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)







from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created_at")
    list_filter = ("service", "created_at")
    search_fields = ("name", "email", "message")









from django.contrib import admin
from .models import Student
admin.site.register(Student)


