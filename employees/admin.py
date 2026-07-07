from django.contrib import admin
from .models import Department, Designation, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'email', 'department',
        'designation', 'salary', 'is_active', 'joining_date',
    )
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'designation', 'is_active', 'gender')
    ordering = ('-created_at',)