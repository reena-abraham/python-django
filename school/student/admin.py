from django.contrib import admin
from . models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone")


admin.site.register(Student, StudentAdmin)
